from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render ,redirect,get_object_or_404
from .models import ProductReview,Product,Contact,Orders,Orderupdate,Product_Detail
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User 
from django.contrib import messages
from django.http import JsonResponse
import razorpay
from django.urls import reverse
from django.conf import settings
from math import ceil

import json

from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    allprods=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod= Product.objects.filter(category=cat)
        n=len(prod)
        nslides=n//4 + ceil((n/4) - (n//4))
        allprods.append([prod,range(1,nslides),nslides])
    context={"allprods":allprods}
    return render(request, 'shop/index.html',context)

def searchMatch(query,item):
    '''return true only if query matches the items'''
    if query in item.discription.lower() or query in item.product_name.lower() or  query in item.category.lower() :
        return True
    else:
        return False

def search(request):
    query=request.GET.get('search')
    allprods=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prodtemp= Product.objects.filter(category=cat)
        prod=[item for item in prodtemp if searchMatch(query,item)]
        n=len(prod)
        nslides=n//4 + ceil((n/4) - (n//4))
        if len(prod)!=0:
            allprods.append([prod,range(1,nslides),nslides])
    context={"allprods":allprods,'msg':''}
    if len(allprods)==0 or len(query)<4:
        context={'msg':'please enter relevent search query'}

    return render(request, 'shop/search.html',context)


def about(request):
    return render(request,"shop/about.html")

def contact(request):
    thankyou=False
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('Email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        thankyou=True
    return render(request,"shop/contact.html",{'thankyou':thankyou})

def tracker(request):
    if request.method=="POST":
        orderId=request.POST.get('orderId','')
        email=request.POST.get('Email','')
        try :
            order = Orders.objects.filter(order_id=orderId , email = email)
            if len(order)>0:
                update = Orderupdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})
                    response = json.dumps({'status':'success','updates':updates, 'itemsJson':order[0].items_json }, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"No items"}')
        except Exception as e:
            return HttpResponse("{'status':'Error'}")
    return render(request,"shop/tracker.html")


def productView(request,myid):
    # fatch the priduct using id
    prod_review= ProductReview.objects.filter(product_id=myid)
    product= Product.objects.filter(id=myid)
    prod_detail= Product_Detail.objects.get(product=product[0])
    
    context={'product':product[0],'prod_review':prod_review,'user':request.user,'prod_detail':prod_detail}
    print(product)
    print(prod_detail)
    return render(request,"shop/prodview.html",context)

