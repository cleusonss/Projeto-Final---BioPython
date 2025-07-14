from bio.constantes import DNA_PARA_AMINOACIDO, DNA_STOP_CODONS

class Sequencia:
    """
    Classe principal do projeto para manipulação de sequências biológicas (DNA ou RNA).

    Atributos:
        sequencia (str): Cadeia de nucleotídeos representada como string (ex: 'ATCG').

    Métodos:
        - complementar(): Retorna a fita complementar (A↔T, C↔G).
        - complementar_reversa(): Retorna a fita complementar reversa (3' → 5').
        - transcrever(): Transforma DNA em RNA substituindo T por U.
        - traduzir(parar=False): Traduz a sequência para proteína (usa códons).
        - calcular_percentual(bases): Calcula percentual de bases informadas.
    """

    def __init__(self, sequencia):
        self.sequencia = sequencia.upper()

    def __repr__(self):
        return f'Sequencia("{self.sequencia}")'

    def __str__(self):
        return self.sequencia

    def __iter__(self):
        return iter(self.sequencia)

    def __len__(self):
        return len(self.sequencia)

    def __eq__(self, outra_sequencia):
        return str(self) == str(outra_sequencia)

    def __getitem__(self, index):
        return self.sequencia[index]

    def complementar(self):
        """
        Gera a fita complementar da sequência atual (assumindo que é DNA).

        Substituições feitas:
            A ↔ T
            C ↔ G

        Returns:
            Sequencia: Nova instância com a sequência complementar.

        Exemplo:
            Sequencia("ATCG").complementar() -> Sequencia("TAGC")
        """
        comp_dict = str.maketrans("ATCGatcg", "TAGCtagc")
        comp = self.sequencia.translate(comp_dict)
        return Sequencia(comp)

    def complementar_reversa(self):
        """
        Gera a fita complementar reversa (sentido 3' → 5') da sequência de DNA.

        Combina o resultado de .complementar() com inversão da sequência.

        Returns:
            Sequencia: Complementar reversa da sequência original.

        Exemplo:
            Sequencia("ATCG").complementar_reversa() -> Sequencia("CGAT")
        """
        complementar = self.complementar()
        reversa = complementar.sequencia[::-1]
        return Sequencia(reversa)

    def transcrever(self, inplace: bool = False):
        """
        Transcreve uma sequência de DNA para RNA, substituindo T por U.

        Args:
            inplace (bool): Compatibilidade com BioPython (não usado; sempre retorna nova instância).

        Returns:
            Sequencia: Nova sequência transcrita como RNA.

        Exemplo:
            Sequencia("ATGCTT").transcrever() -> Sequencia("AUGCUU")
        """
        transcricao_dict = str.maketrans("Tt", "Uu")
        rna = self.sequencia.translate(transcricao_dict)
        return Sequencia(rna)

    def traduzir(self, parar=False) -> str:
        """
        Traduz a sequência de DNA para uma cadeia de aminoácidos (proteína).

        A leitura é feita em trincas (códons), e os códons são convertidos
        usando o dicionário DNA_PARA_AMINOACIDO.

        Regras:
            - Códons de parada (TAA, TAG, TGA) são convertidos para '*'.
            - Códons indefinidos (com bases ambíguas) viram 'X'.
            - Se parar=True, a tradução para no primeiro '*'.

        Args:
            parar (bool): Se True, para no primeiro códon de parada.

        Returns:
            str: Sequência de aminoácidos traduzida.

        Exemplo:
            Sequencia("ATGGCTTGA").traduzir() -> "MA*"
            Sequencia("ATGGCTTGA").traduzir(parar=True) -> "MA"
        """
        proteina = []
        seq = self.sequencia.upper()

        for i in range(0, len(seq) - 2, 3):
            codon = seq[i:i+3]
            aa = DNA_PARA_AMINOACIDO.get(codon, "X")
            proteina.append(aa)

            if parar and aa == "*":
                break

        return "".join(proteina)

    def calcular_percentual(self, bases: list[str]) -> float:
        """
        Calcula o percentual de ocorrência de uma ou mais bases na sequência.

        Args:
            bases (list[str]): Lista com as bases (ex: ['A'], ['C', 'G'])

        Returns:
            float: Percentual entre 0 e 1 das bases somadas na sequência.

        Exemplo:
            Sequencia("ATCGAAA").calcular_percentual(["A"]) -> 0.5
            Sequencia("ATCGCC").calcular_percentual(["C", "G"]) -> 0.5
        """
        total = len(self.sequencia)
        if total == 0:
            return 0.0

        count = sum(self.sequencia.count(base.upper()) for base in bases)
        return round(count / total, 2)
