# 環境変数にFLASK_APPを設定
$env:FLASK_APP = "setup.py"

# データベースの初期化
python -m flask db init

# 現在のデータベースの状態をheadにスタンプ
python -m flask db stamp head

# マイグレーションファイルを作成
python -m flask db migrate -m 'db start'

# マイグレーションを適用してデータベースをアップグレード
python -m flask db upgrade

# Flaskアプリケーションを起動
python setup.py
