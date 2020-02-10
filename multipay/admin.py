from django.contrib import admin
from multipay.models import Gateway, GatewayTransaction


class GatewayAdmin(admin.ModelAdmin):
    list_display = ['app', 'sid', 'type', 'title', 'is_active', 'default', 'archive']
    list_filter = ['type', 'app']
    list_editable = ['default', 'archive']
    # autocomplete_fields = ['app']
    raw_id_fields = ['app']


admin.site.register(Gateway, GatewayAdmin)


class GatewayTransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'sid', 'reference', 'gateway', 'amount', 'status', 'created', 'error_message']
    list_filter = ['status']


admin.site.register(GatewayTransaction, GatewayTransactionAdmin)

#
# class CardNumberAdmin(admin.ModelAdmin):
#     list_display = ['number','bank_code', 'bank', 'bank_name']
#     list_filter = ['bank']
#     list_editable = ['bank',]
#     search_fields = ['bank_name','number']
#
# admin.site.register(CardNumber,CardNumberAdmin)
