# NOT WORKING :  The provided model identifier is invalid.

import boto3
import json

session = boto3.Session(profile_name="genai", region_name="us-east-2")
bedrock_runtime = session.client("bedrock-runtime")

model_id = "amazon.titan-text-lite-v1"

payload = {
    "inputText": "What is the difference between supervised and unsupervised learning?",
    "textGenerationConfig": {
        "maxTokenCount": 200,
        "temperature": 0.5,
        "topP": 0.9
    }
}

response = bedrock_runtime.invoke_model(
    modelId=model_id,
    contentType="application/json",
    accept="application/json",
    body=json.dumps(payload)
)

output = json.loads(response['body'].read())
print("\nResponse:\n")
print(output['results'][0]['outputText'])




