"""
Análise de sequências genômicas a partir de arquivos FASTA.

Este módulo realiza a leitura de um arquivo FASTA contendo genomas (por exemplo, de vírus da família Flaviviridae),
e exibe informações detalhadas para os três primeiros organismos do arquivo.

Para cada organismo, são exibidas:
- ID e nome
- Início da sequência nucleotídica
- Sequência complementar e complementar reversa
- RNA transcrito
- Traduções com e sem parada em códons de terminação
- Percentual de bases A e T na sequência

Requerimentos:
- O módulo `bio.ler_fasta` deve conter a função `ler_fasta`, que retorna uma lista de objetos do tipo `OrganismoFasta`.
- Cada `OrganismoFasta` deve ter os atributos `id`, `nome` e `sequencia`.
- O atributo `sequencia` deve ser uma instância da classe `Sequencia`, com os seguintes métodos:

    - `complementar()`: retorna a sequência complementar (DNA).
    - `complementar_reversa()`: retorna a sequência complementar reversa.
    - `transcrever()`: retorna a sequência de RNA transcrita.
    - `traduzir(parar=True|False)`: traduz a sequência em aminoácidos. Se `parar=True`, interrompe ao encontrar um códon de parada. Se `False`, substitui por '*'.
    - `calcular_percentual(lista_de_bases: list)`: calcula o percentual das bases desejadas na sequência.

Uso:
    Execute este script diretamente. Ele irá processar o arquivo definido na variável `caminho` dentro da função `main`.
"""
from bio.ler_fasta import ler_fasta

def exibir_resultado(organismo):
    """
    Exibe informações detalhadas de um organismo genômico.

    Parâmetros:
    ----------
    organismo : OrganismoFasta
        Objeto contendo os atributos:
            - id (str): Identificador do organismo.
            - nome (str): Nome descritivo do organismo.
            - sequencia (Sequencia): Objeto com a sequência genética e métodos associados.

    Funcionalidades:
    ---------------
    - Exibe os primeiros 50 nucleotídeos da sequência.
    - Gera e exibe:
        - Complementar (primeiros 50 nucleotídeos)
        - Complementar reversa (primeiros 50)
        - RNA transcrito (primeiros 50)
        - Tradução da sequência:
            - Com parada no primeiro códon de terminação (primeiros 100 aminoácidos)
            - Com símbolo '*' nos códons de parada (primeiros 100 aminoácidos)
    - Calcula e exibe o percentual de bases A e T.
    """
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
    """
    Função principal do script.

    Responsável por:
    ----------------
    - Definir o caminho do arquivo FASTA a ser processado.
    - Carregar os dados genômicos utilizando a função `ler_fasta`.
    - Exibir o total de organismos lidos.
    - Chamar `exibir_resultado` para os três primeiros organismos da lista.

    Observação:
    ----------
    O arquivo FASTA deve estar codificado corretamente e conter múltiplos registros no padrão FASTA.
    """
    caminho = "arquivos/Flaviviridae-genomes.fasta"
    organismos = ler_fasta(caminho)

    print(f"Total de organismos lidos: {len(organismos)}\n")

    for organismo in organismos[:3]:  # Limita saída para os 3 primeiros
        exibir_resultado(organismo)

if __name__ == "__main__":
    main()
