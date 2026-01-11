#backtrack solution to find if a Hamiltonian path exists in a graph
import time
def has_hamiltonian(graph, n):
    if n == 1: # Grafo com 1 vértice
        return True

    vertices = graph.keys()

    for vertice in vertices:
        if(check_path(graph, source=vertice, memo={})):
            return True
        
    return False

def check_path(graph, source, number_of_visited=1, memo = {}):
    memo[source] = True

    if number_of_visited == len(graph):
        return True
    
    for vertice in graph[source]:
        if vertice in memo:
            continue
        if check_path(graph, vertice, number_of_visited+1, memo):
            return True
    del memo[source]
    return False
