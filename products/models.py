from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=64,unique=True) #CharField, TextField это тип данных, в скобках - доп условия типо unique, blank (если true то поле может быть пустым)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'ProductCategories'

class Products(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='products_images',blank=True) #upload_to - папка куда будут выгружаться фотографии
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=64, blank=True)
    price = models.DecimalField(max_digits=8,decimal_places=2,default=0) #Тип данных для денег, 2 знака после запятой, максимум цифр в целой части 8, по умолчанию поле равно 0
    quantity = models.PositiveIntegerField(default=0) #Положительное целое число
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE) #Внешний ключ ссылающийся на таблицу ProductCategory, при удалении Категории товары также удалятся

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Products"

