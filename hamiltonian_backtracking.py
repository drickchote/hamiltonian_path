#backtrack solution to find if a Hamiltonian path exists in a graph

def has_hamiltonian(graph, n):
    if n == 1: # Grafo com 1 vértice
        return True
    if n != len(graph): # Grafo desconexo
        return False

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

   
def main():
    n, m = map(int, input().split())

    graph = dict()
    for i in range(m):
        v1, v2 = input().split()
        if v1 not in graph:
            graph[v1] = set()
        if v2 not in graph:
            graph[v2] = set()
        graph[v1].add(v2)
        graph[v2].add(v1)

    return has_hamiltonian(graph, n)

    
print(main())