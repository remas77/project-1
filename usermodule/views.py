from django.shortcuts import render

# Create your views here.
def index3 (requset):
     return render(requset,'index3.html',{'name':' usermodule'})