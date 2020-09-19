from django.db import models

# Create your models here.
class Product_detail(models.Model):
    p_id=models.AutoField(primary_key=True)
    p_name=models.CharField(max_length=150)
    p_price=models.IntegerField()
    p_type=models.CharField(max_length=50)
    p_category=models.CharField(max_length=50)
    p_subcategory=models.CharField(max_length=50,default='No Subcategory')
    p_company=models.CharField(max_length=200,default="havells")
    p_quantity=models.IntegerField()
    p_desc=models.CharField(max_length=750)
    p_warranty=models.CharField(max_length=150)
    publish_date=models.DateField()
    p_img=models.ImageField( upload_to='product_img/', height_field=None, width_field=None, default='product_img/noProductImage.png')

    def __str__(self):
        return (f"{self.p_name}-{self.p_category}-{self.p_company}({self.p_type})") 

# news table
class News(models.Model):
    News_id=models.AutoField(primary_key=True)
    News_type=models.CharField(max_length=150)
    News_desc=models.CharField(max_length=750)
    Date=models.DateField()
   

    def __str__(self):
        return (f"{self.Date}-{self.News_type}")

class Retrailer_Detail(models.Model):
    retrailer_id=models.AutoField(primary_key=True)
    retrailer_name=models.CharField(max_length=150)
    retrailer_phone=models.CharField(max_length=20)
    retrailer_address=models.CharField(max_length=150)
    Date=models.DateField()
   
class clientMoblie(models.Model):
    clientMoblieId=models.AutoField(primary_key=True)
    clientMoblieNumber=models.CharField(max_length=15)
    def __str__(self):
        return (f"{self.clientMoblieNumber}")

class OrderDetail(models.Model):
    order_id=models.AutoField(primary_key=True)
    order_Items=models.CharField(max_length=10000)
    order_Total=models.CharField(max_length=50)
    c_Name=models.CharField(max_length=50)
    c_Moblie=models.CharField(max_length=50)
    c_AltMoblie=models.CharField(max_length=50)
    c_Address=models.CharField(max_length=50)
    c_Address2=models.CharField(max_length=50)
    c_Email=models.CharField(max_length=50)
    c_State=models.CharField(max_length=50)
    c_City=models.CharField(max_length=50)
    c_Zip=models.CharField(max_length=50)
    Date=models.DateField()
    
    def __str__(self):
        return (f"{self.order_id}-{self.c_Name}-{self.order_Total}")
    

    
    
    

