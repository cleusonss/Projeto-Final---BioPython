"""
Problema 3: Identificação de Mutação em Genomas Virais

Este script verifica se existe uma mutação específica (A → G)
na posição 1000 das sequências de um arquivo multiFASTA.

Se a base na posição 1000 for 'G', considera-se que a mutação está presente.

Uso:
    python problemas/problema_3.py
"""

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bio.ler_fasta import ler_fasta

def main():
    """
    Verifica a presença da mutação A → G na posição 1000 das sequências.
    Gera um relatório com os organismos que têm ou não a mutação.
    """
    organismos = ler_fasta("arquivos/Flaviviridae-genomes.fasta")

    print("Relatório de mutação na posição 1000 (A → G):\n")
    for o in organismos:
        if len(o.sequencia) < 1000:
            status = "Sequência muito curta"
        else:
            nt = o.sequencia[999]  # posição 1000 = índice 999
            if nt.upper() == "G":
                status = "Mutação presente (A→G)"
            elif nt.upper() == "A":
                status = "Sem mutação (ainda é A)"
            else:
                status = f"Outro nucleotídeo encontrado: {nt}"

        print(f"{o.id} - {o.nome} → {status}")

if __name__ == "__main__":
    main()
