from rest_framework import serializers
from decimal import Decimal
from datetime import datetime, timezone
from .models import Client, Payload, Payment


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'

    def to_representation(self, obj):
        return {
            "id": str(obj.id), 
        }


class PayloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payload
        fields = "__all__"

    def to_representation(self, obj):
        return {
            "id": str(obj.loan_id), 
            "installment": obj.instalment
            
        }


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

    def to_representation(self, obj):
        return {}
