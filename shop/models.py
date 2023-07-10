from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=100)
    discription=models.CharField(max_length=1000)
    category=models.CharField(max_length=50,default='')
    subcategory=models.CharField(max_length=30,default="")
    price=models.IntegerField(default=0)
    pub_date=models.DateField()
    image=models.ImageField(upload_to='shop/images',default="")

    def __str__(self):
        return self.product_name +" " +  self.category
class Product_Detail(models.Model):
    Package_Dimensions=models.CharField(max_length=40)
    Date_First_Available=models.CharField(max_length=40)
    Manufacturer=models.CharField(max_length=40)
    ASIN =models.CharField(max_length=40)
    Item_part_number=models.CharField(max_length=40)
    Country_of_Origin=models.CharField(max_length=40)
    Department=models.CharField(max_length=40)
    Item_Weight=models.CharField(max_length=40)
    Net_Quantity=models.CharField(max_length=40)
    Generic_Name=models.CharField(max_length=40)
    Best_Sellers_Rank=models.CharField(max_length=40)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product.product_name + self.Generic_Name


class ProductImage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    img=models.ImageField(upload_to='shop/images',default="")

    def __str__(self):
        return str(self.product)
    

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
        return str(self.product)
    
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
    date=models.DateTimeField(auto_now=True)
    order_id= models.AutoField(primary_key=True)
    is_paid=models.BooleanField(default=False)
    razor_pay_order_id=models.CharField(max_length=100,null=True,blank=True)
    razor_pay_payment_id=models.CharField(max_length=100,null=True,blank=True)
    razor_pay_payment_signature=models.CharField(max_length=100,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

class Orderupdate(models.Model):
    
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default=0,null=True)
    payment_mode=models.CharField(max_length=100,null=True)
    update_desc=models.CharField(max_length=50000)
    timestamp=models.DateField(auto_now_add=True)
    

    def __str__(self):
        return str(self.order_id) +  self.update_desc[0:7] + "...."