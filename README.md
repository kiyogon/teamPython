# 動作確認方法

## ①Dockerコンテナを立ち上げる

下記をターミナルで実行

`docker-compose up --build`

補足：Dockerコンテナを停止・削除するには
`docker-compose down`

## ②初回起動時にテーブルを作成する

下記をターミナルで実行

1. マイグレーションファイルの作成
`docker-compose exec web python manage.py makemigrations`

2. マイグレーション
`docker-compose exec web python manage.py migrate`


## ④動作確認
ブラウザで画面を表示する
http://127.0.0.1:8000/
をブラウザに打ち込みロード

### ④で立ち上がらない場合

webサーバー用のコンテナをリロードする

1. webサーバー用のコンテナをクリック
<img width="1302" alt="スクリーンショット 2024-06-12 12 35 22" src="https://github.com/kiyogon/teamPython/assets/26045410/45d4f10c-7200-4333-ac73-fe8005b09b00">

2. リロードボタンを押す
<img width="698" alt="スクリーンショット 2024-06-12 12 36 31" src="https://github.com/kiyogon/teamPython/assets/26045410/59295c1f-9a14-40f1-9a38-07b36b003c48">

3. http://127.0.0.1:8000/にアクセスしてみる

これでも立ち上がらない場合は別途ご相談ください。

# Djangoの使い方

## 新規のページを追加したいとき
1. 01_pages配下にhogehoge.htmlをつくる
2. appsディレクトリ配下のurls.pyにパスを追加する
3. appsディレクトリ配下のviews.pyに関数を作成し、POST, GET時の処理を書く

## 独自のTemplate構文

1. 変数
   テンプレートで変数を表示するには、`{{ variable_name }}`を使用します。
   例: `<p>{{ user_name }}</p>`

2. タグ
   テンプレートでロジックを実行するには、`{% tag %}`を使用します。
   例: `{% if user.is_authenticated %} <p>Welcome, {{ user_name }}!</p> {% endif %}`

3. フィルタ
   変数の表示を変更するには、`{{ variable|filter }}`を使用します。
   例: `<p>{{ text|upper }}</p>`で変数textが全て大文字に変換される

4. forループ
   リストの各アイテムに対してループ処理を行うには、`{% for item in list %}`を使用します。
   例: `{% for item in item_list %} <li>{{ item }}</li> {% endfor %}`

5. if文
   条件に基づいて処理を分岐するには、`{% if condition %}`を使用します。
   例: `{% if user.is_active %} <p>Active User</p> {% else %} <p>Inactive User</p> {% endif %}`

6. コメント
   テンプレート内でコメントを記述するには、`{# comment #}`を使用します。
   例: `{# これはコメントです #}`


7. extendsタグ
   ベーステンプレートを継承するには、`{% extends 'base.html' %}`を使用します。
   例: `{% extends 'layout.html' %}`

8. blockタグ
   継承したテンプレートのブロックをオーバーライドするには、`{% block block_name %}`を使用します。
   例: `{% block content %} <p>This is the content.</p> {% endblock %}`

9. csrf_tokenタグ
    POSTフォームでCSRF（シーサーフ）保護を行うには、`{% csrf_token %}`をフォーム内に含めます。
    例: `<form method="post">{% csrf_token %} ... </form>`


## 新規のテーブルをDBに追加する

1. models.pyにmodelを追加
2. migrationを行う
```
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

3. postgresでテーブルが確認できればOK
ただし、テーブル名は`Djangoに設定したアプリ名_テーブル名`になっています。

## DBに接続する方法

方法①

コマンドラインからDockerコンテナ内のPostgreSQLに接続
`docker-compose exec db psql -U user -d dbs`

もしくは DockerDesktopのコンテナのexecから接続
`psql -U user -d dbs`

全テーブルの確認
`\dt`

特定のテーブルの詳細を見る
`\d table_name`

方法②
pdAdminから確認

## Django admin用アカウントの作成
docker-compose exec web python manage.py createsuperuser
