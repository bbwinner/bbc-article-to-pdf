from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import textwrap
import os

# Register Liberation Serif (Fedora system font)
FONT_PATH = "/usr/share/fonts/liberation-serif-fonts/LiberationSerif-Regular.ttf"
pdfmetrics.registerFont(TTFont("Serif", FONT_PATH))

def save_pdf(title, body, filename="output.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    margin = 50
    y = height - margin

    # Title: 16pt, centered
    c.setFont("Serif", 16)
    wrapped_title = textwrap.wrap(title, width=80)
    for line in wrapped_title:
        c.drawCentredString(width / 2, y, line)
        y -= 24

    y -= 10  # Extra space below title

    # Body: 12pt, left aligned
    c.setFont("Serif", 12)
    wrapper = textwrap.TextWrapper(width=95)

    for paragraph in body.split('\n\n'):
        lines = wrapper.wrap(paragraph)
        for line in lines:
            if y < margin:
                c.showPage()
                c.setFont("Serif", 12)
                y = height - margin
            c.drawString(margin, y, line)
            y -= 16
        y -= 12  # extra space between paragraphs

    c.save()
