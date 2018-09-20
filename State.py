class State:
    # Initialization
    def __init__(self, papanCatur, listOfBidak):
        self.papanCatur = papanCatur
        self.listOfBidak = listOfBidak
        self.heuristikSamaWarna = self.hitungHeuristikSamaWarna
        self.heuristikBedaWarna = self.hitungHeuristikBedaWarna
        self.heuristikTotal = self.hitungHeuristikTotal
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
    def getHeuristikTotal(self, heuristikTotal):
        self.heuristikTotal = heuristikTotal
    
def main():
    papanCatur = [
        ['.','.','K','.','.','.','.','.'],
        ['.','.','.','G','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','K','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','Q','.','.','.','.','.','.'],
        ['.','.','.','.','.','Q','.','.'],
        ['.','.','.','.','.','.','.','.']
    ]
    listOfBidak = [
        {
            'jenisBidak' : 'K',
            'x' : '2',
            'y' : '0',
        },
        {
            'jenisBidak' : 'Q',
            'x' : '1',
            'y' : '5',
        },
        {
            'jenisBidak' : 'G',
            'x' : '3',
            'y' : '1',
        },
        {
            'jenisBidak' : 'K',
            'x' : '6',
            'y' : '3',
        },
        {
            'jenisBidak' : 'Q',
            'x' : '5',
            'y' : '6',
        },
        ]
    state = State(papanCatur, listOfBidak)
    print(state.getElmtListOfBidak(0))

if __name__ == '__main__':
    main()
