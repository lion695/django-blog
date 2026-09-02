from django.shortcuts import render
from .models import About


# Create your views here.
def about_me(request):
    """
    Renders the most recent information on the website Author
    and allows user collaboration requests.
    """
    about = About.objects.all().order_by("-updated_on").first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )
