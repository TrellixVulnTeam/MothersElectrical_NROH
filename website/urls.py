from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',views.index,name='windex'),
    path ('ContactUs/',views.contactus,name="wcontactUs"),
    path ('AboutUs/',views.aboutus,name="wAboutUs"),
    path ('Products/<str:type>/',views.Type,name="wType"),
    path ('Products/<str:category>/<str:company>/',views.product,name="wproduct"),
    path ('Retrailers/',views.retailers,name="wretrailers"),
    path ('AllProducts/<str:type>/',views.AllProduct,name="wAllProduct"),
    path ('Logout/',views.handleLogout,name="wlogout"),
    path('ProductDetail/<int:id>/',views.productDetail,name="wProductDetail"),
    path('Checkout/',views.checkout,name="wCheckout"),
    path('PlacedOrder/',views.placedOrder,name='wPlacedOrder')
]
