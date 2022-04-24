from gzip import READ
from django.contrib import admin
from coreapp.models import Restaurant, Driver, Customer

admin.site.register(Restaurant)
admin.site.register(Customer)
admin.site.register(Driver)

