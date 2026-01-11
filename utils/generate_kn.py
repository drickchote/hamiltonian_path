#!/usr/bin/env python3

# Receives a n and generate the Kn graph
 

import argparse
import random


def generate_kn(n: int) -> None:
    if n < 0:
        raise ValueError("n deve ser >= 0")

    m = n * (n - 1) // 2
    print(f"{n} {m}")

    # gera todas as arestas
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append((i, j))

    # embaralha as arestas
    random.shuffle(edges)

    # imprime após embaralhar
    for i, j in edges:
        print(f"{i} {j}")


def main():
    parser = argparse.ArgumentParser(
        description="Gera um grafo completo K_n no formato: n m + lista de arestas (arestas embaralhadas)."
    )
    parser.add_argument("n", type=int, help="Número de vértices (0..n-1)")
    args = parser.parse_args()

    generate_kn(args.n)


if __name__ == "__main__":
    main()
