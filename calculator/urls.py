from django.urls import path
from . import views

urlpatterns = [
    path('tambah/<int:num1>/<int:num2>',views.tambah),
    path('kurang/<int:num1>/<int:num2>',views.kurang),
    path('kali/<int:num1>/<int:num2>',views.kali),
    path('bagi/<int:num1>/<int:num2>',views.bagi)
]