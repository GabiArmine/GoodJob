from django.contrib import admin
from register.models import Category, Employees, Employer



admin.site.register(Category)
admin.site.register(Employees)
admin.site.register(Employer)
print(Category.objects.all())
