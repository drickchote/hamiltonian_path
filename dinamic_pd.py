from typing import Dict, Iterable, List
import time

def has_hamiltonian_path_bitmask(graph) -> bool:
    """
    Hamiltonian Path (decision) using DP with bitmask:
        dp[mask][v] = True if there exists a path that visits exactly the vertices in 'mask'
                      and ends at vertex v.

    graph: adjacency list (directed or undirected). Vertices must be hashable.
    Returns: True if there exists a Hamiltonian path, otherwise False.
    """
    vertices = list(graph.keys())
    n = len(vertices)
    if n == 0:
        return True
    if n == 1:
        return True

    # Map original vertex labels -> 0..n-1
    idx = {v: i for i, v in enumerate(vertices)}

    # Build adjacency in index form
    adj: List[List[int]] = [[] for _ in range(n)]
    for v in vertices:
        v_i = idx[v]
        for u in graph.get(v, []):
            if u in idx:  # ignore neighbors not in vertex set
                adj[v_i].append(idx[u])

    # dp[mask] is an integer bitset over end-vertices:
    # bit v is 1 if dp[mask][v] is True
    # This is much lighter than a 2^n x n boolean matrix in Python.
    dp = [0] * (1 << n)

    # Initialize: paths that start at each vertex
    for v in range(n):
        dp[1 << v] |= (1 << v)

    # Transitions
    for mask in range(1 << n):
        ends_bitset = dp[mask]
        if ends_bitset == 0:
            continue

        # Iterate over possible end vertices v present in ends_bitset
        vb = ends_bitset
        while vb:
            lsb = vb & -vb
            v = (lsb.bit_length() - 1)
            vb ^= lsb

            # Try to extend from v to each neighbor u not yet in mask
            for u in adj[v]:
                if (mask >> u) & 1:
                    continue
                next_mask = mask | (1 << u)
                dp[next_mask] |= (1 << u)

    full_mask = (1 << n) - 1
    return dp[full_mask] != 0


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

    start_time = time.time()
    result = has_hamiltonian_path_bitmask(graph)
    end_time = time.time()
    print(result)
    print(f"Time taken: {(end_time - start_time) * 1000}  miliseconds")

main()