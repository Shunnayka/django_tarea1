from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello World")

def nombre_completo(request):
    return HttpResponse("Shunayka Graciela Baquero Quintero")