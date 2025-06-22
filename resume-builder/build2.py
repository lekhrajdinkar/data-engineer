import os
import yaml
import pdfkit
from jinja2 import Environment, FileSystemLoader

suffix=input('please provide suffix - se2 | se3 ')
# Constants
OUTPUT_DIR = f"output/{suffix}"
TEMPLATE_FILE = f"template-{suffix}.html"
YAML_FILE = f"resume-{suffix}.yaml"
BASE_NAME = f"resume-{suffix}"

# Create output folder if not exists
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Find next version number
def next_version():
    existing_files = [f for f in os.listdir(OUTPUT_DIR) if f.startswith(BASE_NAME)]
    versions = []
    for f in existing_files:
        parts = f.replace(".pdf", "").replace(".html", "").split("_v")
        if len(parts) == 2 and parts[1].isdigit():
            versions.append(int(parts[1]))
    return max(versions, default=0) + 1

version = next_version()
html_file = f"{BASE_NAME}_v{version}.html"
pdf_file = f"{BASE_NAME}_v{version}.pdf"

# Load YAML data
with open(YAML_FILE, "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

# Render HTML using Jinja2
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template(TEMPLATE_FILE)
rendered_html = template.render(data)

# Save HTML
html_path = os.path.join(OUTPUT_DIR, html_file)
with open(html_path, "w", encoding="utf-8") as f:
    f.write(rendered_html)

# Generate PDF using pdfkit
pdf_path = os.path.join(OUTPUT_DIR, pdf_file)
#pdfkit.from_file(html_path, pdf_path)

print(f"✅ HTML saved to: {html_path}")
print(f"✅ PDF saved to: {pdf_path}")
