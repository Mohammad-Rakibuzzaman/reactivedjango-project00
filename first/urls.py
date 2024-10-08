
from django.contrib import admin
from django.urls import path, include
#add the rest auth token
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', include('demo.urls')),
    path('auth/', obtain_auth_token)

]
