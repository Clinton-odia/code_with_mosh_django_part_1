from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# uSE FOR HTTP REQUEST HANDLING
# HTTP REQUEST HANDLER


def say_hello(request):
    return render(
        request,
        "hello.html",
        {
            "name": "clinton",
            "occupation": "software engineer",
        },
    )
