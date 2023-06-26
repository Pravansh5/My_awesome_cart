from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=30)
    discription=models.CharField(max_length=300)
    category=models.CharField(max_length=50,default='')
    subcategory=models.CharField(max_length=30,default="")
    price=models.IntegerField(default=0)
    pub_date=models.DateField()
    image=models.ImageField(upload_to='shop/images',default="")

    def __str__(self):
        return self.product_name +" " +  self.category

class ProductImage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    img=models.ImageField(upload_to='shop/images',default="")

    def __str__(self):
        return self.product.product_name
    

class ProductReview(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True ,related_name="reviews")
    review = models.TextField(blank=True,default="",null=True)
    rating=models.IntegerField(default=0,
                validators=[
                    MaxValueValidator(5),
                    MinValueValidator(0),
                ])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural="Product Review"

    def __str__(self):
        return self.product.product_name
    
    def get_rating(self):
        return self.rating

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=30,default="")
    phone=models.CharField(max_length=30,default="")
    desc=models.CharField(max_length=500,default="")
    

    def __str__(self):
        return self.name

class Orders(models.Model):
    
    items_json=models.CharField(max_length=5000)
    name=models.CharField(max_length=90)
    amount=models.IntegerField(default=0)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)
    phone=models.CharField(max_length=111,default="")
    order_id= models.AutoField(primary_key=True)
    is_paid=models.BooleanField(default=False)
    razor_pay_order_id=models.CharField(max_length=100,null=True,blank=True)
    razor_pay_payment_id=models.CharField(max_length=100,null=True,blank=True)
    razor_pay_payment_signature=models.CharField(max_length=100,null=True,blank=True)

class Orderupdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default=0)
    update_desc=models.CharField(max_length=50000)
    timestamp=models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.update_desc[0:7] + "...."