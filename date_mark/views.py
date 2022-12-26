from django.http import HttpResponse

from date_mark.service import ImportService


def index(request):
    response = ImportService().get_recommend('9а')
    return HttpResponse(f"<pre>{response}</pre>")
