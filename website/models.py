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
        return (f"{self.p_name}-{self.p_category}({self.p_type})") 

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
   

    def __str__(self):
        return (f"{self.retrailer_name}-{self.retrailer_phone}")

