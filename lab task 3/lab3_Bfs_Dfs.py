# Lab 3 Task 1 - BFS and DFS

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": [],
}

def bfs(start, goal):
    queue = [(start, [start])]
    visited = [start]
    while len(queue) > 0:
        node, path = queue.pop(0)
        if node == goal:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append( (neighbor, path + [neighbor]) )

def dfs(start , goal):
    stack = [(start, [start])]
    visited = []
    while len(stack) > 0:
        node, path = stack.pop()
        if node == goal:
            return path
        if node in visited:
            continue
        visited.append(node)
        for neighbor in reversed (graph[node]):
            stack.append( (neighbor, path + [neighbor]) )

def bfs_trace(start, goal):
    queue = [(start, [start])]
    visited = [start]
    order = []
    step = 0
    print("-----------BFS trace-----------")
    while len(queue) > 0:
        node, path = queue.pop(0)
        step = step + 1
        order.append(node)
        print("Step", step, ": processed", node, "path =", "->".join(path))
        if node == goal:
            queue_nodes = []
            for item in queue:
                queue_nodes.append(item[0])
            print("   goal reached, queue left:", queue_nodes)
            return path, order
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append((neighbor, path + [neighbor]))
        queue_nodes = []
        for item in queue:
            queue_nodes.append(item[0])
        print("   queue now:", queue_nodes)

def dfs_trace(start, goal):
    stack = [(start, [start])]
    visited = []
    order = []
    step = 0
    print("---------DFS trace--------")
    while len(stack) > 0:
        node, path = stack.pop()
        step = step + 1
        if node == goal:
            order.append(node)
            print("Step", step, ": processed", node, "path =", "->".join(path))
            stack_nodes = []
            for item in stack:
                stack_nodes.append(item[0])
            print("   goal reached, stack left:", stack_nodes)
            return path, order
        if node in visited:
            print("Step", step, ":", node, "already processed, skipped")
            continue
        visited.append(node)
        order.append(node)
        print("Step", step, ": processed", node, "path =", "->".join(path))
        for neighbor in reversed(graph[node]):
            stack.append((neighbor, path + [neighbor]))
        stack_nodes = []
        for item in stack:
            stack_nodes.append(item[0])
        print("   stack now:", stack_nodes)

if __name__ == "__main__":
    print("------Code output-------")
    print(bfs("A", "G"))
    print(dfs("A", "G"))
    print()
    bfs_path , bfs_order = bfs_trace("A", "G")
    print("BFS finaled path:", bfs_path)
    print("BFS visited order:", bfs_order)
    print()
    dfs_path, dfs_order = dfs_trace("A", "G")
    print("DFS final path:", dfs_path)
    print("DFS visit order:", dfs_order)
    print()
    print("BFS trace path same as bfs():", bfs_path == bfs("A", "G"))
    print("DFS trace path same as dfs():", dfs_path == dfs("A", "G"))
    print("BFS order same as A manual (A,B,C,D,E,F,G):", bfs_order == ["A",  "B", "C", "D", "E", "F", "G"])
    print("DFS order same as a manual (A,B,D,E,G):", dfs_order == ["A", "B", "D",  "E", "G"])