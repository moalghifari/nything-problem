from random import randint

import constants

class State:

    # Initialization
    def __init__(self, papanCatur=constants.EMPTY_PAPAN_CATUR, listOfBidak=[], inputBidak=[]):
        self.papanCatur = papanCatur
        self.listOfBidak = listOfBidak
        if inputBidak:
            self.generateRandomPapan(inputBidak)
        self.heuristikSamaWarna = self.hitungHeuristikSamaWarna
        self.heuristikBedaWarna = self.hitungHeuristikBedaWarna
        self.heuristikTotal = self.hitungHeuristikTotal

    # Generate Random Bidak Pada Papan Sesuai dengan Input
    def generateRandomPapan(self, inputBidak):
        for bidak in inputBidak:
            # nanti variabel bidak ini bentuknya dictionary gitu {'jenisBidak': 'xxx', 'jumlahBidak}: 10}
            # gunanya ** itu biar key pada variabel bidak disebar menjadi parameter fungsi generateRandomBidak
            self.generateRandomBidak(**bidak)

    def generateRandomBidak(self, jenisBidak, jumlahBidak):
        for i in range(jumlahBidak):
            while True:
                x = randint(0, 7)
                y = randint(0, 7)
                if (self.getElmtPapanCatur(x, y) == '.'):
                    break

            self.listOfBidak.append({
                'jenisBidak': jenisBidak, 
                'x': x,
                'y': y
            })
            self.papanCatur[y][x] = jenisBidak

    # Menghitung heuristik
    def hitungHeuristikSamaWarna(self):
        # Sekar's code
        return 999999
    def hitungHeuristikBedaWarna(self):
        # Sekar's code
        return 999999
    def hitungHeuristikTotal(self):
        # Sekar's code
        return 999999

    # Print papan
    def printPapanCatur(self):
        for baris in self.papanCatur:
            print(' '.join(baris))

    # Getter dan Setter
    def getPapanCatur(self):
        return self.papanCatur
    def getListOfBidak(self):
        return self.listOfBidak
    def getElmtPapanCatur(self, kol, bar):
        return self.papanCatur[bar][kol]
    def getElmtListOfBidak(self, idx):
        return self.listOfBidak[idx]
    def getHeuristikSamaWarna(self):
        return self.heuristikSamaWarna
    def getHeuristikBedaWarna(self):
        return self.heuristikBedaWarna
    def getHeuristikTotal(self):
        return self.heuristikTotal
    def setPapanCatur(self, papanCatur):
        self.papanCatur = papanCatur
    def setListOfBidak(self, listOfBidak):
        self.listOfBidak = listOfBidak
    def setElmtPapanCatur(self, kol, bar, bidak):
        self.papanCatur[bar][kol] = bidak
    def setElmtListOfBidak(self, idx, bidak):
        self.listOfBidak[idx] = bidak
    def setHeuristikSamaWarna(self, heuristikSamaWarna):
        self.heuristikSamaWarna = heuristikSamaWarna
    def setHeuristikBedaWarna(self, heuristikBedaWarna):
        self.heuristikBedaWarna = heuristikBedaWarna
    def setHeuristikTotal(self, heuristikTotal):
        self.heuristikTotal = heuristikTotal
    
# Test Main Program
def main():
    # papanCatur = [
    #     ['.','.','K','.','.','.','.','.'],
    #     ['.','.','.','G','.','.','.','.'],
    #     ['.','.','.','.','.','.','.','.'],
    #     ['.','.','.','.','.','.','K','.'],
    #     ['.','.','.','.','.','.','.','.'],
    #     ['.','Q','.','.','.','.','.','.'],
    #     ['.','.','.','.','.','Q','.','.'],
    #     ['.','.','.','.','.','.','.','.']
    # ]
    # listOfBidak = [
    #     {
    #         'jenisBidak' : 'K',
    #         'x' : '2',
    #         'y' : '0',
    #     },
    #     {
    #         'jenisBidak' : 'Q',
    #         'x' : '1',
    #         'y' : '5',
    #     },
    #     {
    #         'jenisBidak' : 'G',
    #         'x' : '3',
    #         'y' : '1',
    #     },
    #     {
    #         'jenisBidak' : 'K',
    #         'x' : '6',
    #         'y' : '3',
    #     },
    #     {
    #         'jenisBidak' : 'Q',
    #         'x' : '5',
    #         'y' : '6',
    #     },
    #     ]
    # state = State(papanCatur, listOfBidak)
    # print(state.getElmtListOfBidak(0))
    inputBidak = [
        {
            'jenisBidak': 'K',
            'jumlahBidak': 2
        }, {
            'jenisBidak':'B',
            'jumlahBidak': 2
        }, {
            'jenisBidak':'R',
            'jumlahBidak': 2
        }, {
            'jenisBidak':'Q',
            'jumlahBidak': 2
        }
    ]
    state = State(inputBidak=inputBidak)
    state.printPapanCatur()
    for i in state.getListOfBidak():
        print(i)

if __name__ == '__main__':
    main()
