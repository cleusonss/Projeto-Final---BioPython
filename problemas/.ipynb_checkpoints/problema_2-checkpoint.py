"""
Problema 2: Tradução de Sequências para Proteínas

Este script faz o parse de um arquivo multiFASTA, traduz cada sequência
de nucleotídeos para sua cadeia de aminoácidos e imprime o resultado.

Uso:
    python problemas/problema_2.py
"""

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bio.ler_fasta import ler_fasta

def main():
    """
    Executa a tradução de todas as sequências do FASTA para proteínas.
    """
    organismos = ler_fasta("arquivos/Flaviviridae-genomes.fasta")

    print("Tradução das sequências de nucleotídeos:\n")
    for o in organismos:
        print("=" * 60)
        print(f"ID: {o.id}")
        print(f"Nome: {o.nome}")
        proteina = o.sequencia.traduzir(parar=False)
        print(f"Proteína (início): {proteina[:100]}...")
        print("=" * 60)
        print()

if __name__ == "__main__":
    main()
