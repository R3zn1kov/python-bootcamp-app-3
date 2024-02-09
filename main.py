from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Helvetica", style="B", size=18)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=1)
    pdf.line(x1=1.5, y1=1.5, x2=1.5, y2=1.5)

    pdf.ln(265)
    pdf.set_font(family="Helvetica", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R",)

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(265)
        pdf.set_font(family="Helvetica", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R", )


pdf.output("test.pdf")
