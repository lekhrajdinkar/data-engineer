## Project details
```
✅ Project Overview: Investor Education Chatbot

Goal:
    Allow users (clients or advisors) to ask investment-related 
    questions in natural language and get accurate, friendly explanations.
    educate clients on basic investment topics using LLM with American Funds tone.

Prompt: 
    “What is a target date fund?” or “How does dollar cost averaging work?”
    “What is dollar cost averaging?”
    “How do target date funds work?”
    “What is the difference between a mutual fund and ETF?”
    
Tech Stack:
    Bedrock Claude
    Python + LangChain
    Optionally fine-tuned FAQs from AmericanFunds.com

Bonus: 
    Add quiz feature using multiple-choice generation.


C:\Users\Manisha\Documents\GitHub\idea\02-etl-pyspark\
├── src\
│   └── poc_1\
│       ├── app.py                # FastAPI main app
│       ├── bedrock_client.py     # Handles AWS Bedrock calls
│       ├── prompt_template.py    # Prompt engineering
│       ├── utils.py              # Any helper functions
│       ├── ui_streamlit.py       # Optional: Streamlit frontend
│       └── topics\               # Optional: Static content for fallback
│           └── target_date_funds.md
├── requirements.txt


```

| Layer                | Tool                                 |
| -------------------- | ------------------------------------ |
| LLM                  | **AWS Bedrock** (Claude or Sonnet)   |
| App Backend          | **Python** + **FastAPI**             |
| LangChain (optional) | For prompt templates, memory         |
| UI                   | Streamlit or simple React (optional) |
| Logging / Metrics    | CloudWatch / local logs              |


---
## run project 
- **API** :: uvicorn src.AIModule.poc_1.app:app --reload
- **UI** :: streamlit run src/AIModule/poc_1/ui_streamlit.py
