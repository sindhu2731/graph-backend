import networkx as nx


def get_sampled_graph(graph, pos, limit=500):
    nodes_list = list(graph.nodes())[:limit]
    subgraph = graph.subgraph(nodes_list)

    nodes = []
    edges = []

    for node in subgraph.nodes():
        nodes.append({
            "id": str(node),
            "label": f"Node {node}",
            "x": float(pos[node][0]),
            "y": float(pos[node][1]),
            "size": 3,
        })

    for i, (s, t) in enumerate(subgraph.edges()):
        edges.append({
            "id": f"e{i}",
            "source": str(s),
            "target": str(t),
        })

    return {"nodes": nodes, "edges": edges}


def get_subgraph(graph, center=0, depth=5, limit=300):
    """
    Returns a BFS-based subgraph from `center`
    with correct boundary detection (gray nodes).
    """

    nodes_depth = nx.single_source_shortest_path_length(
        graph, center, cutoff=depth
    )

    if not nodes_depth:
        return {
            "center": center,
            "nodes": [],
            "edges": []
        }

    actual_max_depth = max(nodes_depth.values())

    sorted_nodes = sorted(nodes_depth.items(), key=lambda x: x[1])

    selected_nodes = []
    for node, d in sorted_nodes:
        if len(selected_nodes) < limit or d == actual_max_depth:
            selected_nodes.append(node)

    subgraph = graph.subgraph(selected_nodes)

    pos = nx.spring_layout(subgraph, seed=42)

    nodes = []
    for node in subgraph.nodes():
        d = nodes_depth[node]
        nodes.append({
            "id": str(node),
            "depth": d,
            "is_boundary": d == actual_max_depth,
            "x": float(pos[node][0]),
            "y": float(pos[node][1]),
        })

    edges = [
        {"source": str(s), "target": str(t)}
        for s, t in subgraph.edges()
    ]

    return {
        "center": center,
        "requested_depth": depth,
        "actual_depth": actual_max_depth,
        "nodes": nodes,
        "edges": edges,
    }


def get_node_info(graph, node_id: int):
    if node_id not in graph:
        return None

    return {
        "id": node_id,
        "degree": graph.degree[node_id],
        "neighbors": list(graph.neighbors(node_id))[:20]
    }
