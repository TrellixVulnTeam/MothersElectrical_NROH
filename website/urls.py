from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',views.index,name='windex'),
    path ('ContactUs/',views.contactus,name="wcontactUs"),
    path ('AboutUs/',views.aboutus,name="wAboutUs"),
    path ('Products/<str:Category>/',views.productCategory,name="subCategory"),
    path ('Products/<str:category>/<str:subCategory>/',views.product,name="wproduct"),
    path ('Products/<str:category>/<str:subCategory>/<str:company>/',views.productViewByCompany,name="wproduct"),
    path ('Retrailers/',views.retailers,name="wretrailers"),
    path ('AllProducts/<str:type>/',views.AllProduct,name="wAllProduct"),
    path ('Logout/',views.handleLogout,name="wlogout"),
    path('ProductDetail/<int:id>/',views.productDetail,name="wProductDetail"),
    path('Checkout/',views.checkout,name="wCheckout"),
    path('PlacedOrder/',views.placedOrder,name='wPlacedOrder')
]
