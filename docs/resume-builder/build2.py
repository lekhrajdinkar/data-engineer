import os
import yaml
import pdfkit
from jinja2 import Environment, FileSystemLoader

TEMPLATE_DIR = "template"; YAML_DIR = "yaml"

all_templates = [f.replace(".html", "").split('-')[1] for f in os.listdir(TEMPLATE_DIR) if f.startswith(f"template")]
print("template options - ", *all_templates)
template1=input("choose template [default : 2] : ") or '2'
if template1 not in [*all_templates]:  yaml1 = all_templates[0]; print(f"Invalid yaml option provided. Defaulting to {template1}.")

all_yaml = [f.replace(".yaml", "").split('-')[1] for f in os.listdir(YAML_DIR) if f.startswith(f"resume")]
print("yaml options - ", *all_yaml)
yaml1=input("choose yaml [default : se3] : ") or 'se3'
if yaml1 not in [*all_yaml]:  yaml1 = all_yaml[0]; print(f"Invalid yaml option provided. Defaulting to {yaml1}.")


TEMPLATE_FILE = f"template/template-{template1}.html"
YAML_FILE = f"yaml/resume-{yaml1}.yaml"
BASE_NAME = f"resume-from-tpl-{template1}-profile-{yaml1}"
OUTPUT_DIR = f"output/{BASE_NAME}"

print('',OUTPUT_DIR, TEMPLATE_FILE, YAML_FILE, BASE_NAME, sep="\n 🟢 ")
# ======================================

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


version_option=input("enter version option [latest (hit enter)  | increment (press i)]: ") or 'latest'
if version_option == 'latest':
    version =  'latest'
else:
    version = next_version()

html_file = f"resume-from-tpl-{template1}-profile-{yaml1}_v{version}.html" #f"{BASE_NAME}_v{version}.html"
pdf_file = f"resume-from-tpl-{template1}-profile-{yaml1}_v{version}.pdf" #f"{BASE_NAME}_v{version}.pdf"

# Load YAML data
with open(YAML_FILE, "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

# Render HTML using Jinja2
env = Environment(loader=FileSystemLoader(''))
template = env.get_template(TEMPLATE_FILE)
rendered_html = template.render(data)

# Save HTML
html_path = os.path.join(OUTPUT_DIR, html_file)
with open(html_path, "w", encoding="utf-8") as f:
    f.write(rendered_html)

# Generate PDF using pdfkit
pdf_path = os.path.join(OUTPUT_DIR, pdf_file)
print(f"✅ HTML saved to: {html_path}")

pdfkit.from_file(html_path, pdf_path)
print(f"✅ PDF saved to: {pdf_path}")
