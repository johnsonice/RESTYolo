from django.conf.urls import url
from yolo import views

urlpatterns =[
    url(r'^$',views.index,name='index'),
    url(r'^uploadimage',views.uploadimage,name='imageupload'),
    url(r'^api/upload/(?P<filename>[^/]+)$', views.FileUploadView.as_view()),
]
