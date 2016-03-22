from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from datetime import datetime
from PyPDF2 import PdfFileReader, PdfFileWriter
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


class Command(BaseCommand):
    help = "Generate summer festival certificates."

    def handle(self, *args, **options):
        child_name = 'Timothy Gayed'

        pdf = PdfFileReader('/home/medhat/Dropbox/service/2016/summer_festival_certificates/CA_empty_name.pdf')
        page = pdf.getPage(0)

        s = StringIO.StringIO()
        c = canvas.Canvas(s, pagesize=letter)
        c.setFont("Helvetica", 26)
        c.drawCentredString(400, 350, child_name)
        c.save()

        pdf_with_custom_text = PdfFileReader(s)
        page.mergePage(pdf_with_custom_text.getPage(0))

        writer = PdfFileWriter()
        writer.addPage(page)
        
        with open('/home/medhat/Dropbox/service/2016/summer_festival_certificates/{}.pdf'.format(child_name), 'wb') as f:
            writer.write(f)
