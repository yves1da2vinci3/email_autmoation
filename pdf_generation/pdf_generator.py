import PyPDF2

def generate_pdf(emails_per_day):
    pdf_file = "daily_emails_pypdf2.pdf"
    
    pdf_writer = PyPDF2.PdfWriter()

    for day, emails in emails_per_day.items():
        pdf_page = PyPDF2.PageObject.createBlankPage(width=612, height=792)  # Letter page size
        pdf_canvas = PyPDF2.pdf.ContentStream([
            b"BT",
            b"/F1 12 Tf",
            b"1 0 0 1 100 750 Tm",
            f"(Date: {day}) Tj",
        ])
        pdf_page._contentStream = pdf_canvas
        pdf_writer.addPage(pdf_page)

        y_position = 700

        for email in emails:
            pdf_canvas = PyPDF2.pdf.ContentStream([
                b"BT",
                b"/F1 10 Tf",
                b"1 0 0 1 100 " + str(y_position) + b" Tm",
                f"(Object: {email['object']}) Tj",
                b"1 0 0 1 100 " + str(y_position - 20) + b" Tm",
                f"(Sender: {email['sender']}) Tj",
                b"1 0 0 1 100 " + str(y_position - 40) + b" Tm",
                f"(Content: {email['content']}) Tj",
                b"1 0 0 1 100 " + str(y_position - 60) + b" Tm",
                f"(Summary: {email['summary']}) Tj",
                b"ET"
            ])
            pdf_page = PyPDF2.PageObject.createBlankPage(width=612, height=792)  # Letter page size
            pdf_page._contentStream = pdf_canvas
            pdf_writer.addPage(pdf_page)
            
            y_position -= 100

    with open(pdf_file, 'wb') as pdf_output:
        pdf_writer.write(pdf_output)

    return pdf_file
