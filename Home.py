from flask import Flask ,url_for,render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('page2.html')

app.run(debug=True)