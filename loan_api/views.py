from django.shortcuts import render, redirect, get_object_or_404, HttpResponse

from rest_framework.response import Response
from rest_framework.generics import (
    CreateAPIView
)

from .models import Client, Payload, Payment
from .serializers import ClientSerializer, PaymentSerializer, PayloadSerializer


class ClientCreateView(CreateAPIView):
    serializer_class = ClientSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PayloadCreateView(CreateAPIView):
    serializer_class = PayloadSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PaymentCreateView(CreateAPIView):
    serializer_class = PaymentSerializer

    def post(self, request, loan_id, *args, **kwargs):
        loan = get_object_or_404(
            Payload, loan_id=loan_id
        )
        data = request.data
        data["loan_id"] = loan.loan_id
        
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        

def test(request):
    return HttpResponse("Loan Management System")
