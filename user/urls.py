from django.urls import path
from user.views import UserView, UserDetailView, ApiDocView, AddTagView

urlpatterns = [
    path("", UserView.as_view(), name="account_page"),
    path("self/", UserDetailView.as_view(), name="user_page"),
    path("add_tag",AddTagView.as_view(), name="tag_new_page"),
    path("api_doc/", ApiDocView.as_view(), name="api_doc_page"),

]
