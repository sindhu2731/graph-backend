from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import networkx as nx

app = FastAPI(title="Graph API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def generate_graph():
    G = nx.barabasi_albert_graph(1000, 4)
    pos = nx.spring_layout(G, seed=42)

    nodes = []
    edges = []

    for node in G.nodes():
        nodes.append({
            "id": str(node),
            "label": f"Node {node}",
            "x": float(pos[node][0]),
            "y": float(pos[node][1]),
            "size": 3,
            "color": "#f26838",
        })

    for i, (source, target) in enumerate(G.edges()):
        edges.append({
            "id": f"e{i}",
            "source": str(source),
            "target": str(target),
            "size": 0.9,
            "color": "#999999",
        })

    return {"nodes": nodes, "edges": edges}


GRAPH_DATA = generate_graph()

@app.get("/graph")
def get_graph():
    return GRAPH_DATA

@app.get("/")
def root():
    return {"status": "FastAPI Graph Server Running"}
