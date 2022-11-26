from flask import Flask ,url_for,render_template,redirect,request



app = Flask(__name__)


@app.route('/',methods =['GET','POST'])
def home():
    return render_template('home.html')
@app.route('/order',methods =['GET','POST'])
def order():
    return render_template('page2.html')

@app.route('/form',methods =['POST','GET'])
def form():

    FLAVOUR ={"1":"Strawberry","2":"Vanilla","3":"Chocolate"}
    FLAVOUR_PRICE ={'1':120,'2':90,'3':110}
    TOPPING ={"1":"Sugar crystals","2":"M&M's","3":"Oreo","4":"Brownies","5":"Chocolate Syrup","6":"Chocolate Chips"}
    TOPPING_PRICE ={'1':'0','2':'35','3':'25','4':'25','5':'25','6':'30'}
    BILL=0
    f = request.form.get('FLAVOURS')
    s = request.form.get('SIZE')
    t = request.form.getlist('ckb')
    
    if s==None:
        s=1
    
    
    f_price=FLAVOUR_PRICE.get(f)
    f=FLAVOUR.get(f)
    f_price=f_price*int(s)
   

    
    
    topping=[]
    topping_price=[]
    for i in t:
        topping.append(TOPPING[i])

  
    for j in t:
        topping_price.append(TOPPING_PRICE[j])

    for i in range(0, len(topping_price)):
        topping_price[i] = int(topping_price[i]) 

    total_toppings_price=0
    for k in range(0,len(topping_price)):
        total_toppings_price= total_toppings_price +topping_price[k]

        

    Topping = ', '.join(topping)
   
    BILL= BILL+total_toppings_price+f_price

    

        
   
    return render_template('page3.html',BILL=BILL,f=f,Topping=Topping,s=s)


app.run(debug=True)