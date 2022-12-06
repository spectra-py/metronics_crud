from django.shortcuts import render

# Create your views here.
def ajax(request):
    return render(request,'index.html')

def jquery(request):
    return render(request,'jquery.html')