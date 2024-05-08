from django.urls import path
from . import views
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('admin-only/', staff_member_required(views.admin_only_view), name='admin_only'),
]
