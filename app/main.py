from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.graph.store import load_or_create_graph
import app.graph.state as state
from app.api.routes import router

app = FastAPI(title="Graph Backend API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    state.BIG_GRAPH, state.BIG_POS = load_or_create_graph()
    print("🚀 Graph backend ready")

app.include_router(router)
