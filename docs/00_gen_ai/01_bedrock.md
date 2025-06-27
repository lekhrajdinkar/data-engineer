## intro
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
- **RAG** (Retrieval-Augmented Generation, knowledge base)
- **LLM Agents**

## Transfer Learning >> Fine tune

| Step                | Transfer Learning          | Fine-Tuning                     |
| ------------------- | -------------------------- | ------------------------------- |
| Reuse early layers? | Yes, frozen (no training)  | Yes, but some layers retrained  |
| Train new layers?   | Only new classifier layers | Classifier + some old layers    |
| Speed               | Faster                     | Slower                          |
| Accuracy            | Good for limited data      | Better for task-specific tuning |


- **Transfer Learning**
    - reusing a pre-trained model to adapt it to a **new related task**
    - widely used in NLP and image model
    - eg: new layer added for new feature, then onl y last layer.
    - **fine-tune** is subtype
        - Instead of only training the last layer, you also adjust some earlier layers
        - takes more time but usually gets better accuracy
- All models can be fine-tuned
- Adapt a **copy of FM** with our own Training data ( format +  keep in S3)
- will change the **weights**
- **Fine tune::instruction based**
    - further trained on a particular field/domain by ML engineers
    - it will eat up Provisioned throughput $$
    - **label** ( [ {`prompt:` `response:`}])
    - **unlabel** ( [{`input:`}] ) === domain-adaptation fine-tuning
    - **Single/mutli turn Messaging**  --> conversation ( { `system:`, `messages:` [ { `role`:User/assistant, `content:` }, {}, ...] } )
        - chatbots