
root_run = """
import os
from project import create_app

if __name__ == "__main__":
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config", "development.py")
    app = create_app(config_file)
    app.run(host="0.0.0.0", debug=True)
"""

root_init = """
import os
from flask import Flask

def create_app(config_file):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    from project.core.apps.index import index
    app.register_blueprint(index)
    return app
"""



blueprint_init = lambda app_name: """
### Standard Library Imports ###

################################

### 3rd Party Imports ###
from flask import Blueprint
################################

### Local Imports ###

################################


{app_name} = Blueprint('{app_name}', __name__)

from .views import *
""".format(app_name=app_name)


celery_worker = """

from celery import Celery

celery_app = Celery("project.core.celery.celery_worker", broker='redis://localhost:6379/0', include=["project.core.celery.tasks"])
"""

celery_runner = """
from project.core.apps.celery.celery_worker import celery_app

if __name__ == "__main__":
    celery_app.run()


"""

celery_task = """
from .celery_worker import app

##SAMPLE TASK
@app.task
def send_message(to, subject, template):
    message = MIMEMultipart()
    message["From"] = "your username"
    message["To"] = to
    message["Subject"] = subject
    message.attach(MIMEText(template, "html"))
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    # server.starttls()
    server.login("your username", "your password")
    server.sendmail("sender email", to, message.as_string())
    server.close()
"""

views = """
from flask import url_for, render_template
from project.core.apps.index import index


@index.route("/")
def index_page():
    return render_template("index.html")
"""


helper_functions = """

### 3rd Party Imports ###
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.security import check_password_hash, generate_password_hash
from flask import url_for, redirect, render_template, flash, current_app
from itsdangerous import URLSafeTimedSerializer
from flask.ext.login import current_user
################################


### Local Imports ###
from config.developement_config  import SECRET_KEY, SECURITY_PASSWORD_SALT, MAIL_USERNAME, MAIL_PASSWORD, MAIL_SERVER
################################

def check_password(password, password_hash):
    return check_password_hash(password_hash, password)

def generate_password(password):
    return generate_password_hash(password)

def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(SECRET_KEY)
    return serializer.dumps(email, salt=SECURITY_PASSWORD_SALT)

def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(SECRET_KEY)
    try:
        email = serializer.loads(
            token,
            salt=SECURITY_PASSWORD_SALT,
            max_age=expiration
        )
        return email
    except:
        return False

def generate_token_and_html(email, route=None, template=None):
    token = generate_confirmation_token(email)
    url = url_for(route, token=token, _external=True)
    html = render_template(template, url=url)
    return html


def check_confirmation(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            if not current_user.confirmed:
                flash("Please confirm your account")
                return redirect(url_for("user.unconfirmed"))
            else:
                return func(*args, **kwargs)
        except:
            return redirect(url_for("user.login"))
    return wrapper

"""


html_format = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>This is your index page</h1>
</body>
</html>
"""