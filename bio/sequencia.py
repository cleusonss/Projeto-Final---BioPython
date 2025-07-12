from bio.constantes import DNA_PARA_AMINOACIDO
from bio.constantes import DNA_STOP_CODONS
class Sequencia:

    def __init__(self, sequencia):
        self.sequencia = sequencia

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
        return self.sequencia.__getitem__(index)
    
    def calcular_sequencia(self):
        return len(self.sequencia)
    
    def complementar(self, inplace: bool = False):
        comp_dict = str.maketrans("ATCGatcg", "TAGCtagc")
        comp = self.sequencia.translate(comp_dict)
        return Sequencia(comp)
    
    def complementar_reversa(self):
        comp = self.complementar().sequencia[::-1]
        return Sequencia(comp)

    def transcrever(self):
        trans_dict = str.maketrans("Tt", "Uu")
        trans = self.sequencia.translate(trans_dict)
        return Sequencia(trans)
    
    def traduzir(self, parar):
        proteina = []
        seq = self.sequencia
        
        for i in range(0, len(seq) - 2 , 3):
            codon = seq[i:i+3]

            if codon in DNA_STOP_CODONS:
                aa = '*'
            else:
                aa = DNA_PARA_AMINOACIDO.get(codon, "X")

            proteina.append(aa)

            if parar and  aa == '*':
                break

        return "".join(proteina)
    
    def calcular_percentual(self):
        total = self.sequencia.len
        total_a = self.sequencia.upper().count("A")
        total_t = self.sequencia.upper().count("T")
        total_c = self.sequencia.upper().count("C")
        total_g = self.sequencia.upper().count("G")

        return [total, total_a, total_t, total_c, total_g]

        
