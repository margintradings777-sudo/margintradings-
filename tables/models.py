from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class UserDetail(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=255)
    Account_Balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    Phone = models.CharField(max_length=15, blank=True, null=True)
    PAN_No = models.CharField(max_length=10, blank=True, null=True)
    PAN_Image = models.ImageField(upload_to="kyc/pan/", blank=True, null=True)

    Account_No = models.CharField(max_length=30, blank=True, null=True)
    IFSC_Code = models.CharField(max_length=20, blank=True, null=True)

    Bank_Document = models.FileField(upload_to="kyc/bank_docs/", blank=True, null=True)

    def __str__(self):
    return self.Email or self.Name or "UserDetail"

        
# Create your models here.
class Deposit(models.Model):
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="deposits")
   BankName = models.CharField(max_length=100)
   QR = models.ImageField(upload_to='QR_images/')


def __str__(self):
        return self.BankName

class withdrawal(models.Model):
    user = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name='withdrawals')
    Name=models.CharField(max_length=200,blank=True,null=True)
    Amount=models.CharField(max_length=200,blank=True,null=True)
    Status=models.CharField(max_length=200,blank=True,null=True)
    

    # def __str__(self):
    #     return self.Amount


class DepositAccountDetails(models.Model):
    BankName = models.CharField(max_length=200)
    HolderName = models.CharField(max_length=200)
    AccountNumber = models.CharField(max_length=50)
    IFSC = models.CharField(max_length=20)
    QRImage = models.ImageField(upload_to='QR_images/')

    def __str__(self):
        return self.BankName
