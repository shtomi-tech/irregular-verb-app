#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
不規則動詞クイズアプリケーション起動スクリプト
"""

import os
import sys
from app import app, db

def main():
    """メイン実行関数"""
    print("🚀 不規則動詞クイズアプリケーションを起動中...")
    
    # データベースファイルの存在確認
    db_path = os.path.join(os.path.dirname(__file__), 'verbs.db')
    if not os.path.exists(db_path):
        print("⚠️  データベースファイルが見つかりません。")
        print("📝 データベースを初期化します...")
        try:
            with app.app_context():
                db.create_all()
            print("✅ データベースの初期化が完了しました。")
        except Exception as e:
            print(f"❌ データベース初期化エラー: {e}")
            return
    
    print("🌐 アプリケーションを起動しています...")
    print("📱 ブラウザで http://localhost:5000 にアクセスしてください")
    print("⏹️  停止するには Ctrl+C を押してください")
    print("-" * 50)
    
    # 開発サーバーを起動
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main() 