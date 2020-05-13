from django.contrib import admin
from management.models import Book,Image
# Register your models here.
@admin.register(Book)
class admin(admin.ModelAdmin):
	pass