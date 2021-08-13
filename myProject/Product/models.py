from django.db import models

# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=100,blank=False)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)   
    weight=models.IntegerField()
    price=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # class Meta:
    #     app_label = 'product_data'
    def __str__(self):
        return (self.name)
