import yaml
from jinja2 import Environment, FileSystemLoader
import pdfkit

# Load YAML
with open("resume.yaml") as f:
    data = yaml.safe_load(f)

# Render HTML
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("template.html")
html_content = template.render(data)

# Save HTML and then convert to PDF
with open("resume.html", "w", encoding="utf-8") as f:
    f.write(html_content)

pdfkit.from_file("resume.html", "resume.pdf")
print("✅ resume.pdf generated successfully.")