from django.urls import path

from clients.apps import ClientConfig
from clients.views import ClientsListView, ClientsCreateView, ClientsUpdateView, ClientsDeleteView

app_name = ClientConfig.name

urlpatterns = [

    path("", ClientsListView.as_view(), name='clients_list'),
    path("clients/create/", ClientsCreateView.as_view(), name='clients_create/'),
    path("clients/edit/<int:pk>/", ClientsUpdateView.as_view(), name="clients_update_form/"),
    path("clients/delete/<int:pk>/", ClientsDeleteView.as_view(), name="clients_confirm_delete/"),


]
