from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Deposit
from .models import withdrawal, UserDetail, DepositAccountDetails

class UserDetailResource(resources.ModelResource):
    class Meta:
        model = UserDetail

@admin.register(UserDetail)
class UserDetailAdmin(ImportExportModelAdmin):
    resource_class = UserDetailResource
    list_display = ('Name', 'Email', 'Phone', 'Pan', 'Account_No', 'IFSC_code')
    search_fields = ('Name', 'Email', 'Phone', 'Pan')




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
