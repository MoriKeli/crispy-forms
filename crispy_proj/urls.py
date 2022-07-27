from django.contrib import admin
from django.urls import path

from crispy_forms_app.views import UserLogin    # import views from app

urlpatterns = [
    path('', UserLogin.as_view(), name='login'),
    path('admin/', admin.site.urls),
]
