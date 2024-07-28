# 起動方法

## ローカル
開発時はローカルで作業することもできます。
ローカルでアプリを起動するには以下のコマンドを実行します（Dockerが必要です）。
```
docker compose up -d
```
コマンド実行後、以下のログが表示後ブラウザで `http://127.0.0.1:5000/` でアプリにアクセスできます
```
app-1  |  * Debug mode: on
app-1  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
app-1  |  * Running on all addresses (0.0.0.0)
app-1  |  * Running on http://127.0.0.1:5000
app-1  |  * Running on http://172.20.0.3:5000
```

## 本番環境（Kubernetes）
Kubernetes上でアプリを実行するにはリポジトリ上のマニフェストを適用します。
まず`kubectl`コマンドが使えるサーバ上でリポジトリをクローンします。
そして以下のコマンドで`manifest`ブランチに切り替えます。そうするとマニフェストが入った`manifest`ディレクトリが現れます。
```
git checkout manifest
```
次のコマンドでクラスタにマニフェストを適用します。
```
kubectl apply -f ./manifests
```
次に以下のコマンドでクラスタ上にPodやServiceが展開されたか確認します。
```
kubectl get pod
kubectl get service
```
quiz-appという名前のPodのStatusがRunningになっていたらアプリが正常に起動しています。
quiz-appという名前のServiceのポート番号を確認しブラウザから`http://<ノードのIPアドレス>:<ポート番号>/`でアプリにアクセスします。

マニフェストファイルはリポジトリのmainブランチにpushするたびにGitHub Actionsにより更新されます。
更新後のマニフェストファイルを用いるには`git pull`後に`kubectl apply`を行います。


# 仮想環境のセットアップ
ローカルで開発する際にVSCode上でコード補完機能を利用するには以下のコマンドを実行します。
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
