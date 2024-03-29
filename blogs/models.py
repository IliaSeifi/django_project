from django.db import models
from django.utils.text import slugify
# Create your models here.

class Karbaran(models.Model):
    name = models.CharField(max_length=50)
    family = models.CharField(max_length=50)
    age = models.IntegerField()
    is_active = models.BooleanField()

class ProductCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name= 'عنوان')
    url_title= models.CharField(max_length=300,verbose_name = 'عنوان در url')

    def __str__(self):
        return self.title


class Meta:
    verbse_name = 'دسته بندی'
    verbse_name_plural = 'دسته بندی ها'

class ProductInformation(models.Model):
    color = models.CharField(max_length=100, verbose_name= 'رنگ')
    size = models.CharField(max_length=100, verbose_name= 'سایز')

    def __str__(self):
        return self.color
    class Meta:
        verbose_name = 'اطلاعات تکمیلی'
        verbose_name_plural = ' لیست اطلاعات تکمیلی'

class ProductTag(models.Model):
    tag = models.CharField(max_length= 200, verbose_name='عنوان تگ')
    def __str__(self):
        return self.tag
    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = ' تگهای محصولات'
class Product(models.Model):
    category= models.ForeignKey(ProductCategory,on_delete=models.CASCADE,null=True, verbose_name='دسته بندی')
    product_info = models.OneToOneField(ProductInformation, on_delete=models.CASCADE, null = True, blank= True, verbose_name='اطلاعات تکمیلی')
    product_tag = models.ManyToManyField(ProductTag, verbose_name= 'تگ محصول')

    title = models.CharField(max_length=100,verbose_name='عنوان محصول')
    price = models.IntegerField(verbose_name='قیمت')
    description = models.CharField(max_length=500,verbose_name="توضیحات")
    is_active = models.BooleanField(verbose_name='فعال/غیرفعال')

    slug = models.SlugField(default='', null=False, db_index=True ,unique=True,verbose_name='عنوان در url ')


    def save (self, *args, **kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return f'{self.title}---{self.price}'

class Meta:
     verbse_name= 'محصول'
     verbse_name_plural = 'محصولات'
