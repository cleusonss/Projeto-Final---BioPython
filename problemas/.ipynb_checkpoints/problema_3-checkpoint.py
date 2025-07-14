from bio.ler_fasta import ler_fasta

def main():
    organismos = ler_fasta("arquivos/Flaviviridae-genomes.fasta")

    print("Relatório de mutação na posição 1000 (A → G):\n")
    for o in organismos:
        if len(o.sequencia) < 1000:
            status = "Sequência muito curta"
        else:
            nt = o.sequencia[999]  # posição 1000 (índice 999)
            if nt.upper() == "G":
                status = "Mutação presente (A→G)"
            elif nt.upper() == "A":
                status = "Sem mutação (ainda é A)"
            else:
                status = f"Outro nucleotídeo encontrado: {nt}"

        print(f"{o.id} - {o.nome} → {status}")

if __name__ == "__main__":
    main()
