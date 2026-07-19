from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT

INK = colors.HexColor("#14162B")
MUTED = colors.HexColor("#6B6E85")
BLUE = colors.HexColor("#5B6CFF")
TEAL = colors.HexColor("#17B8A6")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Name", fontName="Helvetica-Bold", fontSize=24, textColor=INK, leading=28))
styles.add(ParagraphStyle(name="Role", fontName="Helvetica", fontSize=12, textColor=BLUE, spaceAfter=4))
styles.add(ParagraphStyle(name="Contact", fontName="Helvetica", fontSize=9.5, textColor=MUTED))
styles.add(ParagraphStyle(name="H2", fontName="Helvetica-Bold", fontSize=12, textColor=TEAL, spaceBefore=14, spaceAfter=6))
styles.add(ParagraphStyle(name="Body", fontName="Helvetica", fontSize=10, textColor=INK, leading=14))
styles.add(ParagraphStyle(name="ItemTitle", fontName="Helvetica-Bold", fontSize=10.5, textColor=INK, leading=13))
styles.add(ParagraphStyle(name="ItemMeta", fontName="Helvetica-Oblique", fontSize=9, textColor=MUTED, leading=12))

doc = SimpleDocTemplate("assets/Naduni_Piyathilaka_CV.pdf", pagesize=A4,
                         topMargin=22*mm, bottomMargin=18*mm, leftMargin=20*mm, rightMargin=20*mm)

story = []

story.append(Paragraph("Naduni Piyathilaka", styles["Name"]))
story.append(Paragraph("Information Technology Undergraduate", styles["Role"]))
story.append(Paragraph(
    "yourname@gmail.com &nbsp;•&nbsp; github.com/yourusername &nbsp;•&nbsp; linkedin.com/in/your-profile &nbsp;•&nbsp; Sri Lanka",
    styles["Contact"]))
story.append(Spacer(1, 6))
story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor("#E1E1EE")))

story.append(Paragraph("PROFILE", styles["H2"]))
story.append(Paragraph(
    "Information Technology undergraduate at SLTC Research University with a strong interest in "
    "web development and software development. Passionate about learning new technologies and "
    "solving real-world problems through code, with hands-on experience building websites and "
    "small-scale software applications.", styles["Body"]))

story.append(Paragraph("EDUCATION", styles["H2"]))
story.append(Paragraph("BSc (Hons) in Information Technology", styles["ItemTitle"]))
story.append(Paragraph("SLTC Research University &nbsp;|&nbsp; 2025 – Present", styles["ItemMeta"]))
story.append(Paragraph(
    "Relevant coursework: Web Development, Programming Fundamentals, Database Management Systems, "
    "Professional Practice, Entrepreneurship &amp; Start-up Culture.", styles["Body"]))

story.append(Paragraph("PROJECTS", styles["H2"]))

projects = [
    ("Portfolio Website", "HTML, CSS, JavaScript",
     "Designed and developed a responsive personal portfolio website to showcase education, projects, and technical skills."),
    ("Student Management System", "Java, MySQL",
     "Developed a simple student management system for maintaining student records and academic information."),
    ("Mini Project", "HTML, CSS, JavaScript",
     "Completed an academic mini project as part of university coursework, applying core software development concepts."),
]
for title, stack, desc in projects:
    story.append(Paragraph(title, styles["ItemTitle"]))
    story.append(Paragraph(stack, styles["ItemMeta"]))
    story.append(Paragraph(desc, styles["Body"]))
    story.append(Spacer(1, 4))

story.append(Paragraph("SKILLS", styles["H2"]))
story.append(Paragraph(
    "<b>Languages:</b> HTML, CSS, JavaScript, Java, Python &nbsp;&nbsp;|&nbsp;&nbsp; "
    "<b>Tools &amp; Platforms:</b> MySQL, Git &amp; GitHub, Microsoft Office", styles["Body"]))

story.append(Paragraph("ACHIEVEMENTS", styles["H2"]))
story.append(Paragraph("Certifications and awards will be added here as they are completed.", styles["Body"]))

doc.build(story)
print("done")
