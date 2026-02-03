import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

DATA_DIR = os.path.join(BASE_DIR, "data")
GRAPH_FILE = os.path.join(DATA_DIR, "graph.pkl")
POS_FILE = os.path.join(DATA_DIR, "pos.pkl")

GRAPH_NODES = 10000
GRAPH_ATTACHMENTS = 4
GRAPH_SEED = 42