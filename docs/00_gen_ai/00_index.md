## reference
- [gen ai 1](https://chatgpt.com/c/685dfae8-a808-800d-bc8c-4d992926601d)
- [gen ai 1](https://chatgpt.com/c/685dfae8-a808-800d-bc8c-4d992926601d)

--- 
## Concept (genAI)
- Foundation Model, FM
- Fine-tuning vs retraining vs Transfer learning
- epoch and weight
- layers
- diffusion model
- LLM and LangChain
- GRU
- LSTM

## Code
- py lib : `diffusers`

## Bedrock
- Build Generative AI (Gen-AI) applications on AWS
- Fully-managed service
- **Unified APIs**
- Provisioned throughput
- Leverage a wide array of foundation models. 
    - amazon : **titan** , nova
    - meta: llama
    - Anthropic: claude
    - Mistral
    - choose one : by text,visual,multi, performance, token, level of customization, capabilties, pricing(by token),etc
- **RAG** (knowledge base)
- **LLM Agents**

### fine tune
- all models can be fine-tuned
- Adapt a copy of FM with our own Training data ( format +  keep in S3)
- will change the **weights**
- **Fine tune::instruction based**
    - further trained on a particular field/domain by ML engineers
    - it will eat up Provisioned throughput $$
    - **label** ( [ {`prompt:` `response:`}])
    - **unlabel** ( [{`input:`}] ) === domain-adaptation fine-tuning
    - **Single/mutli turn Messaging**  --> conversation ( { `system:`, `messages:` [ { `role`:User/assistant, `content:` }, {}, ...] } )
      - chatbots

