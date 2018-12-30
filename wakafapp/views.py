from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'home.html')

def assets(request):
	return render(request,"assets.html")

def volunteer(request):
	return render(request,"volunteer.html")

def article (request):
	return render(request,"article.html")

# def testtt(request):
# 	return render(request,'home-old.html')
