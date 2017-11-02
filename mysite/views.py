from django.http import JsonResponse
from mysite.models import (
    Page
)


def page_title(request):
    page = Page()
    page.title = "Title test"
    page.contents = "Contents test"

    return JsonResponse(page.to_dict())
