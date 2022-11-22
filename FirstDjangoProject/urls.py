"""FirstDjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from FirstDjangoProject import views
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name="Home"),
    path('about-Us/', views.AboutUs, name="AboutUs"),
    path('project/', views.project, name="project"),
    path('team/',views.team, name="team"),
    path('what-do/',views.what_do, name="what_do"),
    path('contact/', views.contact, name="contact"),
    path('Submited/', views.Submited, name="Submited"),
    path('practiceFrm/', views.practiceFrm, name="practiceFrm"),
    path('submitform/', views.submitform, name="submitform"),
    path('calculate/', views.calculate, name="calculate"),
    path('oddEven/', views.oddEven, name="oddEven"),
    path('markshet/', views.markshet, name="markshet"),
    path('News-Us/<slug>', views.NewsShow, name="NewsShow"),

]
