from bio.sequencia import Sequencia

class OrganismoFasta:
    """
    Representa um organismo biológico modelado a partir de uma entrada FASTA.

    Essa classe inspira-se na estrutura SeqRecord do Biopython e serve como um contêiner
    para armazenar informações de um organismo, incluindo um identificador único, nome
    e sua sequência biológica, que será encapsulada em um objeto da classe Sequencia.

    Atributos:
        id (str): Identificador único da sequência (geralmente derivado da linha de cabeçalho FASTA).
        nome (str): Nome descritivo do organismo ou da sequência.
        sequencia (Sequencia): Objeto da classe Sequencia contendo a cadeia de nucleotídeos ou aminoácidos.
    """
    def __init__(self, id, nome, sequencia):
        """
        Inicializa um novo objeto OrganismoFasta.
    
        Args:
            id (str): Identificador da sequência.
            nome (str): Nome do organismo.
            sequencia (str): Cadeia da sequência biológica em formato string.
        """
        self.id = id
        self.nome = nome        
        self.sequencia = sequencia if isinstance(sequencia, Sequencia) else Sequencia(sequencia)
    def __repr__(self):
        """
        Retorna uma representação legível do objeto OrganismoFasta.

        Essa representação é útil para depuração e exibição rápida no console ou em notebooks.

        Returns:
            str: String formatada contendo id, nome e representação da sequência.
        """
        return (f"OrganismoFasta(id={self.id!r}, nome={self.nome!r}, "
                f"sequencia={self.sequencia!r})")