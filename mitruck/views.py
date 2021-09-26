"""
To render html web pages
"""
import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article


def home_view(request, *args, **kwargs):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """

    name = "Madhasuki"  # hard coded
    number = random.randint(1, 5)  # pseudo random
    # from the database ?
    article_obj = Article.objects.get(id=number)
    article_queryset = Article.objects.all

    context = {
        "object_list": article_queryset,
        "title": article_obj.title,
        "content": article_obj.content
    }

    # Django Template

    HTML_STRING = render_to_string("home-view.html", context=context)
    # HTML_STRING = """
    # <h1>{title} !</h1>
    # <p>{content}!</p>
    # """.format(**context)

    return HttpResponse(HTML_STRING)
