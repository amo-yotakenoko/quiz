# 起動方法
```
docker compose up -d
```
http://127.0.0.1:5000/ でアプリにアクセスできます

## マイグレーション
```
docker compose exec app flask --app flask_app db upgrade
```

## 仮想環境のセットアップ
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```