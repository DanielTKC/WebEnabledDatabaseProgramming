from django.db import models

class Contact_Information(models.Model):
            contact_phone = models.CharField(max_length=10)
        
            def __str__(self):
                phone = '(%s) %s-%s' %(self.contact_phone[0:3],self.contact_phone[3:6],self.contact_phone[6:10])
                return phone        
