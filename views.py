from django.http import HttpResponse

def homepage(request):
    return HttpResponse("This is first publish in website")
    