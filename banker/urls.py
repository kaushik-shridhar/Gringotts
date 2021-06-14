from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from .views import CustomerListView, CustomerDetailView, TransactionView, TransferView

app_name = 'banker'

urlpatterns = [
    path('', TemplateView.as_view(template_name='banker/index.html'), name='index'),
    path('customer_list/', CustomerListView.as_view(), name='customers'),
    path('customer_list/<pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('transactions/', TransactionView.as_view(), name='transaction-history'),
    path('transfer/', TransferView.as_view(), name='transfer'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)