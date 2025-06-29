import boto3
from src.AIModule.poc_1.prompt_template import education_prompt, education_prompt_1
import json

MODEL_ID = "anthropic.claude-3-sonnet-20240229-v1:0"
MODEL_VERSION = "bedrock-2023-05-31"
region= "us-east-1"

def call_claude_1(question) -> str:
    #prompt = education_prompt.format(question=question)

    messages = [
        #{"role": "system", "content": "You are a helpful financial educator who explains concepts clearly and simply."},
        {"role": "user", "content": education_prompt_1.format(question=question)}
    ]

    client = boto3.client('bedrock-runtime', region_name=region)
    response = client.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps({
            "anthropic_version": MODEL_VERSION,
            #"prompt": prompt,
            "messages": messages,
            #"max_tokens_to_sample": 400,
            "max_tokens": 100,
            "temperature": 0.7
        }),
        contentType="application/json"
    )

    response_body = response["body"].read()
    parsed = json.loads(response_body)

    # Claude's Messages API returns a list under "content"
    try:
        content_parts = parsed["content"]
        if isinstance(content_parts, list):
            return "".join(part.get("text", "") for part in content_parts).strip()
        else:
            return str(content_parts).strip()
    except KeyError:
        return parsed.get("message", "No content returned by Claude.").strip()


def call_claude(question: str, max_tokens: int = 400, temperature: float = 0.7) -> str:
    messages = [
        {"role": "user", "content": education_prompt.format(question=question)}
    ]

    client = boto3.client("bedrock-runtime", region_name=region)
    response = client.invoke_model(
        modelId="anthropic.claude-3-sonnet-20240229-v1:0",
        body=json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature
        }),
        contentType="application/json",
        accept="application/json"
    )

    response_body = response["body"].read()
    parsed = json.loads(response_body)

    try:
        content_parts = parsed["content"]
        if isinstance(content_parts, list):
            return "".join(part.get("text", "") for part in content_parts).strip()
        else:
            return str(content_parts).strip()
    except KeyError:
        return parsed.get("message", "No content returned by Claude.").strip()

