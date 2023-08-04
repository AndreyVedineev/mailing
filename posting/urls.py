from django.urls import path

from posting import views
from posting.apps import PostingConfig
from posting.views import IndexListView, LetterCreateView, LetterUpdateView, LetterDeleteView

app_name = PostingConfig.name

urlpatterns = [

    path("", IndexListView.as_view(), name='letter_list'),
    path("create/", LetterCreateView.as_view(), name='letter_create/'),
    path("edit/<int:pk>/", LetterUpdateView.as_view(), name="letter_update_form/"),
    path("delete/<int:pk>/", LetterDeleteView.as_view(), name="letter_confirm_delete/"),

    # path("contacts/", views.contacts, name="contacts/"),
    # path("<int:pk>/flowers_card/", flowers_card, name="flowers_card/"),

]