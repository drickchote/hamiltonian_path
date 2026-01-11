#!/usr/bin/env python3

# Receives a n and generate a Pn graph
 

def generate_path(n: int) -> None:
    if n < 0:
        raise ValueError("n deve ser >= 0")

    # Um caminho com n vértices tem (n-1) arestas (para n >= 1)
    m = max(0, n - 1)
    print(f"{n} {m}")

    # arestas: 0-1, 1-2, ..., (n-2)-(n-1)
    for i in range(n - 1):
        print(f"{i} {i + 1}")


def main():
    parser = argparse.ArgumentParser(
        description="Gera um grafo caminho P_n no formato: n m + lista de arestas."
    )
    parser.add_argument("n", type=int, help="Número de vértices (0..n-1)")
    args = parser.parse_args()

    generate_path(args.n)


if __name__ == "__main__":
    main()