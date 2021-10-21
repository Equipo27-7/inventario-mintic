from flask import Flask,redirect,url_for,render_template,request
from flask_login import LoginManager
from forms import SinginForm

app=Flask(__name__)
app.config['SECRET_KEY'] = '2e627a7bcf05fa13bf1a23a44c3a38bf8f21f9b2'

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return render_template('index.html')
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)