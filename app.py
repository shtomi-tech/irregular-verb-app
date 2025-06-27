# app.py

import os
import random
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# --- 基本設定 ---
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'verbs.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# --- データベースのモデル定義 ---
class Verb(db.Model):
    __tablename__ = 'verbs'
    id = db.Column(db.Integer, primary_key=True)
    infinitive = db.Column(db.String(50), nullable=False)
    past_simple = db.Column(db.String(50), nullable=False)
    past_participle = db.Column(db.String(50), nullable=False)
    correct_count = db.Column(db.Integer, default=0)
    incorrect_count = db.Column(db.Integer, default=0)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)

# --- アプリのルート（URL）定義 ---
@app.route('/')
def quiz():
    all_verbs = Verb.query.all()
    if not all_verbs:
        return "<h1>データベースを準備中です。数分後にもう一度アクセスしてください。</h1>"
    weights = [v.incorrect_count + 1 for v in all_verbs]
    chosen_verb = random.choices(all_verbs, weights=weights, k=1)[0]
    verb_set_list = [chosen_verb.infinitive, chosen_verb.past_simple, chosen_verb.past_participle]
    blank_index = random.randint(0, 2)
    return render_template('index.html', verb_set=verb_set_list, blank_index=blank_index, verb_id=chosen_verb.id)

@app.route('/check', methods=['POST'])
def check_answer():
    verb_to_update = Verb.query.get(request.form['verb_id'])
    user_answer = request.form['user_answer'].lower().strip()
    correct_answer = request.form['correct_answer'].lower().strip()
    if user_answer == correct_answer:
        verb_to_update.correct_count += 1
        result = {'result': 'correct', 'message': '🎉 正解！'}
    else:
        verb_to_update.incorrect_count += 1
        result = {'result': 'incorrect', 'message': f"残念！正解は {request.form['correct_answer']} でした。"}
    verb_to_update.last_updated = datetime.utcnow()
    db.session.commit()
    return jsonify(result)

@app.route('/stats')
def stats():
    all_verbs = Verb.query.order_by(Verb.incorrect_count.desc()).all()
    return render_template('stats.html', verbs=all_verbs)

# --- メインの実行部分 ---
if __name__ == '__main__':
    print("🚀 不規則動詞クイズアプリケーションを起動中...")
    print("📱 ブラウザで http://localhost:5000 にアクセスしてください")
    print("⏹️  停止するには Ctrl+C を押してください")
    print("-" * 50)
    app.run(debug=True, host='0.0.0.0', port=5000)