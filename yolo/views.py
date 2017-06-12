from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import yolo.forms as forms
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.parsers import FileUploadParser,MultiPartParser,FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

from .yolomodel import yolo_model
import json
import os
yolo=yolo_model.yolo()
yolo.load()

## Create your views here.
def index(request):
    #return HttpResponse('Hello World!')
    my_dict = {'insert_me':'This is from views.py index function'}
    return render(request,'yolo/index.html',context=my_dict) #render functio knows to look for index.html in templates folder

def uploadimage(request,yolo=yolo):
    if request.method == "POST":
        form = forms.uploadimage(request.POST,request.FILES)
        if form.is_valid():
            print("Validation Success")
            result = handle_uploaded_file(request.FILES['image'],yolo)
            return render(request,'yolo/showimage.html',{'form':form,'result':result})
    else:
        form = forms.uploadimage()
    return render(request,'yolo/imageupload.html',{'form':form})

###--------------------------------------------------------------------
###--------------------------------------------------------------------

class FileUploadView(APIView):
    parser_classes = (FileUploadParser,)
    def post(self, request, filename, format=None):
        up_file = request.data['file']
        result = handle_uploaded_file(up_file,yolo)
        return Response({'status':200,'result':result})


##helper functions --------------------------------------------------------------
##-------------------------------------------------------------------------------

def handle_uploaded_file(f,yolo):
    file_path = 'static/images/in/test.jpg'
    with open(file_path,'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    ## preload weights
    result = yolo.predict(file_path)

    return result
