from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def get_user_input():
    details = {}
    details['Name'] = input("Enter your name: ")
    details['Age'] = input("Enter your age: ")
    details['Gender'] = input("Enter your gender: ")
    details['Email'] = input("Enter your email: ")
    details['Phone'] = input("Enter your phone number: ")
    details['Objective'] = input("Enter your career objective: ")
    details['Work Experience'] = input("Enter your work experience: ")
    details['Education'] = input("Enter your education: ")
    details['Skills'] = input("Enter your skills: ")
    details['Certifications'] = input("Enter your certifications: ")
    details['LinkedIn'] = input("Enter your LinkedIn profile URL: ")
    details['GitHub'] = input("Enter your GitHub profile URL: ")
    return details

def generate_pdf(details):
    file_name = "resume.pdf"
    c = canvas.Canvas(file_name, pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(colors.black)
    c.drawString(200, height - 50, "Professional Resume")

    # Drawing a line
    c.setLineWidth(1)
    c.setStrokeColor(colors.grey)
    c.line(30, height - 60, width - 30, height - 60)

    # Personal Information
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(colors.black)
    c.drawString(30, height - 100, "Personal Information")

    c.setFont("Helvetica", 12)
    y = height - 130
    for key, value in details.items():
        if key in ['Name', 'Age', 'Gender']:
            c.drawString(50, y, f"{key}: {value}")
            y -= 20

    # Adding a space between sections
    y -= 20

    # Contact Information
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(colors.black)
    c.drawString(30, y, "Contact Information")

    c.setFont("Helvetica", 12)
    for key, value in details.items():
        if key in ['Email', 'Phone']:
            c.drawString(50, y - 20, f"{key}: {value}")
            y -= 20

    # Adding a space between sections
    y -= 40

    # Professional Summary
    c.setFont("Helvetica-Bold", 14)
    c.drawString(30, y, "Professional Summary")
    c.setFont("Helvetica", 12)
    y -= 30
    c.drawString(50, y, details['Objective'])

    # Adding a space between sections
    y -= 40

    # Work Experience
    c.setFont("Helvetica-Bold", 14)
    c.drawString(30, y, "Work Experience")
    c.setFont("Helvetica", 12)
    y -= 30
    c.drawString(50, y, details['Work Experience'])

    # Adding a space between sections
    y -= 40

    # Education
    c.setFont("Helvetica-Bold", 14)
    c.drawString(30, y, "Education")
    c.setFont("Helvetica", 12)
    y -= 30
    c.drawString(50, y, details['Education'])

    # Adding a space between sections
    y -= 40

    # Skills
    c.setFont("Helvetica-Bold", 14)
    c.drawString(30, y, "Skills")
    c.setFont("Helvetica", 12)
    y -= 30
    c.drawString(50, y, details['Skills'])

    # Adding a space between sections
    y -= 40

    # Certifications
    c.setFont("Helvetica-Bold", 14)
    c.drawString(30, y, "Certifications")
    c.setFont("Helvetica", 12)
    y -= 30
    c.drawString(50, y, details['Certifications'])

    # Adding LinkedIn and GitHub links
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(colors.black)
    c.drawString(30, y - 40, "Social Links:")
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.black)

    # Get text width
    linkedin_text = "LinkedIn"
    github_text = "GitHub"
    linkedin_width = c.stringWidth(linkedin_text)
    github_width = c.stringWidth(github_text)

    # Set links on text
    c.linkURL(details['LinkedIn'], (50, y - 60, 50 + linkedin_width, y - 50), thickness=0, color=None)
    c.linkURL(details['GitHub'], (50, y - 80, 50 + github_width, y - 70), thickness=0, color=None)

    # Draw text
    c.drawString(50, y - 60, linkedin_text)
    c.drawString(50, y - 80, github_text)

    # Adding a gray footer
    c.setFillColor(colors.lightgrey)
    c.rect(0, 0, width, 40, fill=1)

    c.save()
    print(f"PDF resume generated: {file_name}")

if __name__ == "__main__":
    user_details = get_user_input()
    generate_pdf(user_details)
