import boto3
from src.AIModule.poc_1.prompt_template import education_prompt
import json

def call_claude(question) -> str:
    prompt = education_prompt.format(question=question)

    client = boto3.client('bedrock-runtime', region_name='us-east-1')
    response = client.invoke_model(
        modelId="anthropic.claude-3-sonnet-20240229-v1:0",
        body=json.dumps({
            "prompt": prompt,
            "max_tokens": 400,
            "temperature": 0.7
        }),
        contentType="application/json"
    )

    response_body = response["body"].read()
    print('response_body', response_body)
    completion = json.loads(response_body)["completion"]
    print('completion',completion)
    return completion.strip()
