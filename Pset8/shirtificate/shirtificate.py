from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        #rendering logo:
        self.image("shirtificate.png", 10, pdf.eph / 5, pdf.epw)
        #setting font: helvetica bold 15
        self.set_font("Times", "B", 20)
        #moving cursor to the right:
        self.cell(20)
        #print title:
        self.cell(0, 10, txt="CS50 SHRTIFICATE", align="C")
        # Performing a line break:
        self.ln(20)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        #  Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        #  Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")


name = "Earl Kalf" #input("Name: ")
# instantiation of inherited class
pdf = PDF(orientation="P",unit="mm",format="A4")
pdf.add_page()
pdf.set_font("Times", size=40)
pdf.set_text_color(225, 255, 255)


pdf.cell(0, 200, f"{name} took CS50P", new_x="LMARGIN", new_y="NEXT", align="C")
pdf.output("shirtificate.pdf")

# print(pdf.eph)