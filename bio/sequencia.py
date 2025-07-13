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
    
    def calcular_percentual(self, bases=None):
        seq = self.sequencia.upper()
        
        total = len(self.sequencia)
        
        total_a = seq.count("A")
        total_t = seq.count("T")
        total_c = seq.count("C")
        total_g = seq.count("G")
        
        percentuais = {}

        if total == 0:
            percentuais = {
                "A": 0,
                "T": 0,
                "C": 0,
                "G": 0
            }
        else:
            percentuais = {
                "A": total_a / total,
                "T": total_t / total,
                "C": total_c / total,
                "G": total_g / total
            }
        
        if bases is not None:
            percentuais = {base: percentuais[base] for base in bases if base in percentuais}
            
        return percentuais
            

        
