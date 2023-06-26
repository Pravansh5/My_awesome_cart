from django.contrib import admin
from .models import ProductImage, ProductReview,Product,Contact,Orders,Orderupdate
# Register your models here.
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(Orderupdate)
admin.site.register(ProductReview)
admin.site.register(ProductImage)

