@echo off
chcp 65001 >nul
echo 🚀 不規則動詞クイズアプリケーションを起動中...
echo.

REM 仮想環境の確認とアクティベート
if exist "venv\Scripts\activate.bat" (
    echo 📦 仮想環境をアクティベート中...
    call venv\Scripts\activate.bat
) else (
    echo ⚠️  仮想環境が見つかりません。新しく作成します...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo 📦 依存関係をインストール中...
    pip install -r requirements.txt
)

echo.
echo 🌐 アプリケーションを起動しています...
echo 📱 ブラウザで http://localhost:5000 にアクセスしてください
echo ⏹️  停止するには Ctrl+C を押してください
echo.

python run.py

pause 