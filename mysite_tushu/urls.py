"""mysite_tushu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^publisher_list/$',views.publisher_list,name="publisher_list"),
    url(r'^add_pub/$',views.add_pub,name='add_pub'),
    url(r'^del_pub/$',views.del_pub,name='del_pub'),
    # url(r'^edit_pub/',views.edit_pub), #由add_pub中取代其功能
    url(r'^book_list/$',views.book_list,name='book_list'),
    url(r'^add_book/$',views.add_book,name='add_book'),
    url(r'^edit_book/([0-9]+)/$',views.edit_book,name='edit_book'),
    url(r'^del_book/([0-9]+)/$',views.del_book,name='del_book'),
    url(r'^autor_list/$', views.autor_list,name='autor_list'),
    url(r'^add_autor/$', views.add_autor,name='add_autor'),
    url(r'^edit_autor/([0-9]+)/$', views.edit_autor,name='edit_autor'),
    url(r'^del_autor/([0-9]+)/$', views.del_autor,name='del_autor'),
]
