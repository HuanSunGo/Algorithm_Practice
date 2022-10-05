"""
Graph Definition: 
A set of edges E, with every edge in E connects two vertices.

Application: 
- web crawling: V -- page/website, E -- link
- social networking V -- people, E -- connection 

Realization: 
The matrix format uses too much space, dictionary is an ideal way of strorage. 

"""

# Traverse: breadth first search(BFS), pseudo code 
def bfs(graph,s):
    """
    TC: O(V+E*T)
    """
    frontier = [s]
    has_seen = set(s)
    while frontier:
        next = []
        for u in frontier: 
            for v in neighbors(u):
                if v not in has_seen:
                    next.append(v)
                    has_seen.add(v)
        frontier = next 