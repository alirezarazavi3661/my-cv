from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
def Index_page(request):
    return render(request,'website/index.html')