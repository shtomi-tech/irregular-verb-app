import os
import random
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# --- データベースの設定 ---
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "verbs.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# --- データベースの「型（モデル）」を定義 ---
class Verb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    infinitive = db.Column(db.String(50), nullable=False)      # 原形
    past_simple = db.Column(db.String(50), nullable=False)     # 過去形
    past_participle = db.Column(db.String(50), nullable=False) # 過去分詞形
    correct_count = db.Column(db.Integer, default=0)           # 正解数
    incorrect_count = db.Column(db.Integer, default=0)         # 不正解数

    def __repr__(self):
        return f'<Verb {self.infinitive}>'

@app.route('/')
def quiz():
    all_verbs = Verb.query.all()
    if not all_verbs:
        return "データベースに動詞がありません。create_db.pyを実行してください。"

    weights = [verb.incorrect_count + 1 for verb in all_verbs]
    chosen_verb = random.choices(all_verbs, weights=weights, k=1)[0]
    
    verb_set_list = [chosen_verb.infinitive, chosen_verb.past_simple, chosen_verb.past_participle]
    blank_index = random.randint(0, 2)
    
    return render_template('index.html', 
                           verb_set=verb_set_list, 
                           blank_index=blank_index,
                           verb_id=chosen_verb.id)

@app.route('/stats')
def stats():
    all_verbs = Verb.query.order_by(Verb.incorrect_count.desc()).all()
    return render_template('stats.html', verbs=all_verbs)

@app.route('/check', methods=['POST'])
def check_answer():
    user_answer = request.form['user_answer']
    correct_answer = request.form['correct_answer']
    verb_id = request.form['verb_id']

    verb_to_update = Verb.query.get(verb_id)

    if user_answer.lower().strip() == correct_answer.lower().strip():
        verb_to_update.correct_count += 1
        result_status = 'correct'
        message = '🎉 正解！'
    else:
        verb_to_update.incorrect_count += 1
        result_status = 'incorrect'
        message = f'残念！正解は {correct_answer} でした。'

    db.session.commit()

    return jsonify({'result': result_status, 'message': message})

if __name__ == '__main__':
    app.run(debug=True)