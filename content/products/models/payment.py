from accounts.models import Costumer
from django.db import models
from orders.models import Order

class Payment(models.Model):
    '''
    Key payment information, including key, payment type, and... 
    '''
    PAYMENT_CHOICE = [
        ('P', 'Pix'),
        ('T', 'Transferência bancária'),
        ('C', 'Cartão de crédito'),
    ]
    
    customer = models.ForeignKey(Costumer, on_delete=models.CASCADE, related_name='payment')
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()
    payment_method = models.CharField(choices=PAYMENT_CHOICE, max_length=32, blank=True)
    transaction_id = models.AutoField(primary_key=True)
    
    class Meta:    
        ordering = ['-payment_date']
        verbose_name = 'payment'
        verbose_name_plural = 'payments'
        
    def __str__(self):
        return self.amount