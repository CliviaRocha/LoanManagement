from django.db import models
from django.utils.translation import gettext as _


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(_('Name'), max_length=100)
    surname = models.CharField(_('Surname'), max_length=100)
    email = models.EmailField(_('Email'), max_length=254)
    telephone = models.CharField(_('Telephone'), max_length=100)
    cpf = models.CharField(_('CPF'), max_length=100, unique=True)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return f'Client Id: {self.client_id}'


class Payload(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    loan_id = models.AutoField(primary_key=True)
    amount = models.FloatField()
    term = models.IntegerField()
    rate = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f'Payload Id: {self.loan_id} instalment: {self.instalment}'

    @property
    def instalment(self):
        r = self.rate / self.term
        instalment = (
            (r + r / ((1 + r) ** self.term - 1))
            * self.amount
        )
        return round(instalment, 2)


class Payment(models.Model):
    """
    Payment Model
    Defines the attributes of a Payment
    """
    PAYMENT_CHOICES = (('made', 'made'), ('missed', 'missed'))

    loan_id = models.ForeignKey('Payload', on_delete=models.CASCADE)
    status = models.CharField('status', max_length=6, choices=PAYMENT_CHOICES)
    date = models.DateTimeField('Date', auto_now=False, auto_now_add=False)
    amount = models.DecimalField('Amount', max_digits=15, decimal_places=2)

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

    def __str__(self):
        return f"Payment(loan_id={self.loan_id}, status={self.status}, date={self.date}, amount={self.amount})"
