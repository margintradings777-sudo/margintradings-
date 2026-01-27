from django.contrib import admin
from .models import UserDetail, Deposit, withdrawal

@admin.register(UserDetail)
class UserDetailAdmin(admin.ModelAdmin):
    list_display = ("id", "Name", "Email", "Phone", "Pan", "Account_No", "IFSC_code", "Account_Balance")
    search_fields = ("Name", "Email", "Phone", "Pan")
    list_filter = ("IFSC_code",)

@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "BankName", "QR")
    search_fields = ("BankName", "user__Email")

@admin.register(withdrawal)
class WithdrawalAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "Name", "Amount", "Status")
    search_fields = ("Name", "user__Email")
    list_filter = ("Status",)

@admin.register(DepositAccountDetails)
class DepositAccountDetailsAdmin(ImportExportModelAdmin):
    list_display = ('BankName', 'HolderName', 'AccountNumber')
    search_fields = ('BankName', 'HolderName', 'AccountNumber')
# Register your models here.
