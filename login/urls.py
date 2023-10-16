from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

    

