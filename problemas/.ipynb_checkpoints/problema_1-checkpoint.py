from bio.ler_fasta import ler_fasta

def main():
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
