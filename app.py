import flask
from flask import jsonify, Flask, render_template, redirect, url_for, request, session
import manage_users as mu
import manage_buckets as mb
import Aira as aira
import json

# ------------------------------------- FLASK ROUTES --------------------------------------- #

app = Flask(__name__)
app.secret_key = 'secret_key'

# Decorator to check if the user is logged in
def login_required(f):
    def wrap(*args, **kwargs):
        if 'username' not in session:
            return render_template('error.html', message="You must be logged in to view this page"), 401
        return f(*args, **kwargs)
    wrap.__name__ = f.__name__
    return wrap

@app.route('/', methods=['GET', 'POST'])
def start():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_route():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    logged_in = mu.login(username=username, password=password)

    if logged_in == True:
        session['username'] = username
        return redirect(url_for('home'))
    else:
        return jsonify({"error": logged_in}), 401
    
@app.route('/signup', methods=['POST'])
def signup_route():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    mailid = data.get('email')

    signed_up = mu.signup(username=username, email=mailid, password=password)
    if signed_up == True:
        return jsonify({"status": signed_up}), 200
    else:
        return jsonify({"error": signed_up}), 401

@app.route('/validate', methods=['POST'])
def validate_route():
    data = request.json
    username = data.get('username')
    validation_code = data.get('validation_code')
    
    signed_up = mu.confirm_signup(username, validation_code)
    if signed_up == True:
        return redirect(url_for('start'))
    else:
        return jsonify({"error": signed_up}), 401
    
@app.route('/resend', methods=['POST'])
def resend_route(username):
    mu.resend_verification_code(username)

@app.route('/home')
@login_required
def home():
    username = session.get('username', None)
    return render_template('home.html', username=username)

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@app.route('/currentprofile')
@login_required
def currentprofile():
    return render_template('currentprofile.html')

@app.route('/about')
@login_required
def about():
    return render_template('about.html')

@app.route('/uploadinfo', methods=['POST'])
def uploadinfo():
    jsondata = request.json
    username = session.get('username', None)

    if isinstance(jsondata, str):
        jsondata = json.loads(jsondata)
    
    jsondata = aira.useai(jsondata)
    uploaded = mb.uploaddata(json.dumps(jsondata), username, mb.s3)
    t1_done = mb.uploadtemplate1(jsondata, username, mb.s3)
    t2_done = mb.uploadtemplate2(jsondata, username, mb.s3)
    t3_done = mb.uploadtemplate3(jsondata, username, mb.s3)

    if uploaded == True and t1_done == True and t2_done == True and t3_done == True:
        return "Information updated successfully. You can proceed to download your resume"
    elif uploaded != True:
        return uploaded
    
@app.route('/readinfo', methods=['POST'])
def readinfo():
    username = session.get('username', None)
    jsondata = mb.readdata(username=username, s3=mb.s3)
    jsondata = jsonify(jsondata)
    return jsondata

@app.route('/redirect', methods=['POST'])
def openpage():
    print('/redirect route triggered')
    page = request.json
    page = page.get('page')
    return redirect(url_for(page))

if __name__ == '__main__':
    app.run(debug=True)
