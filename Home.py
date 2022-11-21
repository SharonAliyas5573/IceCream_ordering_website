from flask import Flask ,url_for,render_template,request,redirect,flash

app = Flask(__name__)


@app.route('/',methods =['GET','POST'])
def home():
    return render_template('home.html')
@app.route('/form',methods =['POST','GET'])
def form():
    flavour = request.form.get('FLAVOURS')
    size = request.form.get('SCOPS')
    

    return render_template('page2.html',size=size,flavour=flavour)


app.run(debug=True)