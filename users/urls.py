from django.urls import path
from users.views import login, register

app_name = 'users'

urlpatterns = [
    # где мы передавали например в href = "index.html" будем передавать href="{% url 'index' %}" в .html файле?
    path('login/', login, name='login'),
    path('register/', register, name='register'),

]