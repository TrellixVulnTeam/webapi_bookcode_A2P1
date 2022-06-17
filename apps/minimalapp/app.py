import logging
import os
from flask import Flask,render_template,url_for,current_app,g,request,redirect,make_response,session,flash
from email_validator import EmailNotValidError, validate_email
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail, Message

app = Flask(__name__)


# SECRET_KEYを追加する
app.config["SECRET_KEY"] = "2AZSMss3p5QPbcY2hBsJ"


# リダイレクトを中断しないようにする
app.logger.setLevel(logging.DEBUG)

# DebugToolbarExtensionにアプリケーションをセットする
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

# Mailクラスのコンフィグを追加する




app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # 电子邮件服务器的主机名或IP地址
app.config['MAIL_PORT'] = 587  # 电子邮件服务器的端口
app.config['MAIL_USE_TLS'] = True  # 启用传输层安全
# 注意这里启用的是TLS协议(transport layer security)，而不是SSL协议所以用的是25号端口
app.config['MAIL_USERNAME'] = 'wmeadal@gmail.com'  # 你的邮件账户用户名
app.config['MAIL_PASSWORD'] = 'awqvkfgtdwfxajjs'  # 邮件账户的密码,这个密码是指的授权码!授权码!授权码!
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER")


# flask-mailコンフィグ設定

# DebugToolbarExtensionにアプリケーションをセットする
#toolbar = DebugToolbarExtension(app)

# flask-mail拡張を登録する
mail = Mail(app)

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

with app.test_request_context():
    print(url_for("index"))

    print(url_for("hello-endpoint",name="world"))

    print(url_for("show_name",name="mingde",page="1"))


# ここで呼び出すとエラーとなる
# print(current_app)

# アプリケーションコンテキストを取得してスタックへpushする
ctx = app.app_context()
ctx.push()

# current_appにアクセスが可能になる
print(current_app.name)
# >> apps.minimalapp.app

# グローバルなテンポラリ領域に値を設定する
g.connection = "connection"
print(g.connection)
# >> connection

with app.test_request_context("/users?updated=true"):
    # trueが出力される
    print(request.args.get("updated"))

@app.route("/contact")
def contact():
    # レスポンスオブジェクトを取得する
    return render_template("contact.html")

@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        # form属性を使ってフォームの値を取得する
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]

        # 入力チェック
        is_valid = True
        if not username:
            flash("ユーザ名は必須です")
            is_valid = False

        if not email:
            flash("メールアドレスは必須です")
            is_valid = False

        try:
            validate_email(email)
        except EmailNotValidError:
            flash("メールアドレスの形式で入力してください")
            is_valid = False

        if not description:
            flash("問い合わせ内容は必須です")
            is_valid = False

        if not is_valid:
            return redirect(url_for("contact"))

        # メールを送る
        send_email(email,
            "問い合わせありがとうございました。",
            "contact_mail",
            username=username,
            description=description,
            )
         # 問い合わせ完了エンドポイントへリダイレクトする
        flash("問い合わせ内容はメールにて送信しました。問い合わせありがとうございます。")


        return redirect(url_for("contact_complete"))
    return render_template("contact_complete.html")

def send_email(to, subject, template, **kwargs):
    """メールを送信する関数"""
    msg = Message(subject, recipients=[to])
    msg.body = render_template(template + ".txt", **kwargs)
    msg.html = render_template(template + ".html", **kwargs)
    mail.send(msg)


