import random
import string #All ascii characters
class Individual:
    def __init__(self, idealGenes):
        alphabet = string.ascii_lowercase + " "
        for i in range(len(idealGenes)):
            print(random.choice(alphabet))
