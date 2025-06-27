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

## Transfer Learning >> Fine tune

- will change the **weights** in layers (neural network)
- All models can be fine-tuned

| Step                | Transfer Learning          | Fine-Tuning                     |
| ------------------- | -------------------------- | ------------------------------- |
| Reuse early layers? | Yes, frozen (no training)  | Yes, but some layers retrained  |
| Train new layers?   | Only new classifier layers | Classifier + some old layers    |
| Speed               | Faster                     | Slower                          |
| Accuracy            | Good for limited data      | Better for task-specific tuning |

### **Transfer Learning**
- reusing a pre-trained model to adapt it to a **new related task**
- widely used in NLP and image model
- eg: new layer added for new feature, then train only last layer.
- **fine-tune** is subtype
    - Instead of only training the last layer, you also adjust some earlier layers
    - takes more time but usually gets better accuracy

### fine tune
- Adapt a **copy of FM** with our own Training data ( format +  keep in S3)
- further trained on a particular field/domain by ML engineers
- Adapt general knowledge to our use case (e.g., legal , financial, medical data, etc)
- it will eat up Provisioned throughput $$
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

== Domain Adaptation Fine-Tuning ==
unlabeled domain-specific data :
[
  { "input": "Medical record of a patient with Type 2 diabetes..." }
]

== Conversation and Multi-Turn Messaging ==
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

### Re-train

| Aspect                   | Fine-Tuning                                                                             | Retraining                                                                    |
| ------------------------ | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Definition**           | Start with a pre-trained model and train it further on a smaller, task-specific dataset | Train a model from scratch or large dataset, often from random initialization |
| **Data Size**            | Usually small, task/domain-specific dataset                                             | Large dataset covering broad/general knowledge or new data                    |
| **Compute Cost**         | Lower, fewer epochs, updates only part/all weights                                      | Higher, requires full training from scratch                                   |
| **Time**                 | Faster to complete                                                                      | Time-consuming, longer training cycles                                        |
| **Use Case**             | Customize a model for specific task/domain                                              | Build a new model or significantly update with fresh data                     |
| **Model Starting Point** | Uses weights from an existing pre-trained model                                         | Starts with random or previous checkpoint (sometimes old model)               |
| **Flexibility**          | Good for domain adaptation or task-specific tweaks                                      | Suitable for major updates or completely new models                           |
| **Performance**          | Often better with limited data, leverages learned knowledge                             | Can be better if you have massive new data and resources                      |

