# Lab 3 Task 2 - DLS and IDDFS (root A is depth 0)

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": [],
}

def dls(graph_data, node, goal, limit, path, visited_log):
    visited_log.append(node)
    if node == goal:
        return "FOUND", path
    if limit == 0:
        for neighbor in graph_data[node]:
            if neighbor not in path:
                return "CUTOFF", None
        return "FAILURE", None
    cutoff = False
    for neighbor in graph_data[node]:
        if neighbor in path:
            continue
        status, result_path = dls(graph_data, neighbor, goal, limit - 1, path + [neighbor], visited_log)
        if status == "FOUND":
            return status, result_path
        if status == "CUTOFF":
            cutoff = True
    if cutoff:
        return "CUTOFF", None
    return "FAILURE", None

def run_dls(graph_data, start, goal, limit, visited_log=None):
    if visited_log is None:
        visited_log = []
    return dls(graph_data, start, goal, limit, [start], visited_log)

def iddfs(graph_data, start, goal, max_depth):
    limits_tried = []
    status = "FAILURE"
    for limit in range(0, max_depth + 1):
        limits_tried.append(limit)
        status, path = run_dls(graph_data, start, goal, limit)
        if status == "FOUND":
            return status, path, limits_tried
        if status == "FAILURE":
            return status, None, limits_tried
    return status, None, limits_tried

if __name__ == "__main__":
    print("== DLS, on original graph, start A, goal G ==")
    for limit in  (1, 2, 3, 4):
        status, path = run_dls(graph, "A", "G", limit)
        if path:
            path_text = "->".join(path)
        else:
            path_text = None
        print(f"limit={limit}: status={status}, path={path_text}")

    print("\n== IDDFS with maximum depth 1..4 ==")
    for max_depth in(1, 2, 3, 4):
        status , path , limits_tried = iddfs(graph, "A", "G", max_depth)
        if path:
            path_text = "->".join(path)
        else:
            path_text = None
        print(f"max_depth={max_depth}: status={status}, path={path_text} , limits attempted={limits_tried}")

    print("\n------------Repeated work in IDDFS------------")
    total_nodes = 0
    for limit in range(0, 4):
        visited_log = []
        run_dls(graph, "A", "G", limit, visited_log)
        total_nodes = total_nodes + len(visited_log)
        print(f"limit={limit}: {visited_log}  count={len(visited_log)}")
    print("total nodes processed by IDDFS:", total_nodes)

    print("\n --------------Edge cases -------------")
    print("start == goal  :", run_dls(graph, "A", "A", 0))
    print("unreachable goal Z (graph has no Z):")
    graph2 = dict(graph)
    graph2["Z"] = []
    for limit in (2, 6):
        print(f"   DLS limit={limit}:", run_dls(graph2, "A", "Z", limit))
    print("   IDDFS max, 6   :", iddfs(graph2, "A", "Z", 6))
    cycle_graph =  {"A": ["B"], "B": ["C"], "C": ["A", "D"], "D": [ ]}
    print("cycle graph A->B->C->A, goal D:")
    print("   DLS limit=5   :", run_dls(cycle_graph, "A", "D", 5))
    print("   IDDFS max 5   :", iddfs(cycle_graph, "A", "D", 5))
    print("cycle graph, unreachable goal X:")
    cycle_graph["X"] = []
    print("   DLS limit=5   :", run_dls(cycle_graph, "A", "X", 5))