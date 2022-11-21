from flask import Flask ,url_for,render_template,request,redirect,flash

app = Flask(__name__)


@app.route('/',methods =['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/options',methods =['GET','POST'])

def options():
    value = request.form.get('FLAVOURS')
    print(value)
    return render_template('page2.html')

app.run(debug=True)