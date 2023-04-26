from django.http import HttpResponse

# Create your views here.
def greeting_view(request):
    if request.method == "GET":
        name = request.GET.get("name", "[no name]")
        message = request.GET.get("message", "[no message]")
        return HttpResponse(f"Hello, {name}!<br>{message}")