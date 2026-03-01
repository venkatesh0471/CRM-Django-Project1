from django.shortcuts import render
def html_page(request):
    return render(request,"index.html")