from flask import Flask, url_for, render_template, redirect, request, session, flash
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mbnbvjbhvgvgvgv'


@app.route('/', methods=['POST', 'GET'])
def root():
    return redirect('/home',)


@app.route('/home', methods=['GET', 'POST'])
def home():
    
   
    return render_template('home.html')




@app.route('/pin', methods=['GET', 'POST'])
def pin():
    pin = request.form.get('pin')
    if pin is None:
        pin = 0
        return pin
    if pin is 0:
        return redirect(url_for('home'))

    else:
        res = requests.get(f'https://api.postalpincode.in/pincode/{pin}').json()
        sts = res[0]['Status']
        if sts == 'Success':
            loc = res[0]['PostOffice'][0]['Name']
        else:

           

            return redirect(url_for('home'))

    return render_template('page2.html',loc=loc)


@app.route('/form', methods=['POST', 'GET'])
def form():

    FLAVOUR = {"1": "Strawberry", "2": "Vanilla", "3": "Chocolate"}
    FLAVOUR_PRICE = {'1': 120, '2': 90, '3': 110}
    TOPPING = {"1": "Sugar crystals", "2": "M&M's", "3": "Oreo",
               "4": "Brownies", "5": "Chocolate Syrup", "6": "Chocolate Chips"}
    TOPPING_PRICE = {'1': 0, '2': 35, '3': 25, '4': 25, '5': 25, '6': 30}
    BILL = 0
    f = request.form.get('FLAVOURS')
    s = request.form.get('SIZE')
    t = request.form.getlist('ckb')

    if s == None:
        s = 1

    f_price = FLAVOUR_PRICE.get(f)
    f = FLAVOUR.get(f)
    f_price = f_price*int(s)

    topping = []
    topping_price = []
    for i in t:
        topping.append(TOPPING[i])  # LIST OF TOPPING

    for j in t:
        topping_price.append(TOPPING_PRICE[j])  # list of Topping price

    total_toppings_price = 0
    for k in range(0, len(topping_price)):  # SUM OF TOPPING PRICE
        total_toppings_price = total_toppings_price + topping_price[k]

    # convert topping price list to int
    topping_price = [str(x) for x in topping_price]

    temp = ''
    for i in range(len(topping)):
        temp += " " + topping[i] + " (" + topping_price[i]+") "

    BILL = BILL+total_toppings_price+f_price

    return render_template('page3.html', BILL=BILL, f=f, s=s, t=temp)


app.run(debug=True)
