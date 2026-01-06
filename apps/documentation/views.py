from django.shortcuts import render

def home(request):
    return render(request, 'documentation/HOME.html')

def details(request):
    return render(request, 'documentation/DETAILS_PAGE.html')

def page_editor(request):
    return render(request, 'documentation/PAGE_EDITOR.html')