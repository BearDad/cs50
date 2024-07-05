from fpdf import FPDF, Align


def main():
    name = str(input("Name: "))
    pdf = FPDF(orientation="P", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", size=40, style="B")
    pdf.cell(200, None, "CS50 Shirtificate", 0, align="C")

    pdf.image("./shirtificate.png", Align.C, 30, 200, 200)
    pdf.set_font("Helvetica", size=40, style="B")
    pdf.set_text_color(255, 255, 255)
    page_width = pdf.w
    name_width = pdf.get_string_width(name)
    x = (page_width - name_width) / 2
    pdf.set_xy(x, 98)

    pdf.cell(name_width, None, f"{name}", 0, align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
