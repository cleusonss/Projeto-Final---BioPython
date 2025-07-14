"""
Problema 1: Análise de Composição de Nucleotídeos

Este script realiza o parse de um arquivo multiFASTA e imprime:
- O percentual de cada base (A, T, C, G)
- O conteúdo GC para cada sequência

Uso:
    python problemas/problema_1.py
"""

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bio.ler_fasta import ler_fasta

def main():
    """
    Executa a análise de composição de nucleotídeos para cada organismo do FASTA.
    """
    organismos = ler_fasta("arquivos/Flaviviridae-genomes.fasta")

    print("Análise de composição de nucleotídeos:\n")
    for o in organismos:
        print("=" * 60)
        print(f"ID: {o.id}")
        print(f"Nome: {o.nome}")
        print(f"A: {o.sequencia.calcular_percentual(['A']) * 100:.2f}%")
        print(f"T: {o.sequencia.calcular_percentual(['T']) * 100:.2f}%")
        print(f"C: {o.sequencia.calcular_percentual(['C']) * 100:.2f}%")
        print(f"G: {o.sequencia.calcular_percentual(['G']) * 100:.2f}%")
        gc = o.sequencia.calcular_percentual(['G', 'C']) * 100
        print(f"GC Content: {gc:.2f}%")
        print("=" * 60)
        print()

if __name__ == "__main__":
    main()
