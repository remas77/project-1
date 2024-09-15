from django.shortcuts import render

# Create your views here.
def index2 (requset):
     return render(requset,'index2.html',{'name':' bookmodule'})