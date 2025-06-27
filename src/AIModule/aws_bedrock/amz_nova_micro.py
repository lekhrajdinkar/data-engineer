# NOT WORKING

import boto3

sts = boto3.client('sts')
print(sts.get_caller_identity())

session = boto3.Session(profile_name='genai', region_name='us-east-2')
client = session.client('bedrock-runtime')

MODEL_1 = 'ModelId="arn:aws:bedrock:us-east-2:533267082359:inference-profile/us.amazon.nova-micro-v1:0'

response = client.invoke_model(
    modelId=MODEL_1,
    contentType='application/json',
    accept='application/json',
    body='{"prompt": "what is genAI?", "max_tokens": 100}'
)

print(response['body'].read().decode())
