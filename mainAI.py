from hillClimbing import solveHill
import geneticalgorithm

def main() :
    print("\n▀ ▄ ░ ▀ ▄ ░     █▀▀▄ ░ ░ █░░█ ▀▀█▀▀ █░░█ ░▀░ █▀▀▄ █▀▀▀     ░ ▄ ▀ ░ ▄ ▀")
    print("░ ░ █ ░ ░ █     █░░█ ▀ ▀ █▄▄█ ░░█░░ █▀▀█ ▀█▀ █░░█ █░▀█     █ ░ ░ █ ░ ░")
    print("▄ ▀ ░ ▄ ▀ ░     ▀░░▀ ░ ░ ▄▄▄█ ░░▀░░ ▀░░▀ ▀▀▀ ▀░░▀ ▀▀▀▀     ░ ▀ ▄ ░ ▀ ▄\n")
    fname = input("Masukan Nama File Input Bidak Catur : ")
    with open(fname) as f:
        getLine = f.readlines()
    
    pawnInput = []
    for line in getLine :
        dataPawn = line.split(" ")
        if (dataPawn[0] == "WHITE"):
            if (dataPawn[1]=="KNIGHT"):
                pawnInput.append({'pawnType': 'K','pawnCount': int(dataPawn[2])})
            elif (dataPawn[1]=="BISHOP"):
                pawnInput.append({'pawnType': 'B','pawnCount': int(dataPawn[2])})
            elif (dataPawn[1]=="ROOK"):
                pawnInput.append({'pawnType': 'R','pawnCount': int(dataPawn[2])})
            else :
                pawnInput.append({'pawnType': 'Q','pawnCount': int(dataPawn[2])})
        else :
            if (dataPawn[1]=="KNIGHT"):
                pawnInput.append({'pawnType': 'k','pawnCount': int(dataPawn[2])})
            elif (dataPawn[1]=="BISHOP"):
                pawnInput.append({'pawnType': 'b','pawnCount': int(dataPawn[2])})
            elif (dataPawn[1]=="ROOK"):
                pawnInput.append({'pawnType': 'r','pawnCount': int(dataPawn[2])})
            else :
                pawnInput.append({'pawnType': 'q','pawnCount': int(dataPawn[2])})
    #print(pawnInput)

    print(" *•.¸*•.¸¤ Pilih Algoritma local search yang digunakan ¤¸.•*¸.•* "),
    print(">> 1. Hill Climbing")
    print(">> 2. Simulated Annealing")
    print(">> 3. Genetic Algorithm\n")
    str = input(">> Pilihan : ")
    while(not(int(str)==1 or int(str)==2 or int(str)==3)):
        print(">> Masukan Salah !")
        str = input(">> Pilihan : ")
    if (int(str) == 1) :
        finalState = solveHill(pawnInput)
        print ("Solusi HC")
    elif (int(str) == 2) :
        print ("Solusi SA")
        print(" *•.¸*•.¸¤ Pilih jenis temperatur yang diinginkan ¤¸.•*¸.•* "),
        print(">> 1. Constant")
        print(">> 2. Linear")
        print(">> 3. Logaritmic\n")
        inputT = input(">> Pilihan : ")
    else :
        print ("\n-- Solusi GA --")
        result = geneticalgorithm.main(pawnInput)
        print('Total Generasi: {}'.format(result['generation']))
        print('Populasi: {}'.format(result['population']))
        print('Mutation Rate: {}'.format(result['mutationRate']))
        finalState = result['state']

    finalState.printChessBoard()
    print(finalState.calcSameColorHeuristic(), finalState.calcDiffColorHeuristic())
if __name__ == '__main__' :
    main()