from django.db import models

# Create your models here.
class Product_detail(models.Model):
    p_id=models.AutoField(primary_key=True)
    p_name=models.CharField(max_length=150)
    p_price=models.IntegerField()
    p_type=models.CharField(max_length=50)
    p_category=models.CharField(max_length=50,default='No Subcategory')
    p_subcategory=models.CharField(max_length=50)
    p_quantity=models.IntegerField(max_length=50)
    p_desc=models.CharField(max_length=750)
    p_warranty=models.CharField(max_length=150)
    publish_date=models.DateField()
    p_img=models.ImageField( upload_to='product_img/', height_field=None, width_field=None, default='product_img/noProductImage.jpg')

    def __str__(self):
        return (f"{self.p_name}-{self.p_category}({self.p_type})")

# news table
class News(models.Model):
    News_id=models.AutoField(primary_key=True)
    News_type=models.CharField(max_length=150)
    P_type=models.CharField(max_length=50)
    p_desc=models.CharField(max_length=750)
    Date=models.DateField()
   

    def __str__(self):
        return (f"{self.Date}-{self.News_type}")

