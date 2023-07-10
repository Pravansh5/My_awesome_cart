from django.contrib import admin
from .models import ProductImage, ProductReview,Product,Contact,Orders,Orderupdate,Product_Detail
# Register your models here.
from django.contrib import admindocs

class ShopAdminArea(admin.AdminSite):
    site_header ='Shop Admin Area'
    

admin.site.register(Product)
admin.site.register(Product_Detail)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(Orderupdate)
admin.site.register(ProductReview)
admin.site.register(ProductImage)

