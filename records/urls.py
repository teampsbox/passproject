from django.urls import path
from records import views

urlpatterns = [
    path('', views.CustomerList.as_view(), name='customer_list'),
    path('<int:pk>/', views.CustomerDetail.as_view(), name='customer_detail'),
    path('new/', views.CustomerNew.as_view(), name='customer_new'),
    path('<int:pk>/edit/', views.CustomerEdit.as_view(), name='customer_edit'),
    path('<int:pk>/delete', views.CustomerDelete.as_view(), name='customer_delete'),
]
