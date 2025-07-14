from bio.ler_fasta import ler_fasta

def main():
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
