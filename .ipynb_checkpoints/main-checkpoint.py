from bio.ler_fasta import ler_fasta

def exibir_resultado(organismo):
    print("=" * 60)
    print(f"ID: {organismo.id}")
    print(f"Nome: {organismo.nome}")
    print(f"Sequência (início): {organismo.sequencia[:50]}...\n")

    # Métodos da classe Sequencia
    print("Complementar (início):", organismo.sequencia.complementar()[:50])
    print("Complementar reversa (início):", organismo.sequencia.complementar_reversa()[:50])
    print("RNA transcrito (início):", organismo.sequencia.transcrever()[:50])
    print("Tradução (com parada):", organismo.sequencia.traduzir(parar=True)[:100])
    print("Tradução (com * nos stop codons):", organismo.sequencia.traduzir(parar=False)[:100])
    
    # Percentual A + T
    percentual = organismo.sequencia.calcular_percentual(["A", "T"]) * 100
    print(f"Percentual de A e T: {percentual:.2f}%")
    
    print("=" * 60)
    print("\n")

def main():
    caminho = "arquivos/Flaviviridae-genomes.fasta"
    organismos = ler_fasta(caminho)

    print(f"Total de organismos lidos: {len(organismos)}\n")

    for organismo in organismos[:3]:  # Limita saída para os 3 primeiros
        exibir_resultado(organismo)

if __name__ == "__main__":
    main()
