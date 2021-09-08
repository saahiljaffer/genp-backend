import functools

from django.conf import settings
from django.http import HttpResponse, FileResponse
from weasyprint import HTML
import tempfile
import json

def generate_pdf(request):
    data = json.loads(request.body)
    """Generate pdf."""
    html = HTML(string=data['text'])
    pdf_file = html.write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="home_page.pdf"'
    return response