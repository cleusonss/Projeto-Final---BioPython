from bio.sequencia import Sequencia

class OrganismoFasta:
    """
    Representa um organismo biológico modelado a partir de uma entrada FASTA.

    Essa classe é inspirada na estrutura SeqRecord da biblioteca BioPython,
    e serve como um contêiner para armazenar informações básicas de uma sequência,
    como ID, descrição e o conteúdo da sequência em si (encapsulado como um objeto da classe Sequencia).

    Atributos:
        id (str): Identificador único da sequência (geralmente a primeira palavra do cabeçalho FASTA).
        nome (str): Nome descritivo do organismo ou da sequência (restante da linha do cabeçalho).
        sequencia (Sequencia): Objeto da classe Sequencia contendo a cadeia de nucleotídeos.
    """

    def __init__(self, id: str, nome: str, sequencia: str | Sequencia):
        """
        Inicializa um novo objeto OrganismoFasta.

        Se a sequência for fornecida como string, ela será automaticamente
        convertida para um objeto da classe Sequencia.

        Args:
            id (str): Identificador da sequência (ex: "NC_001477.1").
            nome (str): Nome ou descrição do organismo (ex: "Yellow fever virus").
            sequencia (str or Sequencia): Cadeia de DNA como string ou instância da classe Sequencia.

        Exemplo:
            OrganismoFasta("NC_001477.1", "Yellow fever virus", "ATGCGTA...")

        """
        self.id = id
        self.nome = nome
        self.sequencia = sequencia if isinstance(sequencia, Sequencia) else Sequencia(sequencia)

    def __repr__(self):
        """
        Retorna uma representação legível do objeto OrganismoFasta.

        Útil para inspeção em notebooks ou debug no console.

        Returns:
            str: Representação formatada do objeto.

        Exemplo:
            OrganismoFasta(id='NC_001477.1', nome='Yellow fever virus', sequencia=Sequencia("ATGC..."))
        """
        return (f"OrganismoFasta(id={self.id!r}, nome={self.nome!r}, "
                f"sequencia={self.sequencia!r})")