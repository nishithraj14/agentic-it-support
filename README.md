# 🚀 Agentic IT Service Desk Automation

An AI-powered system that autonomously classifies, retrieves, decides, and resolves IT support tickets.

---

## 🧠 Problem

Enterprise IT teams handle millions of repetitive tickets:

- Password resets
- VPN issues
- Network problems

Manual handling leads to:
- Slow resolution (2–3 hours)
- SLA violations
- High operational cost

---

## 🎯 Solution

Built an **agentic AI system** that:

✔ Classifies tickets using LLM  
✔ Retrieves enterprise policies (Hybrid RAG)  
✔ Makes intelligent decisions  
✔ Executes automated actions  
✔ Escalates when needed  

---

## ⚙️ Architecture
User → Streamlit UI → FastAPI → LangGraph Agent → Tools + RAG → Response


---

## 🔥 Features

- 🧠 LLM-based classification
- 🔎 Hybrid Retrieval (Embeddings + BM25)
- ⚡ Decision Engine (multi-factor)
- 🛠 Tool Execution (simulated automation)
- 📊 Observability (LangSmith)
- 🌐 Deployed on AWS EC2

---

## 🧪 Example

**Input:**

VPN not connecting


**Output:**
- Category: vpn_issue
- Decision: resolve
- Action: Restart VPN
- Status: Resolved

---

## 🛠 Tech Stack

- LangGraph
- LangChain
- OpenAI GPT-4o
- FastAPI
- PostgreSQL (pgVector / Neon)
- Streamlit
- AWS EC2
- LangSmith

---

## 🚀 Run Locally

### Backend

uvicorn app.main:app --reload


### Frontend

streamlit run streamlit_app.py


---

## 🌐 Live Demo

👉 (Add your Streamlit link after deployment)

---

## 💡 Key Learning

- Built real agentic system (not chatbot)
- Designed decision-based automation
- Implemented hybrid retrieval architecture
- Deployed production-style AI system

---

## 📌 Author

Nishit
📁 4. FINAL PROJECT STRUCTURE
agentic-automation/
│
├── app/
│   ├── main.py
│   ├── graph/
│   ├── rag/
│   ├── tools/
│
├── data/
│   ├── policies/
│
├── streamlit_app.py
├── test_system.py
│
├── requirements.txt
├── .gitignore
├── README.md