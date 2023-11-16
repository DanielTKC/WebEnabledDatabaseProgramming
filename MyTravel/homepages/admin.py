from django.contrib import admin
from .models import Contact_Information, Employee, State, Skill

admin.site.register(State)
admin.site.register(Skill)
admin.site.register(Contact_Information)
admin.site.register(Employee)  

# Register your models here.
