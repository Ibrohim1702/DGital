from django.shortcuts import render

from sayt.models import Subscribe


# Create your views here.


def index(requests):
    ctx = {}
    if requests.POST:
        email = requests.POST.get('email')
        Subscribe.objects.create(
            email=email
        )
        ctx = {
            "email": email
        }
    return render(requests, "index.html", ctx)

def about(requests):
    ctx = {

    }
    return render(requests, "about.html", ctx)

def contact(requests):
    ctx = {

    }
    return render(requests, "contact.html", ctx)

def projects(requests):
    ctx = {

    }
    return render(requests, "project.html", ctx)

def service(requests):
    ctx = {

    }
    return render(requests, "service.html", ctx)

def team(requests):
    ctx = {

    }
    return render(requests, "team.html", ctx)

def testimonial(requests):
    ctx = {

    }
    return render(requests, "testimonial.html", ctx)

