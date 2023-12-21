from django.urls import path
from users.views import login, register, profile, logout

app_name = 'users'

urlpatterns = [
    # где мы передавали например в href = "index.html" будем передавать href="{% url 'index' %}" в .html файле?
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
]