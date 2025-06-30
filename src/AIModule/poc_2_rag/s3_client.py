import boto3
import os

REGION = "us-east-1"
BUCKET_NAME = "genai-rag-demo-bucket"
s3 = boto3.client("s3", region_name=REGION)

def upload_file(file_path, filename):
    s3.upload_file(file_path, BUCKET_NAME, f"documents/{filename}")


### 📁 src/AIModule/poc_2_rag/utils.py

def chunk_text(text: str, max_tokens=200) -> list[str]:
    import textwrap
    return textwrap.wrap(text, width=max_tokens)