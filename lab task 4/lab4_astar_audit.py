print ("task 1")

graph = {
     "S" :[("A",1),("B",4)],
         "A":[(("C",2))],
         "B":[("G",5)],
         "C":[("G,3")],
         "G":[]}
h ={
    "S":5,
    "A":4,
    "B":4,
    "C":2,
    "G":0}

def A_star (graph,h,start,goal,show = False ):
    q = [(h[start],0,start,[start])]
    best ={start :0}
    expanded = []
    processed = []
    while q :
        q.sort()
        f,g,node,path=q.pop(0)
        if node == goal :
            processed.append(node +"(goal)")
            return g,path,expanded,processed
        if g!=best[node]:
            processed.append(node + "(stale)")
            continue
        processed.append(node)
        expanded.append(node)
        for nxt , w in graph.get(node,[]):
            ng = g + w
            if ng<best.get(nxt,1e9):
                best[nxt] = ng
                q.append((ng + h[nxt],ng,nxt,path+[nxt]))
        if show and  len (expanded) <= 3:                     
            print("selectad", node, "g =", g, "h =", h[node], "f =", f)
            for ff, gg, nn, pp in sorted(q):
                print("   frontier", nn, "g =", gg, "h =", h[nn], "f =", ff)
    return None, None, expanded, processed                   
def path_cost(graph, path):                                
    total = 0
    for a , b in zip(path, path[1:] ):
        for nxt, w in graph[a]:
            if nxt == b:
                total += w
    return total
A_star(graph, h, "S", "G", show = True)   


print ("task 2")
'''    task 2    '''



zero_h = {k: 0 for k in h}                                  
for name, hh in (("A*", h), ("UCS", zero_h)):               
    g, path, exp, proc = A_star(graph, hh, "S", "G")
    print(name, "path:", path, "cost:", g, "summed:", path_cost(graph, path))
    print("   processed:", proc)
    print("   expanded:", exp, "count:", len(exp))

h2 = dict(h)
h2["C"] = 10
g, path, exp, proc = A_star(graph, h2, "S", "G")
print(path, g, exp, len(exp))

''' task 3 '''
print ("task 3")


def true_cost(node):
    if node == "G":
        return 0
    return min(w + true_cost(n) for n, w in graph[node])

h2 = dict(h)
h2["C"] = 10
print("consistency audit (h)")
for u in graph:
    for v, w in graph[u]:
        print(u, "->", v, h[u], "<=", w + h[v], h[u] <= w + h[v])

print("admissibility check (h)")
for n in h:
    print(n, h[n], true_cost(n), h[n] <= true_cost(n))

print("admissibility check (h2, C = 10)")
for n in h2:
    print(n, h2[n], true_cost(n), h2[n] <= true_cost(n))

print(h["C"], h2["C"], true_cost("C"), h2["C"] <= true_cost("C"))

for name, hh in (("original", h), ("modified", h2)):        
    g, path, exp, proc = A_star(graph, hh, "S", "G")
    print(name, "path:", path, "cost:", g, "summed:", path_cost(graph, path))
    print("   processed:", proc)
    print("   expanded:", exp, "count:", len(exp))

    print("edge case: goal unreachable")
graph_nogoal = {"S": [("A", 1)], "A": [], "G": []}
h_nogoal = {"S": 1, "A": 1, "G": 0}
g, path, exp, proc = A_star(graph_nogoal, h_nogoal, "S", "G")
if path is None:
    print("No path found", exp)
else:
    print(path, g, path_cost(graph_nogoal, path), exp)


