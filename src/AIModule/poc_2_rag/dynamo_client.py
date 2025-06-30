import boto3
from decimal import Decimal
import os

REGION = "us-east-1"
TABLE_NAME = "rag_chunks"
ddb = boto3.resource("dynamodb", region_name=REGION)
table = ddb.Table(TABLE_NAME)

def save_chunk(doc_id, chunk_id, text, embedding, source):
    item = {
        "PK": f"DOC#{doc_id}",
        "SK": f"CHUNK#{chunk_id}",
        "text": text,
        "embedding": [Decimal(str(x)) for x in embedding],
        "source": source
    }
    table.put_item(Item=item)