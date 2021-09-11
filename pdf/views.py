import functools

from django.conf import settings
from django.http import HttpResponse, FileResponse
from weasyprint import HTML, CSS
import tempfile
import json


def generate_pdf(request):
    data = json.loads(request.body)
    """Generate pdf."""
    html = HTML(string=data["text"])
    css = CSS(string=data["css"])
    pdf_file = html.write_pdf(stylesheets=[css])
    response = HttpResponse(pdf_file, content_type="application/pdf")
    response["Content-Disposition"] = 'filename="home_page.pdf"'
    return response
