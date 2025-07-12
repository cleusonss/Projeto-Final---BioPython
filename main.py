from bio.ler_fasta import ler_fasta

caminho_do_arquivo = './arquivos/Flaviviridae-genomes.fasta'

organismos_do_fasta = ler_fasta(caminho_do_arquivo)

print('Os organismos são:')
for organismo in organismos_do_fasta:
    print(organismo.id)

