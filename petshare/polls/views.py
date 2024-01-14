from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Alina. You're at the polls index.")