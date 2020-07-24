from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',views.index,name='windex'),
    path ('ContactUs/',views.contactus,name="wcontactUs"),
    path ('AboutUs/',views.aboutus,name="wAboutUs"),
    path ('Products/',views.product,name="wproduct"),
    path ('Retrailers/',views.retailers,name="retrailers")
]
