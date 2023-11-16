from django.contrib import admin
from .models import Contact_Information, Employee, State, Skill, Skill_Level

admin.site.register(State)
admin.site.register(Skill)
admin.site.register(Contact_Information)
admin.site.register(Employee)  
admin.site.register(Skill_Level)

# Register your models here.
