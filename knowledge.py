'''
test comment
# Flaskに関するナレッジドキュメントファイ
## 1. まず公式ドキュメント通りにインストール
リンク通り進めば環境構築できる、一方でpyファイル作成してimportしても使える。
[Flask]
https://a2c.bitbucket.io/flask/installation.html#installation

[Jinja2]
http://jinja.pocoo.org/docs/dev/


## 2. クイックスタートで、3分でアプリ作成
Flaskのお作法が出てくる。おまじないとして覚えて理解後手でも良い。
途中で難しいと感じたら、参考リンクの写経すると良い。
https://a2c.bitbucket.io/flask/quickstart.html#id2

## 3. CSS, JSとの連携
jinja2テンプレート
共通部分はlayout.htmlに記載するため、header, footerはlayoutにまとめる
### すべての画面に CSS や JavaScript を読み込むためのヘッダーなどを書くのは面倒ですし無駄です。
### そこでウェブアプリケーションでは共通の部分のみを layout.html のようにレイアウト用の HTML をひとつ用意してしまうのが普通です。

staticファイル
### url_for('static', filename='style.css')
### そのファイルは、ファイルシステム上に static/style.css という名前で保存されます。

### 以下のコードが非常に分かりやすい。
### htmlからリンクを引っ張ってくるときの引き出し元ディレクトリはstatic以下で、特殊な呼び方じゃないと引き出せませんよってだけ。（URL_FOR構文）

<!-- index.html -->
<!DOCTYPE html>
<html lang="ja">
  <head>
    <link rel="stylesheet" href="{{url_for('static', filename='index.css')}}">
    <script src="{{url_for('static', filename='index.js')}}"></script>
  </head>
  <body>

    <h1>Hello</h1>
    <h2 id='test'>World</h2>

  </body>
</html>


## 4. DB接続
### 選定において、プロコン仕切れていないため、dynamodb以外により良いDBがあるんではないか。
### NOSQLでいえば、MONGODBでも良い（学習コストが低いため）
-- 2018/03/20 --
### Mongodbに確定
### pymongoをインポートして利用する


w/ dynamodb
https://github.com/rdegges/flask-dynamo








## 5. 並列処理
https://qiita.com/5zm/items/251be97d2800bf67b1c6




## 参考リンク
### 全般的にとても易しく書かれている。超初心者向け。
https://qiita.com/zaburo/items/5091041a5afb2a7dffc8

### 説明はあまりなく進んでいく。後半はHerokuへのデプロイ方法がある。
https://qiita.com/k-nishigaki/items/f9f49b4749395ab5091c#_reference-f4f5c565040baa9791fb

### 一番上の記事同様様々なレシピが載っている。CSS, JS読み込み部分にも触れている。
http://python.zombie-hunting-club.com/entry/2017/11/03/223503#%E6%9B%B8%E7%B1%8D

### 全体的に明快な記事。CSSのファイルの置き方なども記載されている。
https://qiita.com/ynakayama/items/2cc0b1d3cf1a2da612e4

### Blueprint
https://www.yoheim.net/blog.php?q=20160905

### 一言多いプログラマーの独り言。小ネタ集的な感じで様々なtipsが載っている。
https://programmer-jobs.blogspot.jp/2018/03/python-flask-jinja2-registering-custom-filters.html

### 将来的にはこういった使い方もしていきたい。画像認識周りと相性が良さそう。
https://qiita.com/AkiyoshiOkano/items/dc19bffc88c549393699#_reference-91891460bbb635a9f065

### MongoDBの基本的な使い方
https://qiita.com/yanoojapan/items/91d4090b263cef7af4e8

### pythonからpymongoを触ってみる
http://nwpct1.hatenablog.com/entry/python-flask-mongodb

### 
'''