from django.db import models

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

class Employee(models.Model):
            emp_first = models.CharField(max_length=20)
            emp_last = models.CharField(max_length=20)
            emp_state = models.ForeignKey('State', null=True, blank=True, on_delete=models.SET_NULL)
            contact_information = models.OneToOneField(Contact_Information, on_delete=models.CASCADE)
            
            def __str__(self): 
                    return (self.emp_first + " " + self.emp_last)    

