from django.shortcuts import render

def index(request):
    return render(request, template_name="test_project/index.html")

