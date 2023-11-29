from django.db import models

class State(models.Model):
    abbrev = models.CharField(max_length=2, unique=True, null=False)
    state_name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.state_name

class Customer(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    address = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=30, null=False)
    state = models.OneToOneField(State, on_delete=models.CASCADE)
    zipcode = models.CharField(max_length=9, null=False)
    phone = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return (self.full_name) 
    
    @property
    def full_name(self):
      return '%s %s' % (self.first_name, self.last_name)  

class Order(models.Model):
    description = models.CharField(max_length=20, null=False)
    cost = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    order_date = models.DateTimeField(null=False)

    def __str__(self):
        return str(self.id)

class CustomerOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return (self.customer_order)
    
    @property
    def customer_order(self):
        return '%s - %s' %(self.customer, self.order)


# Create your models here.
