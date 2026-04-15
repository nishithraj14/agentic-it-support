import logging
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

# ---------------- LOAD ENV ----------------
load_dotenv()

# ---------------- LOGGING ----------------
logging.basicConfig(level=logging.INFO)

# ---------------- IMPORT GRAPH ----------------
from app.graph.workflow import build_graph

# ---------------- INIT APP ----------------
app = FastAPI(
    title="Agentic IT Support API",
    description="Autonomous AI system for IT ticket resolution",
    version="1.0"
)

# Build graph once (important for performance)
graph = build_graph()


# ---------------- REQUEST SCHEMA ----------------
class Ticket(BaseModel):
    ticket: str


# ---------------- HEALTH CHECK ----------------
@app.get("/")
def health():
    return {
        "status": "running",
        "service": "Agentic IT Support API"
    }


# ---------------- MAIN ENDPOINT ----------------
@app.post("/resolve")
def resolve_ticket(req: Ticket):
    logging.info(f"[API] Received ticket: {req.ticket}")

    try:
        # 🔥 Invoke LangGraph agent
        result = graph.invoke({"ticket": req.ticket})

        # 🔥 Ensure structured response (safe access)
        response = {
            "ticket": req.ticket,
            "category": result.get("category"),
            "confidence": result.get("confidence"),
            "decision": result.get("decision"),
            "context": result.get("context"),
            "response": result.get("response"),
            "status": result.get("status", "completed")
        }

        return {
            "status": "success",
            "data": response
        }

    except Exception as e:
        logging.error(f"[API ERROR] {str(e)}")

        return {
            "status": "error",
            "message": str(e)
        }