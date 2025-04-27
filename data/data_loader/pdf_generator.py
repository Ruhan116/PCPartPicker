import sqlite3
import os
import glob
from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch


class PDFGenerator:
    def __init__(self, db_path='data/database/database.sqlite'):
        self.db_path = db_path

    def clean_component(self, value):
        """Ensure each cell contains only one component"""
        if not value or str(value).strip() == "":
            return "-"
        components = str(value).split(" ")
        return " ".join(components[:4])

    def remove_old_pdfs(self):
        """Remove previous build PDFs"""
        pdf_files = glob.glob("builds_*.pdf")
        for file in pdf_files:
            try:
                os.remove(file)
                print(f"Removed old PDF: {file}")
            except Exception as e:
                print(f"Could not remove {file}: {e}")

    def generate_pdf(self, build_id=None):
        """Generate a PDF for all builds or a specific build if build_id is provided."""
        self.remove_old_pdfs()

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        if build_id:
            cursor.execute('SELECT rowid, * FROM Builds WHERE rowid = ?', (build_id,))
            builds = cursor.fetchall()
        else:
            cursor.execute('SELECT rowid, * FROM Builds')
            builds = cursor.fetchall()

        if not builds:
            print("No builds found in database")
            conn.close()
            return

        cursor.execute('PRAGMA table_info(Builds)')
        columns = ["#"] + [column[1] for column in cursor.fetchall()]

        filename = f"builds_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        doc = SimpleDocTemplate(filename, pagesize=letter)

        elements = []
        styles = getSampleStyleSheet()
        title = Paragraph("PC Builds Report", styles['Heading1'])
        elements.append(title)
        elements.append(Spacer(1, 0.2 * inch))

        for build in builds:
            build_data = list(zip(columns, [str(build[0])] + [self.clean_component(item) for item in build[1:]]))
            table = Table(build_data, colWidths=[1.5 * inch, 4.5 * inch])

            # Styling the vertical table
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3E606F')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 9),
                ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F5F5F5')),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.lightgrey),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('ROWHEIGHT', (0, 0), (-1, -1), 0.3 * inch),
            ]))

            # Add a title for each build
            build_title = Paragraph(f"<b>Build #{build[0]}</b>", styles['Heading3'])
            elements.append(build_title)
            elements.append(Spacer(1, 0.1 * inch))
            elements.append(table)
            elements.append(Spacer(1, 0.3 * inch))

        doc.build(elements)
        print(f"PDF generated: {os.path.abspath(filename)}")
        conn.close()


if __name__ == "__main__":
    pdf_generator = PDFGenerator()

    # Generate PDF for all builds
    print("Generating PDF for all builds...")
    pdf_generator.generate_pdf()

    # Generate PDF for a specific build (example: build_id = 1)
    print("Generating PDF for build ID 1...")
    pdf_generator.generate_pdf(build_id=1)
