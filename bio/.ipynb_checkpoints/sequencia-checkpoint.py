from bio.constantes import DNA_PARA_AMINOACIDO
from bio.constantes import DNA_STOP_CODONS

class Sequencia:
    """
    Classe principal do projeto para manipulação de sequências biológicas (DNA ou RNA). seguindo o documento 
    Essa classe deve ter os métodos 
    
    complementar
    complementar_reversa
    transcrever
    traduzir
    calcular_percentual
    
    Atributos:
        sequencia (str): Sequência biológica representada como string (ex: 'ATCG').
    """
    def __init__(self, sequencia):
        self.sequencia = sequencia.upper()

    def __repr__(self):
        return f'Sequencia("{self.sequencia}")'

    def __iter__(self):
        return self.sequencia

    def __str__(self):
        return self.sequencia

    def __len__(self):
        return len(self.sequencia)

    def __eq__(self, outra_sequencia):
        return str(self) == str(outra_sequencia)

    def __getitem__(self, index):
        return self.sequencia.__getitem__(
            index)
    def complementar(self):
        """
        Retorna a fita complementar de uma sequência de DNA.
    
        Substitui as bases segundo o pareamento canônico:
            A ↔ T
            C ↔ G
    
        Obs: Esta função assume que a sequência é DNA.
        
        Args:
            inplace (bool): Se True, tenta modificar a sequência original (não suportado).
    
        Returns:
            Sequencia: Nova sequência com as bases complementares.
    
        Raises:
            TypeError: Se `inplace=True`, pois a sequência é imutável.
        
        Example:
            >>> seq = Sequencia("ATCG")
            >>> tools = FerramentaSequencia(seq)
            >>> tools.complementar()
            Sequencia("TAGC")
        """
        comp_dict = str.maketrans("ATCGatcg", "TAGCtagc")
        comp = self.sequencia.translate(comp_dict)
        return Sequencia(comp)
    
    def complementar_reversa(self):
        """
        Retorna a fita complementar reversa (sentido 3' → 5') de uma sequência de DNA.
    
        Esta operação é comum em bioinformática ao modelar a fita molde ou processos como
        replicação e transcrição reversa.
    
        Args:
            inplace (bool): Se True, tenta modificar a sequência original (não suportado).
    
        Returns:
            Sequencia: Sequência complementar invertida.
    
        Raises:
            TypeError: Se `inplace=True`, pois a sequência é imutável.
    
        Example:
            >>> seq = Sequencia("ATCG")
            >>> tools = FerramentaSequencia(seq)
            >>> tools.complementar_reversa()
            Sequencia("CGAT")
        """
        complementar = self.complementar()
        reversa = complementar.sequencia[::-1]
        return Sequencia(reversa)
    
    def transcrever(self, inplace: bool = False):
        """
        Transcreve a sequência de DNA em RNA.
    
        Substitui timina (T) por uracila (U), seguindo a convenção de que a
        sequência representa a fita codificadora. A ordem da sequência é mantida.
    
        Args:
            inplace (bool): Apenas para compatibilidade com API do Biopython.
                            Como a classe Sequencia é imutável, inplace=True levanta erro.
    
        Returns:
            Sequencia: Nova instância contendo a sequência de RNA.
    
        Raises:
            TypeError: Se `inplace=True`, pois a classe Sequencia é imutável.
    
        Example:
            >>> seq = Sequencia("ATGCTT")
            >>> tools = FerramentaSequencia(seq)
            >>> tools.transcrever()
            Sequencia("AUGCUU")
        """
        transcricao_dict = str.maketrans("Tt", "Uu")
        rna = self.sequencia.translate(transcricao_dict)
        return Sequencia(rna)
    
    def traduzir(self, parar=False) -> str:
        """
        Traduz a sequência de DNA para uma cadeia de aminoácidos.

        A sequência é lida em trincas (códons), e cada códon é traduzido de acordo
        com o dicionário DNA_PARA_AMINOACIDO importado de bio/constantes.py.

        Parada da tradução: este método inclui códons de parada (TAA, TAG, TGA),
        que são convertidos para '*'.

        Returns:
            str: String contendo a cadeia de aminoácidos traduzida.

        Example:
            >>> seq = Sequencia("ATGGCTTGA")
            >>> tools = FerramentaSequencia(seq)
            >>> tools.traduzir()
            'MA*'
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
        Calcula o percentual de ocorrência de uma base na sequência.

        Args:
            base (str): A base nitrogenada desejada (ex: 'A', 'T', 'G', 'C', ou 'U').

        Returns:
            float: Percentual da base na sequência (de 0 a 100).

        Raises:
            ValueError: Se a base fornecida não for válida.
        """
        total = len(self.sequencia)
        if total == 0:
            return 0.0
    
        count = sum(self.sequencia.count(base.upper()) for base in bases)
        return round(count / total, 2)