def checkout(request):
    if request.method=="POST":
        
        items_json=request.POST.get('itemsJson','')
        name=request.POST.get('name',''),
        amount=request.POST.get('totalAmount','')
        email=request.POST.get('email','')
        address=request.POST.get('address1','')  + " " + request.POST.get('address2','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip_code=request.POST.get('zip_code','')
        phone=request.POST.get('phone','')
        paymentMethod=request.POST.get('paymentMethod')
        # razor=request.POST.get('razorpay1')
        
        print('hari')

        print(paymentMethod)
        if  paymentMethod=='cod':
            print('hari bol')
            order = Orders(items_json,name=name,email=email,city=city,state=state,address=address,zip_code=zip_code,phone=phone,amount=amount)
            order.save()
            Id= order.order_id
            update = Orderupdate(order_id = Id, update_desc = " the order has been placed",payment_mode="Cash on Delivary")
            print(Id)
            update.save()
            messages.success(request,f"Your order has been placed successfully your order id is {Id}")
            return redirect('/shop')

        else:
            
            client=razorpay.Client(auth=(settings.KEY,settings.SECRET))
            payment = client.order.create({'amount':int(amount)*100,'currency':'INR','payment_capture':1})
            print(payment)

            order = Orders(items_json,name=name,email=email,city=city,state=state,address=address,zip_code=zip_code,phone=phone,amount=amount,razor_pay_order_id=payment['id'])
            order.save()
            Id= order.order_id
            update = Orderupdate(order_id = Id, update_desc = " the order has been placed",payment_mode="PrePaid")
            print(Id)
            update.save()
        
            context={'cart':order,'payment':payment,'ID':Id}
            
        
            return render(request,"shop/payment.html",context)
            
    
    return render(request,"shop/checkout.html")



def success(request):
    payment_id=request.GET.get('razorpay_order_id')
    order=Orders.objects.get(razor_pay_order_id=payment_id)
    order_id=order.order_id
    order.is_paid=True
    order.save()
    messages.success(request,f'Payment successfull  Order_Id : {order_id} Payment_Id : {payment_id} ')
    return redirect("/shop")
    # return HttpResponse('payment Done')

def cancel(request):
    if request.method=="POST":
        
        order_id=request.POST.get('order_id')
        print('hari bol')
        print(order_id)
        order=get_object_or_404(Orders,order_id=order_id)
        orderupdate=Orderupdate.objects.get(order_id = order_id)
        orderupdate.delete()
        order.delete()
        messages.error(request,'Order Canceled!!')
        # return render(request,"shop/index.html")
        # return HttpResponseRedirect('/shop')
        response = json.dumps({'status':'success' }, default=str)
        return HttpResponse(response)
        return JsonResponse({'success':'true'}, safe=False)

        return redirect(reverse('ShopHome'))
    # return HttpResponse('payment Done')
    return render(request,"templates/shop/index.html")

def payment(request):
    return render(request,'shop/index.html')

def rate_product(request):
    if request.method =="POST":
        el_id=request.POST.get('el_id')
        val=request.POST.get('val')
        prod=Product.objects.get(id=el_id)
        user=request.user
        # review='harekrishna'
        try:
            prodRev = ProductReview.objects.get(product=prod,user=user)
        except ProductReview.DoesNotExist:
            prodRev=None
        if prodRev==None:
            print(el_id)
            print(val)
            
            obj = ProductReview(user=request.user,rating=val,product=prod)
            # obj.user=User
            # obj.rating=val
            obj.save()
            messages.success(request,'Product reated Successful')
            return JsonResponse({'success':'true', 'score': val}, safe=False)
        else:
            prodRev.rating=val
            # prodRev.review=review
            prodRev.save()
            messages.success(request,'Product reated Successful')
            return JsonResponse({'success':'true','score': val})
    return JsonResponse({'success':'false'})
    
def review_product(request):
    if request.method =="POST":
        prodId=request.POST.get('prodID')
        val=request.POST.get('review')
        prod=Product.objects.get(id=prodId)
        user=request.user
        print(prodId)
        print(val)
        print(prod)
        # review='harekrishna'
        try:
            prodRev = ProductReview.objects.get(product=prod,user=user)
        except ProductReview.DoesNotExist:
            prodRev=None
        if prodRev==None:
            print(prodId)
            print(val)
            
            obj = ProductReview(user=request.user,review=val,product=prod)
            # obj.user=User
            # obj.rating=val
            obj.save()
            messages.success(request,'Product Review Successful')
            return JsonResponse({'success':'true', 'score': val}, safe=False)
        else:
            prodRev.review=val
            # prodRev.review=review
            prodRev.save()
            messages.success(request,'Product Review Successful')
            return JsonResponse({'success':'true','score': val})
    return JsonResponse({'success':'false'})
    




     



def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['EMAIL']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if User.objects.filter(username=username).exists():
            # Handle username already exists error
            messages.error(request,'user already exist!!')
            return redirect('/shop')
        
        elif len(username)>10:
            messages.error(request,"Usernamemust be under 10 character")
            return redirect('/shop')
         
        elif  not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('/shop')
        elif (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('/shop')

        else:
        # Create the user
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name= fname
            myuser.last_name= lname
            myuser.save()
            messages.success(request, " Your AvantiKart account has been successfully created")
            return redirect('/shop')

    else:
        return HttpResponse("404 - Not found")



def handlelogin(request): 
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
    
        user= authenticate(username = loginusername, password=loginpassword)

        if user is not None:
            login(request , user)
            messages.success(request, "login Successfull")
            return redirect("/shop")
        else:
            messages.error(request,"wrong credentials")
            return redirect("/shop")

    return HttpResponse("404 - not found ")
def handlelogout(request): 
    logout(request)
    messages.success(request, "Logout successful")
    return redirect("/shop")