from django.http import HttpResponse

from date_mark.service import ImportService


def index(request):
    ImportService().import_data('9а')
    return HttpResponse("Hello, world. You're at the polls index.")