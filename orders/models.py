from django.db import models
from accounts.models import user
from .date_convertor import gregorian_to_shamsi

class order(models.Model):
    user = models.ForeignKey(user,on_delete=models.CASCADE)
    #the gain has calculated in toman_cost
    toman_cost = models.IntegerField()
    currency_cost = models.FloatField()
    currency_rate = models.IntegerField()
    currency_type = models.CharField(max_length=15,default='dollor')
    paid = models.BooleanField(default=False)
    transaction_no = models.CharField(max_length=30, null=True)
    status = models.CharField(max_length=10, choices=(('0', 'waiting for payment'), ('1', 'pending'), ('2', 'done'), ('-1', 'unsuccess payment')), default='0')
    #convert the dictionary of info to str and save them here
    information = models.TextField()
    #order_type shows which exam or site
    order_type = models.CharField(max_length=20)
    last_update = models.DateTimeField(auto_now=True)
    attach_file = models.FileField(upload_to='orders',null=True, blank=True)

    def shamsi_last_update(self):
        return gregorian_to_shamsi(self.last_update)

    def status_word(self):
        if self.status == '0':
            return 'در انتظار پرداخت'
        if self.status == '1':
            return 'در حال بررسی'
        if self.status == '2':
            return 'انجام شده'
        if self.status == '-1':
            return 'پرداخت ناموفق'

    def status_color(self):
        if self.status == '0':
            return 'table-warning'
        if self.status == '1':
            return 'table-info'
        if self.status == '2':
            return 'table-success'
        if self.status == '-1':
            return 'table-danger'
