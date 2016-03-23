from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from datetime import datetime
from PyPDF2 import PdfFileReader, PdfFileWriter
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os.path


class Command(BaseCommand):
    help = "Generate summer festival certificates."

    def handle(self, *args, **options):
        for cert_type, ss_class_children in settings.CERT_CHILDREN.iteritems():
            self.std
            for ss_class, children in ss_class_children.iteritems():
                for child in children:
                    paf_path = os.path.join(settings.CERT_TEMPLATE_PATH, settings.CERT_FILE[cert_type])
                    pdf = PdfFileReader(paf_path)
                    page = pdf.getPage(0)

                    s = StringIO.StringIO()
                    c = canvas.Canvas(s, pagesize=letter)

                    # Child
                    font_name = settings.CERT_COORD[cert_type]['child']['font']['name']
                    font_size = settings.CERT_COORD[cert_type]['child']['font']['size']
                    x = settings.CERT_COORD[cert_type]['child']['x']
                    y = settings.CERT_COORD[cert_type]['child']['y']
                    c.setFont(font_name, font_size)
                    c.drawCentredString(x, y, child)
                    c.save()

                    # Event
                    font_name = settings.CERT_COORD[cert_type]['event']['font']['name']
                    font_size = settings.CERT_COORD[cert_type]['event']['font']['size']
                    x = settings.CERT_COORD[cert_type]['event']['x']
                    y = settings.CERT_COORD[cert_type]['event']['y']
                    c.setFont(font_name, font_size)
                    c.drawCentredString(x, y, 'Sunday School Summer Festival {}'.format(datetime.now().strftime('%Y')))
                    c.save()

                    # Date
                    font_name = settings.CERT_COORD[cert_type]['date']['font']['name']
                    font_size = settings.CERT_COORD[cert_type]['date']['font']['size']
                    x = settings.CERT_COORD[cert_type]['date']['x']
                    y = settings.CERT_COORD[cert_type]['date']['y']
                    c.setFont(font_name, font_size)
                    c.drawCentredString(x, y, '{}'.format(datetime.now().strftime('%Y')))
                    c.save()

                    # Church
                    font_name = settings.CERT_COORD[cert_type]['church']['font']['name']
                    font_size = settings.CERT_COORD[cert_type]['church']['font']['size']
                    x = settings.CERT_COORD[cert_type]['church']['x']
                    y = settings.CERT_COORD[cert_type]['church']['y']
                    c.setFont(font_name, font_size)
                    c.drawCentredString(x, y, 'St. Mark Coptic Orthodox Church')
                    c.save()

                    pdf_with_custom_text = PdfFileReader(s)
                    page.mergePage(pdf_with_custom_text.getPage(0))

                    writer = PdfFileWriter()
                    writer.addPage(page)
                    
                    output_file = '{}_{}.pdf'.format(child, datetime.now().strftime('%Y'))
                    output_dir = os.path(settings.CERT_PATH, ss_class)
                    if not os.path.exists(output_dir):
                        os.makedirs(output_dir)
                    output_path = os.path(output_dir, output_file)
                    with open(output_path, 'wb') as f:
                        writer.write(f)
