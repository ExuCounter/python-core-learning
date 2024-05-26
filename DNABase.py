class DNABase:
    def __init__(self, nucleotide):
        self.set_nucleotide(nucleotide)

    def set_nucleotide(self, nucleotide):
        nucleotideTuples = [("A", "adenine"), ("C", "cytosine"), ("G", "guanine"), ("T", "thymine")]

        if not isinstance(nucleotide, str):
            return TypeError("Specified nucleotide is not string")

        for nucleotideTuple in nucleotideTuples:
            short_name, long_name = nucleotideTuple

            if nucleotide.upper() == short_name or nucleotide.lower() == long_name:
                self._nucleotide = long_name
                return self.get_nucleotide()

        return TypeError("Specified nucleotide does not exist")

    def get_nucleotide(self):
        return self._nucleotide

    @property
    def base(self):
        return self.get_nucleotide()

    def __repr__(self):
        return f"DNABase(nucleotide={self.base})"


dna = DNABase("a")
print(dna.base)
print(dna.set_nucleotide("cytozine"))
print(dna.set_nucleotide("cytosine"))
print(dna.set_nucleotide("g"))
print(dna.base)
