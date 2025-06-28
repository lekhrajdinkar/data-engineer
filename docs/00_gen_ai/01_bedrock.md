## Intro
- interface to multiple foundation models
    - https://us-east-2.console.aws.amazon.com/bedrock/home?region=us-east-2#/model-catalog/serverless/amazon.nova-premier-v1:0 
    - https://us-east-2.console.aws.amazon.com/bedrock/home?region=us-east-2#/model-catalog/serverless/amazon.nova-micro-v1:0
    - ...
- Build Generative AI (Gen-AI) applications on AWS
- Fully-managed service : don’t need to manage GPU infra, **use models via simple API calls** + `boto3`
- provides access to multiple FM from different providers ⬅️
- **Unified APIs**
- **Provisioned throughput** : 
    - reserve a certain capacity of compute 
    - and requests for your Foundation Model (FMs) inference
    - guaranteeing performance and availability.
    - Instead of paying per request (on-demand), pre-allocate throughput capacity.
    - pay for the reserved throughput whether fully used or not
    - Helps avoid throttling and latency spikes.
- Leverage a wide array of foundation models.
    - amazon : **titan** , nova
    - meta: llama
    - Anthropic: claude
    - Mistral
    - choose one : by text,visual,multi, performance, token, level of customization, capabilties, pricing(by token),etc
- **RAG** (Retrieval-Augmented Generation, knowledge base)
- **LLM Agents**

---
## Model Lifecycle in Bedrock
- base model as a read-only template that AWS keeps stable
- When you customize it, AWS makes a copy for your account, like creating a fork of the model

| Phase                  | Description                                                                                    |
| ---------------------- | ---------------------------------------------------------------------------------------------- |
| **Base Model**         | Hosted by AWS (e.g., Titan, Claude, Jurassic, Mistral) — immutable and shared                  |
| **Fine-Tuned Version** | Your private copy with added training or instructions — only visible to you                    |
| **Inference Endpoint** | You call *your* version of the model via API; others don’t see or use it                       |
| **Billing**            | You’re billed for fine-tuning, storage, and inference time separately from the base model cost |


---
## Optimized FM :: Fine tune
- bedrock hosts the large foundation model, readOnly, and shared across customers.
   - makes a reference to the base model + delta layers(created with tuning) 
- Adapt a **copy of FM** with our own Training data ( formatted +  keep in S3)
- further trained on a particular field/domain by ML engineers
- it will eat up Provisioned throughput $$ while tuning/training.
- creates a lightweight, **private version** of the model without duplicating the global model (immutable/frozen) ⬅️
   - called adapters, LoRA layers, or delta weights
   - These new parameters plug into the base model at runtime

- **types**
```
Full                : Update all model weights (requires lots of compute)
Parameter-efficient : Update only small parts (like LoRA, adapters) to save cost and time
Prompt              : Learn soft prompts without changing model weights
```

- **strategies**
```
== Supervised Instruction Fine-Tuning ==
Labeled data :
[
  {
    "prompt": "How do you boil an egg?",
    "response": "Place the egg in boiling water for 9–12 minutes."
  }
]

== Domain Adaptation Fine-Tuning / continued pre-training ==
unlabeled domain-specific data :
need ML engineer
$$
[
  { "input": "Medical record of a patient with Type 2 diabetes..." }
]

== Conversation and single/Multi-Turn Messaging ==
To handle chat-style applications - Customer support bots, etc
{
  "system": "You are a helpful assistant.",
  "messages": [
    { "role": "user", "content": "What's the weather in LA?" },
    { "role": "assistant", "content": "It’s sunny and 75°F in Los Angeles today." },
    { "role": "user", "content": "What about tomorrow?" }
  ]
}

```


## 2. Evaluate Model
- evaluation metrics
- ways - manual or by another Model
- reference : benchmark
- compare model response with benchmark response
- seen on Console, will explore more later

## 3. RAG and Knowledge
- real-time data is needed to be fed into the FM , **outside of its training data**
- Bedrock takes care of creating **Vector Embeddings** (dynamoDB, aurora, RDS, ElasticSearch, Neptune)
- **Source** : s3, saleforce, confluence, website, sharpoint, etc
- ![img_1.png](../99_img/genai/01/img_1.png)
- ![img.png](../99_img/genai/01/img.png)

## 4. gaurdrail

## 5. Agents

## 6. More
### CW integration
### pricing


