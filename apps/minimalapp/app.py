from flask import Flask,render_template,url_for,current_app,g


app = Flask(__name__)





# URLと実行する関数をマッピングする
@app.route("/")
def index():
    return "Hello, Flaskbook!"


@app.route("/hello/<name>", methods=["GET","POST"], endpoint="hello-endpoint")
def hello(name):
    return f"Hello, {name}"


# show_nameエンドポイントを作成する
@app.route("/name/<name>")
def show_name(name):
    # 変数をテンプレートエンジンに渡す
    return render_template("index.html", name=name)

