from fastapi import APIRouter, HTTPException
import app.graph.state as state

from app.graph.service import (
    get_sampled_graph,
    get_subgraph,
    get_node_info
)

router = APIRouter()

@router.get("/")
def health():
    return {"status": "Graph API running"}

@router.get("/graph")
def graph(limit: int = 500):
    return get_sampled_graph(state.BIG_GRAPH, state.BIG_POS, limit)

@router.get("/subgraph")
def subgraph(center: int = 0, depth: int = 2, limit: int = 300):
    return get_subgraph(state.BIG_GRAPH, center, depth, limit)

@router.get("/node/{node_id}")
def node_info(node_id: int):
    info = get_node_info(state.BIG_GRAPH, node_id)
    if not info:
        raise HTTPException(status_code=404, detail="Node not found")
    return info
