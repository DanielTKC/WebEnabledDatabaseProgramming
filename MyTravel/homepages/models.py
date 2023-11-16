from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Contact_Information(models.Model):
            contact_phone = models.CharField(max_length=10)
        
            def __str__(self):
                phone = '(%s) %s-%s' %(self.contact_phone[0:3],self.contact_phone[3:6],self.contact_phone[6:10])
                return phone 
class State(models.Model) :
            state_abbrev = models.CharField(max_length=2)
            state_description = models.CharField(max_length=30)
        
            def __str__(self):
                return (self.state_description)  
class Skill(models.Model) :
            description = models.CharField(max_length=30)
        
            def __str__(self):
                return (self.description)
        
class Employee(models.Model):
            TITLE = (
                ('Ms.', 'MISS'),
                ('Mr.', 'MR.'),
                ('Mrs.', 'MRS.'),
                ('Miss', 'Miss'),
                ('Mx.', 'MX.'),
            )
        
            emp_first = models.CharField(max_length=20)
            emp_last = models.CharField(max_length=20)
            emp_title = models.CharField(max_length=4, choices=TITLE, null=True, blank=True)
            emp_state = models.ForeignKey('State', null=True, blank=True, on_delete=models.SET_NULL)
            contact_information = models.OneToOneField(Contact_Information, on_delete=models.CASCADE)
            
            #Add this line
            emp_skills = models.ManyToManyField('Skill', through='Skill_Level')
        
            def __str__(self):
                return (self.emp_first + " " + self.emp_last)
        
        #Add this class
class Skill_Level(models.Model):
            employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
            skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
            skill_rating = models.PositiveIntegerField(default=3, validators=[MinValueValidator(0), MaxValueValidator(5)])
        
            def __str__(self):
                return '%s %s %s %i' %(self.employee.emp_first,self.employee.emp_last,self.skill.description,self.skill_rating)