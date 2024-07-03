from django.shortcuts import render
from django.http import HttpResponseRedirect

from webapp.cat import Cat


# Create your views here.


def index(request):
    if request.method == "GET":
        return render(request, 'index.html')
    else:
        Cat.name = request.POST.get("cat_name")
        return HttpResponseRedirect("/cat_stats/")


def cat_stats(request):
    if request.method == "GET":
        context = {
            "name": Cat.name,
            "age": Cat.age,
            "avatar": Cat.avatar,
            "satiety": Cat.satiety,
            "happiness": Cat.happiness,
        }
        return render(request, "cat_stats.html", context=context)
    else:
        action = request.POST.get("action")
        if action == "play":
            Cat.play()
        elif action == "sleep":
            Cat.sleep()
        else:
            Cat.feed()
        return HttpResponseRedirect("/cat_stats/")

