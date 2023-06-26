keyid="rzp_test_xv4WlbBrgONmBf"
keySecret="hlidterSNr98bAeYzVk3O4fR"
import razorpay

client = razorpay.Client(auth=("keyid", "keySecret"))

data = { "amount": 500*100, 
         "currency": "INR",
        #  "receipt": "nitai108",
          "notes":{
              'name':'Nitai',
              "payment_for":'2k23 Rath Yatra'
          } }
payment = client.order.create(data=data)
print(payment)