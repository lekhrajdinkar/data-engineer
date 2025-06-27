## reference
- [gen ai 1](https://chatgpt.com/c/685dfae8-a808-800d-bc8c-4d992926601d) 🗨️
- [gen ai 2](https://chatgpt.com/c/685e3233-8420-800d-a08a-2cd8b933dad6) 🗨️

--- 

## Intro
- create new content such as text, images, audio, code, or video.
- AI "generates" new data that is similar to the **data it was trained on**.
- Most 
```
Text: ChatGPT generating human-like conversations, essays, or emails.
Images: DALL·E creating images from text descriptions.
Audio: AI generating music or voice from a script.
Code: GitHub Copilot generating programming code suggestions.
```
## key technology
- **Foundation Model** FM
- **Large Language Models** (LLMs): 
    - AI model trained on massive amounts of text to understand 
    - and generate human-like language.
    - Can answer questions, summarize, translate, write code, and more.
- **Diffusion Model**s / GANs: 
    - Used for generating images and videos.
- Fine-tuning vs retraining vs Transfer learning

  | Method                | What It Does                                                | When to Use                                           |
  | --------------------- | ----------------------------------------------------------- | ----------------------------------------------------- |
  | **Retraining**        | Train all layers from scratch (no pre-learned knowledge)    | You have a **huge dataset** and want **full control** |
  | **Transfer Learning** | Reuse early layers, train only the last layer               | You have **limited data** and want to save time       |
  | **Fine-Tuning**       | Start from a pre-trained model and train some or all layers | You want to **adapt** a model to your domain          |

```
Transfer Learning
✅ Use Layer 1-3 (pretrained) ➡️ 🔒 Freeze them
🆕 Add new Layer 4 for your task ➡️ 🟢 Train only this

---
Fine-Tuning
✅ Use Layer 1-3 ➡️ 🔓 Unfreeze some (e.g., Layer 3)
🆕 Add Layer 4 ➡️ 🟢 Train both new and selected old layers

---
Think of it this way 🧠
    Retraining = Teach a student everything from zero 📖
    Transfer learning = Student already knows basics, you teach just the last chapter 📘
    Fine-tuning = Student knows a lot, but you adjust what they’ve learned to your topic ✏️
```


## Core Architecture
- Transformers
- **neural network**
    - stack of layers
    - each performing a specific transformation on the data as it passes through
    - freeze/unfreeze some layers so their weights don’t change, turning training.
    ```
    Input Layer (simple)    : Takes raw data (e.g., an image’s pixels).
    Hidden Layers           : Intermediate layers that learn features like edges, shapes, textures.
    ...
    ...
    Output Layer (complex)  : Produces the final prediction (e.g., “cat” or “dog”).
    ---
    [Input Layer]
    ⬇️
    [Layer 1: Detects Edges]
    ⬇️
    [Layer 2: Detects Shapes]
    ⬇️
    [Layer 3: Detects Object Parts]
    ⬇️
    [Layer 4: Classifies Object]
    ```
- **epoch** :  
    - training happens over many epochs to help the model learn better
    - during model training, one complete pass through.
    - If having 1000 training examples, 1 epoch means the model has seen all 1000 examples once.
- **weight**
    - parameters inside a neural network that the model learns and updates during training 
    - control how input data is transformed as it passes through the network
    - Training adjusts these weights to minimize errors and improve predictions.

- **Recurrent Neural Networks** (RNNs)
    - used for sequence data like time series, text, or speech.
    - **GRU** Gated Recurrent Unit
    - **LSTM** Long Short-Term Memory
  
      | Feature    | LSTM                           | GRU                        |
      | ---------- | ------------------------------ | -------------------------- |
      | Gates      | 3 (input, forget, output)      | 2 (update, reset)          |
      | Memory     | Hidden + cell state            | Single state (hidden only) |
      | Complexity | Higher                         | Lower (faster training)    |
      | Accuracy   | Slightly better for long tasks | Often comparable           |


## GenAI tools and frameworks
### Python-based
- `diffusers`  
- `TensorFlow` 
- `pytorch`
- `LangChain` 
    - Python/JavaScript framework for building applications with LLM
    - integrate LLMs with real-world data (APIs, SQL, docs)
    - prg:
        - Document Q&A system (e.g., chat with PDF, DB, storage)
        - Chatbot with memory
        - Enterprise search engine (RAG pattern)
  
### more
- **Jupyter Notebooks** for experimentation
- Model fine-tuning (LoRA, PEFT)

### Cloud and MLops
- AWS Bedrock, SageMaker
- GPU-backed compute
- CI/CD pipelines for ML (MLOps)
- Prompt engineering

## more
- Vector databases (e.g., FAISS, Pinecone, Weaviate)
- Observability, latency, rate limiting
- Cost optimization and caching

## Learn by Doing
- Build a chatbot with OpenAI + FastAPI
- Try Hugging Face demos
- Connect your GenAI app to a company’s document set



