from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=20,verbose_name='书籍名称')
    author=models.CharField(max_length=30,verbose_name='作者')
    price=models.FloatField(verbose_name='定价',default=0.0)
    publish_date=models.DateTimeField(verbose_name='出版时间',null=True,blank=True)
    category=models.CharField(verbose_name='书籍分类',max_length=10,default='未分类')
    create_datetime=models.DateTimeField(auto_now_add=True,verbose_name='添加日期')
    def __str__(self):
        return self.name
class Image(models.Model):
    name=models.CharField(max_length=50,verbose_name='图片名称')
    description=models.TextField(verbose_name='图片描述',default='')
    img=models.ImageField(upload_to='img/%Y/%m/%d',verbose_name='图片')
    book=models.ForeignKey(Book,on_delete=models.CASCADE,verbose_name='所属书籍')
    def __str__(self):
        return self.name