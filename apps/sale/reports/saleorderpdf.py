"""PDF para la sale order
"""
# Librerias Standard
import io
import locale

# Librerias Django
from django.conf import settings
from django.http import FileResponse, HttpResponse
from django.utils import timezone

# Librerias de terceros
from apps.sale.models import PySaleOrder, PySaleOrderDetail
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle

locale.setlocale(locale.LC_ALL, '')
locale._override_localeconv = {'mon_thousands_sep': '.'}


def sale_order_pdf(request, pk):
    """ Función para imprimir la orden de ventas
    """
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "clientes.pdf"
    response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name

    # Los productos de la orden
    _sale_order = PySaleOrder.objects.get(pk=pk)

    # Los productos de la orden ya en una matriz
    _products = PySaleOrderDetail.objects.filter(sale_order=pk).only(
        "product",
        "description",
        "quantity",
        "amount_untaxed",
        "discount",
        "amount_total"
    )

    # Create a file-like buffer to receive PDF data.
    _buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    _pdf = canvas.Canvas(_buffer, pagesize=letter)

    # Header corporativa
    archivo_imagen = settings.MEDIA_ROOT+'/pyerp-marketing/PyERP_logo_2.png'
    # Definimos el tamaño de la imagen a cargar y las coordenadas
    _pdf.drawImage(archivo_imagen, 30, 710, 120, 90, preserveAspectRatio=True)
    _pdf.setLineWidth(.3)
    _pdf.line(30, 735, 582, 735)

    # Header del reporte
    _pdf.setFont('Helvetica', 22)
    _pdf.drawString(30, 650, 'Presupuesto # ' + _sale_order.name)

    _pdf.setFont('Helvetica-Bold', 12)
    _pdf.drawString(30, 625, 'Fecha de cotización:')

    _pdf.setFont('Helvetica-Bold', 12)
    _pdf.drawString(180, 625, 'Vendedor:')

    today = timezone.now()
    _pdf.setFont('Helvetica', 12)
    _pdf.drawString(30, 610, today.strftime("%Y-%m-%d %H:%M:%S"))

    _pdf.setFont('Helvetica', 12)
    _pdf.drawString(180, 610, 'Nombre del Vendedor')

    # Alto y ancho de la hoja
    _width, _height = letter

    # A partir de que altura debriamos imprimir la tabla
    _high = 550

    # Header de la tabla
    _data_header = []
    _data_header.append([
        # "Producto",
        "Descripcion",
        "Cantidad",
        "Precio",
        "Descuento",
        "Sub Total"
    ])

    # Imprimir el header de la tabla
    table = Table(
        _data_header,
        colWidths=[7*cm, 3*cm, 3*cm, 3*cm, 3.5*cm]
    )
    table.setStyle(
        TableStyle([
            # ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            # ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
            ('LINEABOVE', (0, 0), (-1, 0), 1.5, colors.black),
            ('LINEBELOW', (0, 0), (-1, 0), 1.5, colors.black),
            # ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
            ('ALIGN', (1, 0), (-1, 0), 'RIGHT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
        ])
    )
    table.wrapOn(_pdf, _width, _height)
    table.drawOn(_pdf, 30, _high)

    # Cuerpo de la tabla
    _data_table = []
    for _product in _products:
        _data_table.append(
            [
                _product.product,
                # _product.description,
                str(_product.quantity) + ' Unidades',
                _product.amount_untaxed,
                _product.discount,
                locale.format(
                    '%.2f',
                    _product.amount_total,
                    grouping=True,
                    monetary=True
                )
            ]
        )
        _high = _high - 18

    # Imprimir cuerpo la tabla
    table = Table(
        _data_table,
        colWidths=[7*cm, 3*cm, 3*cm, 3*cm, 3.5*cm]
    )
    table.setStyle(
        TableStyle([
            # ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            # ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
            ('LINEBELOW', (0, 0), (-1, -1), 0.5, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            # ('ALIGN', (0, 0), (0, -1), 'CENTER'),
            ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
        ])
    )
    table.wrapOn(_pdf, _width, _height)
    table.drawOn(_pdf, 30, _high)

    # Footer de la tabla
    _data_foot = []
    _data_foot.append(
        ["", "Subtotal:", "$ " + locale.format('%.2f', _sale_order.amount_untaxec, grouping=True, monetary=True)]
    )
    _data_foot.append(
        ["", "IVA:", "$" + "???"]
    )
    _data_foot.append(
        ["", "Total:", "$" + "???"]
    )

    _high = _high - (18 * 3)
    # Imprimir cuerpo la tabla
    table = Table(
        _data_foot,
        colWidths=[13*cm, 3*cm, 3.5*cm]
    )
    table.setStyle(
        TableStyle([
            # ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            # ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
            ('LINEBELOW', (1, 0), (2, 0), 1.5, colors.black),
            ('LINEBELOW', (1, 1), (2, 1), 0.5, colors.black),
            ('LINEBELOW', (1, 2), (2, 2), 1.5, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            # ('ALIGN', (0, 0), (0, -1), 'CENTER'),
            ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
            ('FONTNAME', (1, 0), (1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('FONTNAME', (1, 2), (1, 2), 'Helvetica-Bold'),
        ])
    )
    table.wrapOn(_pdf, _width, _height)
    table.drawOn(_pdf, 30, _high)

    # Close the PDF object cleanly, and we're done.
    _pdf.showPage()
    _pdf.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    _buffer.seek(0)
    response.write(_buffer.getvalue())

    return response
