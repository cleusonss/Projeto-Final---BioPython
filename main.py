from bio.ler_fasta import ler_fasta

caminho_do_arquivo = './arquivos/Flaviviridae-genomes.fasta'

organismos_do_fasta = ler_fasta(caminho_do_arquivo)

for organismo in organismos_do_fasta:
    print(organismo.nome, ':', organismo.sequencia.calcular_sequencia())

