from django.contrib import admin
from .models import Customer, Order
# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
     list_display = ('name','email','phone','address','created_at')
     list_filter = ("name",)
     search_fields = ("name",)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer','product','quantity','price','order_date','order_status')
    list_filter = ("customer",)
    search_fields = ("customer",)