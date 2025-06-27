# NOT WORKING

import boto3
import json

# Use Bedrock runtime client with your AWS profile and region
session = boto3.Session(profile_name="genai", region_name="us-east-2")
bedrock_runtime = session.client("bedrock-runtime")

# Model ID that supports streaming
model_id = "anthropic.claude-3-haiku-20240307-v1:0"

# Claude-style input
payload = {
    "anthropic_version": "bedrock-2023-05-31",
    "messages": [
        {
            "role": "user",
            "content": "What's the difference between AI and Machine Learning?"
        }
    ],
    "max_tokens": 512
}

# Call Bedrock with streaming
response = bedrock_runtime.invoke_model_with_response_stream(
    modelId=model_id,
    contentType="application/json",
    accept="application/json",
    body=json.dumps(payload)
)

# Print streamed response
print("Response:")
for event in response["body"]:
    chunk = json.loads(event["chunk"]["bytes"].decode())
    if "delta" in chunk:
        print(chunk["delta"]["text"], end="", flush=True)
