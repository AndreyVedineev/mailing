from django.urls import path

from posting import views
from posting.apps import PostingConfig
from posting.views import IndexListView

app_name = PostingConfig.name

urlpatterns = [

    path("", IndexListView.as_view(), name='letters_list'),
    # path("contacts/", views.contacts, name="contacts/"),
    # path("<int:pk>/flowers_card/", flowers_card, name="flowers_card/"),
    # path("create/", Blog_flCreateView.as_view(), name="blog_fl_form/"),
    # path("edit/<int:pk>/", Blog_flUpdateView.as_view(), name="update_blog_fl_form/"),
    # path("list/", Blog_flListView.as_view(), name="blog_fl_list/"),
    # path("detail/<int:pk>", Blog_flDetailView.as_view(), name="blog_fl_detail/"),
    # path("delete/<int:pk>/", Blod_flDeleteView.as_view(), name="blog_fl_confirm_delete/"),
    # path("activity/<int:pk>", toggle_activity, name="toggle_activity/"),

]