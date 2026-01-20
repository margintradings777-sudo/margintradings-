from django.db import models

class UserDetail(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=128)
    Phone = models.CharField(max_length=20)
    Pan = models.CharField(max_length=10, unique=True)
    Pan_card_Image = models.ImageField(upload_to='pan_cards/')
    Account_No = models.CharField(max_length=50)
    IFSC_code = models.CharField(max_length=20)
    Cancel_cheque_or_bank_statement = models.ImageField(upload_to='bank_documents/')
    Account_Balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.Name

        
# Create your models here.
class Deposit(models.Model):
   user = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name='deposits')
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