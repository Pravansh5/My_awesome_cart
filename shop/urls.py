from django.urls import path
from .  import views 
urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("product/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    # path("handlerequest/", views.handlerequest, name="HandleRequest"),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handlelogin, name="handlelogin"),
    path('logout', views.handlelogout, name="handlelogout"),
    path('rate_product/', views.rate_product, name="rate_product"),
    path('review_product/', views.review_product, name="review_product"),
    path('checkout/success/',views.success,name="success"),
    # path('payment/',views.payment,name="payment")

]
