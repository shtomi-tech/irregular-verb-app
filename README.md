# 不規則動詞クイズアプリケーション

英語の不規則動詞を学習するためのWebアプリケーションです。

## 🚀 簡単起動方法

### Windowsの場合
1. プロジェクトフォルダを開く
2. `start.bat` をダブルクリック
3. ブラウザで `http://localhost:5000` にアクセス

### 手動起動の場合
```bash
# 仮想環境を作成（初回のみ）
python -m venv venv

# 仮想環境をアクティベート
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 依存関係をインストール
pip install -r requirements.txt

# アプリケーションを起動
python run.py
```

## 📱 使用方法

1. **クイズ**: ホームページで不規則動詞のクイズに挑戦
2. **統計**: `/stats` ページで学習進捗を確認
3. **間違いが多い動詞**: 間違えた動詞ほど頻繁に出題される仕組み

## 🛠️ 技術スタック

- **Flask**: Webフレームワーク
- **SQLAlchemy**: データベースORM
- **SQLite**: データベース
- **HTML/CSS/JavaScript**: フロントエンド

## 📁 ファイル構成

```
irregular-verb-app/
├── app.py          # メインアプリケーション
├── run.py          # 起動スクリプト
├── start.bat       # Windows用起動ファイル
├── requirements.txt # Python依存関係
├── templates/      # HTMLテンプレート
│   ├── index.html  # クイズページ
│   └── stats.html  # 統計ページ
└── verbs.db        # データベースファイル
```

## 🎯 機能

- ✅ 不規則動詞のクイズ機能
- ✅ 正解・不正解の記録
- ✅ 間違いが多い動詞の優先出題
- ✅ 学習統計の表示
- ✅ レスポンシブデザイン

## 🔧 トラブルシューティング

### データベースエラーが発生する場合
```bash
python init_db.py
```

### ポート5000が使用中の場合
`run.py` の `port=5000` を別のポート番号に変更してください。

## 📞 サポート

問題が発生した場合は、以下を確認してください：
1. Python 3.7以上がインストールされているか
2. 仮想環境が正しくアクティベートされているか
3. 依存関係が正しくインストールされているか 