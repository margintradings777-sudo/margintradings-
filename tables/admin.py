from django.contrib import admin
from .models import UserDetail, Deposit, Withdrawal, DepositAccountDetails


@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    pass
    list_display = ("id", "Name", "Email", "Phone", "Pan", "Account_No", "IFSC_code", "Account_Balance")
    search_fields = ("Name", "Email", "Phone", "Pan")
    list_filter = ("IFSC_code",)

    # edit screen pe easy banane ke liye
    readonly_fields = ("id",)

    fieldsets = (
        ("Basic", {"fields": ("Name", "Email", "Phone", "Password")}),
        ("KYC", {"fields": ("Pan", "Pan_card_Image")}),
        ("Bank", {"fields": ("Account_No", "IFSC_code", "Cancel_cheque_or_bank_statement")}),
        ("Wallet", {"fields": ("Account_Balance",)}),
    )





@admin.register(Deposit)
class DepositAdmin(ImportExportModelAdmin):
    list_display = ('BankName', 'QR')
    search_fields = ('BankName',)

@admin.register(withdrawal)
class withdrawalAdmin(ImportExportModelAdmin):
    list_display = ('Name', 'Amount', 'Status')
    search_fields = ('Name', 'Amount', 'Status')

@admin.register(DepositAccountDetails)
class DepositAccountDetailsAdmin(ImportExportModelAdmin):
    list_display = ('BankName', 'HolderName', 'AccountNumber')
    search_fields = ('BankName', 'HolderName', 'AccountNumber')
# Register your models here.
