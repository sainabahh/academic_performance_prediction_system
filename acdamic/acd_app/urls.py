"""acdamic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from acd_app import views

urlpatterns = [
    path('',views.login),
    path('adminhome',views.adminhome),
    path('logincode',views.logincode),
    path('register',views.register),
    path('register_code',views.register_code),
    path('logout',views.logout),
    path('addcourse',views.addcourse),
    path('addcourse1',views.addcourse1),
    path('deletecourse/<int:id>',views.deletecourse),
    path('addstaff',views.addstaff),
    path('deletestaff/<int:id>',views.deletestaff),
    path('editstaff/<int:id>',views.editstaff),
    path('deletesub/<int:id>',views.deletesub),
    path('updatestaff',views.updatestaff),
    path('addstaff1',views.addstaff1),
    path('addsubject',views.addsubject),
    path('addsubject1',views.addsubject1),
    path('allocsubject',views.allocsubject),
    path('allocsubject1',views.allocsubject1),
    path('deletealloc/<int:id>',views.deletealloc),
    path('managecourse',views.managecourse),
    path('managecourse_search', views.managecourse_search),
    path('managestaff',views.managestaff),
    path('managestaff_search',views.managestaff_search),
    path('managesub',views.managesub),
    path('managesub_search',views.managesub_search),
    path('viewalloc',views.viewalloc),
    path('viewalloc_search',views.viewalloc_search),
    path('viewcomplaint',views.viewcomplaint),
    path('viewcomplaint_search',views.viewcomplaint_search),
    path('viewfeedback',views.viewfeedback),
    path('viewreply',views.viewreply),
    path('viewstudentperformance',views.viewstudentperformance),
    path('viewperformance3',views.viewperformance3),


    #staff

    path('addstudymaterial',views.addstudymaterial),
    path('addstudymaterial1',views.addstudymaterial1),
    path('managestudymaterial',views.managestudymaterial),
    path('managestudymaterial1',views.managestudymaterial1),
    path('deletematerial/<int:id>',views.deletematerial),
    path('sendreply/<int:id>',views.sendreply),
    path('sendreply1',views.sendreply1),
    path('staffhomepage',views.staffhomepage),
    path('viewcomplaints',views.viewcomplaints),
    path('viewcomplaints1',views.viewcomplaints1),
    path('viewfeedback1',views.viewfeedback1),
    path('viewfeedback1_search',views.viewfeedback1_search),
    path('viewperformance',views.viewperformance),
    path('viewperformance2',views.viewperformance2),
    path('viewsubject',views.viewsubject),
    path('viewsubject2',views.viewsubject2),
    path('addwork',views.addwork),
    path('addworkpost',views.addworkpost),


    #Student

    path('complaintreply',views.complaintreply),
    path('homepagestudent',views.homepagestudent),
    path('sendcomplaint',views.sendcomplaint),
    path('sendcomplaints1',views.sendcomplaints1),
    path('sendreply2',views.sendreply2),
    path('sendfeedback',views.sendfeedback),
    path('sendfeedback1',views.sendfeedback1),
    path('viewstudymaterial',views.viewstudymaterial),
    path('viewstudymaterial1',views.viewstudymaterial1),
    path('viewsubject1',views.viewsubject1),
    path('viewsubject3',views.viewsubject3),
    path('viewperformance1',views.viewperformance1),
    path('VIEWwork',views.VIEWwork),
    path('uploadwork/<int:id>',views.uploadwork),
    path('sendremark/<int:id>',views.sendremark),
    path('sendremarks',views.sendremarks),
    path('update_work',views.update_work),
    path('staffVIEWworkStudent',views.staffVIEWworkStudent),
    path('emotion_post',views.emotion_post),




















]
