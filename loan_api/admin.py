from django.contrib import admin
from .models import Payload, Client, Payment


class PayloadAdmin(admin.ModelAdmin):
    list_display = [
        'loan_id',
        'amount',
        'term',
        'rate',
        'date'
    ]

class ClientAdmin(admin.ModelAdmin):
    list_display = [
        'client_id',
        'name',
        'surname',
        'email',
        'telephone',
        'cpf',
    ]

class PaymentAdmin(admin.ModelAdmin):
    list_display = ("loan_id", "status", "date", "amount")


admin.site.register(Payload, PayloadAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Payment, PaymentAdmin)