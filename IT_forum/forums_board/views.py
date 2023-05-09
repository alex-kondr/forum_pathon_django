from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        "hello": "It`s work",
        "test_list": [1, 2, 3, 4, 5]
    }
    return render(request, "forums_board/index.html", context)