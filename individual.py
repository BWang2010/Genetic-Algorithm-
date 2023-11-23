import random
import string #All ascii characters
class Individual:
    def __init__(self, idealGenes):
        alphabet = string.ascii_lowercase + " "
        self.act_genes = ""
        self.fitness = 0
        for i in range(len(idealGenes)):
            a = random.choice(alphabet)
            self.act_genes = self.act_genes + a
            if a == idealGenes[i]:
                self.fitness = self.fitness + 1


