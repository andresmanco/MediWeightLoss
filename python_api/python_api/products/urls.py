from django.conf.urls import url
from products.views import *

urlpatterns = [
url(r'^products/$', ProductList.as_view(), name = 'products')
]

app_name = 'product'
