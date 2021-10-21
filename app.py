from flask import Flask,redirect,url_for,render_template,request
from flask_login import LoginManager
from forms import SinginForm

app=Flask(__name__)
app.config['SECRET_KEY'] = '2e627a7bcf05fa13bf1a23a44c3a38bf8f21f9b2'

login_manager = LoginManager(app)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return render_template('index.html')
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

    next = request.args.get('next', None)
    if next:
        return redirect(next)
    return redirect(url_for('index'))

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)