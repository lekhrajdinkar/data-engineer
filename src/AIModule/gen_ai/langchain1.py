from langchain.llms import Bedrock
import boto3

# Bedrock client
bedrock_client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Claude model wrapper
llm = Bedrock(
    model_id="anthropic.claude-3-haiku-20240307",  # or other Claude model
    client=bedrock_client,
    model_kwargs={"max_tokens_to_sample": 300}
)

response = llm.invoke("Explain large language models in simple terms.")
print(response)
