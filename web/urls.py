from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('logout/', signout,name='logout'),
    path('product/<int:product_id>/', product_details,name='product_details'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
