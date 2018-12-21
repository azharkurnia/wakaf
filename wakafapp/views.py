from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'home.html')

def assets(request):
	return render(request,"assets.html")

def testtt(request):
	return render(request,'home-old.html')
