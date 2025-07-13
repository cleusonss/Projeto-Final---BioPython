from bio.ler_fasta import ler_fasta

caminho_do_arquivo = './arquivos/Flaviviridae-genomes.fasta'

organismos_do_fasta = ler_fasta(caminho_do_arquivo)

#for organismo in organismos_do_fasta:
#    print(organismo.sequencia.traduzir(True))

organismo = organismos_do_fasta[0]
seq = organismo.sequencia
print(seq.calcular_percentual(bases=["A", "T"]))
