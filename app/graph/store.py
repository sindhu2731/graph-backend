import os
import pickle
import networkx as nx
from app.core.config import GRAPH_FILE, POS_FILE, GRAPH_NODES, GRAPH_ATTACHMENTS

def load_or_create_graph():
    if os.path.exists(GRAPH_FILE) and os.path.exists(POS_FILE):
        print(" Loading graph from disk...")
        with open(GRAPH_FILE, "rb") as f:
            graph = pickle.load(f)
        with open(POS_FILE, "rb") as f:
            pos = pickle.load(f)
        return graph, pos

    print(" Creating new graph...")
    graph = nx.barabasi_albert_graph(GRAPH_NODES, GRAPH_ATTACHMENTS)
    pos = nx.spring_layout(graph, seed=42)

    os.makedirs(os.path.dirname(GRAPH_FILE), exist_ok=True)

    with open(GRAPH_FILE, "wb") as f:
        pickle.dump(graph, f)
    with open(POS_FILE, "wb") as f:
        pickle.dump(pos, f)

    print(" Graph cached")
    return graph, pos
    