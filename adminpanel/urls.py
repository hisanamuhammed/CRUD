from django.urls import path

from . import views

urlpatterns = [

    path('admin_page/',views.admin_page,name='admin_page'),
    path('delete_user/<int:user_id>/',views.delete_user,name='delete_user'),
    path('<int:id>/',views.edit_user,name='update_user'),

]