## reference
- [gen ai 1](https://chatgpt.com/c/685dfae8-a808-800d-bc8c-4d992926601d) 🗨️
- [gen ai 2](https://chatgpt.com/c/685e3233-8420-800d-a08a-2cd8b933dad6) 🗨️
- 🟠 Udemy :: https://www.udemy.com/course/aws-ai-practitioner-certified/learn/lecture/44901525?start=15#overview
- 🟠 AWS training : https://skillbuilder.aws/learning-plan/G8ENMJ5QBE/aws-artificial-intelligence-practitioner-learning-plan/SU2A1EJM1A (8)
    ```
    --- 8 sections ---
    Fundamentals of AI and ML
    Exploring AI :: Use Cases and Applications
    Responsible AI Practices
    Developing ML Solutions
  
    Developing GenAI Solutions
    Optimizing FM
    Security, Compliance, and Governance for AI Solutions
    Essentials of Prompt Engineering
    ```
## A. Intro :: AI
```
- Artificial Intelligence (computer vision, NLP (computer lang 💻 <--> 🙍🏻‍♂️ human lang))
  ├── Machine Learning
  │   └── Deep Learning (Neural n/w, stacker layer)
  │       └── Generative AI

``` 
### NLP
- text classification
- sentiment analysis
- machine translation 
- language generation.

### Computer vision
- makes it possible for computers to interpret and understand digital images and videos.
- image classification
- object detection
- image segmentation

--- 

## Intro :: genAI + FM
- models that are pretrained on **internet-scale data** --> FM
- traditional ML : 
    - collect > prep > label > train > model-1 (**static**)
    - collect > prep > label > train > model-2 (static)
    - ...
    - collect > prep > label > train > FM > adapt to perform multiple task (**dynamic**) ⬅️
    - FMs can also serve as the starting point for developing more **specialized models**
- **Inference** is the process of using a FM to make predictions or generate **new** outputs
- genAI generates new data/content (ext, images, audio, code, or video) that is similar to the **data it was trained on**.
- **Specialized AI datacenters**
    - requires massive compute, typically across thousands of GPUs over weeks/months. NVIDIA A100  H100.
    - supercomputers with 10,000–25,000 GPUs, interconnected by high-speed NVLink
    - Training data is stored in fast, distributed SSD/NVMe storage. Needs hundreds of TBs to petabytes.
    - Infiniband : 400 Gbps
- examples 
```
== AI::NLP ==
    Text    : ChatGPT generating human-like conversations, essays, or emails.
    
== AI::Computer Vision ==
    Images  : DALL·E creating images from text descriptions.
    Audio   : AI generating music or voice from a script.

Code    : GitHub Copilot generating programming code suggestions.
```

### FM life cycle 
```
Data collect : website, book, etc
Data prep : struture/unstructure(image,etc) + labels, map() + unlabel(input), inheritance pattern, relationship
Data train with ML alog == 🔺initial pre-training🔺
Data evaluation
MODEL ready ✅
use it (inference) - batch + realtime

🔺Continious pre-training🔺 + evaluate ( metrics and benchmarks)
then use it

🔺optimized🔺 + evaluate  ( metrics and benchmarks)
prompt engineering
retrieval-augmented generation (RAG)
transfer learning(new layer) >>  🔺fine tune (some layer)🔺 >>  re-train (all layer)

Deploy FM :: production rnv

Obsevability ::
-  the model's performance is continuously monitored
- feedback is collected from users, domain experts, or other stakeholders
```

| Term       | Full Form               | What It Means                                                                     | Examples                                              |
| ---------- | ----------------------- | --------------------------------------------------------------------------------- | ----------------------------------------------------- |
| **AI**     | Artificial Intelligence | The broad field of building machines that mimic human intelligence                | Chatbots, self-driving cars, recommendation systems   |
| **ML**     | Machine Learning        | A subset of AI where machines learn from data without being explicitly programmed | Spam detection, fraud detection, image classification |
| **DL**     | Deep Learning           | A subset of ML using deep neural networks for complex tasks                       | Face recognition, speech-to-text, GPT models          |
| **Gen AI** | Generative AI           | A type of AI (often using DL) that generates new content (text, image, etc.)      | ChatGPT, DALL·E, GitHub Copilot, Sora                 |

### Fine-tuning vs retraining vs Transfer learning

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

---
### FM vs LLM

| **Aspect**        | **Foundation Model**                                                                     | **LLM (Large Language Model)**                                                        |
| ----------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Definition**    | A large, general-purpose model trained on diverse data that can be adapted to many tasks | A type of foundation model specialized in understanding and generating human language |
| **Domain**        | Multimodal: text, images, audio, video, code, etc.                                       | Primarily text (some LLMs now include code & basic image understanding)               |
| **Use Cases**     | Chatbots, image generation, code generation, audio transcription, robotics               | Text generation, summarization, translation, Q\&A                                     |
| **Training Data** | Diverse: images, video, text, code, audio, etc.                                          | Mostly large-scale text and code                                                      |

### LLM
- **Large Language Models** (LLMs): 
    - AI model trained on massive amounts of text to understand 
    - and generate human-like language.
    - Can answer questions, summarize, translate, write code, and more.
- **Diffusion Model**s / GANs: 
    - Used for generating images and videos.

### Multimodal models

### Other generative models
- GANs
- VAEs

---
## B. Core Architecture
### Transformers
### DL :: **neural network**
- tiny Nodes, connected together
- node talking and identify patterns
- These nodes are organized into **layers**
- stack of layers : input >> hidden/s >> putput
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

### **Recurrent Neural Networks** (RNNs)
- used for sequence data like time series, text, or speech.
- **GRU** Gated Recurrent Unit
- **LSTM** Long Short-Term Memory
  
  | Feature    | LSTM                           | GRU                        |
  | ---------- | ------------------------------ | -------------------------- |
  | Gates      | 3 (input, forget, output)      | 2 (update, reset)          |
  | Memory     | Hidden + cell state            | Single state (hidden only) |
  | Complexity | Higher                         | Lower (faster training)    |
  | Accuracy   | Slightly better for long tasks | Often comparable           |

### Diffusion models


---
## C. GenAI tools and frameworks
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

---
## D. More ➕
- Vector databases (e.g., FAISS, Pinecone, Weaviate)
- Observability, latency, rate limiting
- Cost optimization and caching

---
## Z. Learn by Doing
- Build a chatbot with OpenAI + FastAPI
- Try Hugging Face demos
- Connect your GenAI app to a company’s document set





