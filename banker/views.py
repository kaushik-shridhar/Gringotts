from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import View
from django.db import connection

from .models import userinfo, TransferInfo
from .forms import TransferForm

from datetime import date, datetime

# Create your views here.

class CustomerListView(ListView):
    model = userinfo
    template_name = 'banker/view_all_customers.html'
    context_object_name = 'customers'

class CustomerDetailView(DetailView):
    model = userinfo
    template_name = 'banker/customer_info.html'
    context_object_name = 'customer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TransferForm(initial={'sender_name':kwargs['object']})
        context['users'] = userinfo.objects.all()
        return context

class TransactionView(ListView):
    model = TransferInfo
    template_name = 'banker/transactions.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        return TransferInfo.objects.order_by('-time')

class TransferView(View):
    def send_money(self, sender, reciever, amt):
        sender_balance = userinfo.objects.raw(f"SELECT id, current_balance FROM banker_userinfo WHERE name='{sender}'")
        reciever_balance = userinfo.objects.raw(f"SELECT id, current_balance FROM banker_userinfo WHERE name='{reciever}'")
        transfer_date = date.today()
        now = datetime.now()
        transfer_time = now.strftime("%H:%M:%S")
        sender_updated_bal = sender_balance[0].current_balance-amt
        reciever_updated_bal = reciever_balance[0].current_balance+amt
        with connection.cursor() as cursor:
            cursor.execute(f"UPDATE banker_userinfo SET current_balance={sender_updated_bal} WHERE name='{sender}'")
            cursor.execute(f"UPDATE banker_userinfo SET current_balance={reciever_updated_bal} WHERE name='{reciever}'")
        a = TransferInfo.objects.create(sender_name=sender, reciever_name=reciever, amount=amt, date=transfer_date, time=transfer_time)
        a.save()

    def get(self, request, *args, **kwargs):
        return render(request, 'banker/view_all_customers.html')

    def post(self, request, *args, **kwargs):
        form = TransferForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['sender_name']
            reciever_name = form.cleaned_data['reciever_name']
            amt = form.cleaned_data['amount']
            reciever_name = userinfo.objects.get(pk=reciever_name).name
            self.send_money(sender_name, reciever_name, amt)
            return redirect('/customer_list/')
