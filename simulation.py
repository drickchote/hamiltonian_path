import os
import time
import matplotlib.pyplot as plt
from dinamic_pd import has_hamiltonian_path_bitmask
from hamiltonian_backtracking import has_hamiltonian

def read_graph_from_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    # primeira linha: n m
    n, m = map(int, lines[0].split())

    graph = dict()

    # próximas m linhas: arestas
    for i in range(1, m + 1):
        v1, v2 = lines[i].split()

        if v1 not in graph:
            graph[v1] = set()
        if v2 not in graph:
            graph[v2] = set()

        graph[v1].add(v2)
        graph[v2].add(v1)

    return n, m, graph


def main():
    files = [
        "k10",
        "k11",
        "k12",
        "k13",
        "k14",
        "k15",
        "k16",
        "k17",
        "k18",
        "k19",
        "k20",
       
    ]
    folder = "inputs/valid_kn"

    labels = []
    times_backtracking_ms = []
    times_dp_ms = []

    for file in files:
        filename = os.path.join(folder, file)
        n, m, graph = read_graph_from_file(filename)

        labels.append(file.replace(".txt", ""))

        # --- Backtracking ---
        t0 = time.perf_counter()
        res_bt = has_hamiltonian(graph, n)
        bt_time_ms = (time.perf_counter() - t0) * 1000  # ms
        times_backtracking_ms.append(bt_time_ms)

        # --- DP (bitmask) ---
        t0 = time.perf_counter()
        res_dp = has_hamiltonian_path_bitmask(graph)
        dp_time_ms = (time.perf_counter() - t0) * 1000  # ms
        times_dp_ms.append(dp_time_ms)

        print(f"\nArquivo: {filename}")
        print(f"  Backtracking: {res_bt} | tempo = {bt_time_ms:.3f} ms")
        print(f"  DP Bitmask:   {res_dp} | tempo = {dp_time_ms:.3f} ms")

    # === Gráfico 1: Backtracking (ms) ===
    plt.figure()
    plt.bar(labels, times_backtracking_ms)
    plt.ylabel("Tempo (ms)")
    plt.title("Kn - Backtracking")
    plt.tight_layout()
    plt.show()

    # === Gráfico 2: DP Bitmask (ms) ===
    plt.figure()
    plt.bar(labels, times_dp_ms)
    plt.ylabel("Tempo (ms)")
    plt.title("Kn - DP Bitmask")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
