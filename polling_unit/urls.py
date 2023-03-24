from django.urls import path
from . import views

urlpatterns = [
    path('<unitcode:unitcode>', views.show, name='show_polling_unit'),
]