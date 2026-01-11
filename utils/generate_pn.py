#!/usr/bin/env python3
import argparse
import random

# Recebe n e gera um grafo caminho Pn

def generate_path(n: int) -> None:
    if n < 0:
        raise ValueError("n deve ser >= 0")

    # Um caminho com n vértices tem (n - 1) arestas
    m = max(0, n - 1)
    print(f"{n} {m}")

    # gera as arestas do caminho
    edges = []
    for i in range(n - 1):
        edges.append((i, i + 1))

    # embaralha as arestas (exceto a primeira linha)
    random.shuffle(edges)

    # imprime
    for u, v in edges:
        print(f"{u} {v}")


def main():
    parser = argparse.ArgumentParser(
        description="Gera um grafo caminho P_n no formato: n m + lista de arestas (arestas embaralhadas)."
    )
    parser.add_argument("n", type=int, help="Número de vértices (0..n-1)")
    args = parser.parse_args()

    generate_path(args.n)


if __name__ == "__main__":
    main()
