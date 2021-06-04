import random

nilaibidak = {"K": 0, "P": 100, "R": 500, "B": 325, "G": 250, "I": 925, "A": 825, "L": 1400, "M": 400, "F": 1250,
              "O": 1200, "N": 300, "Q": 950,
              "J": 775, "C": 875, "H": 450, "D": 900, "E": 1075, "S": 150, "T": 150, "U": 175, "V": 840, "W": 165,
              "X": 610, "Y": 175, "Z": 315}

skorkuda = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
    [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 2, 1],
    [1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

skorgajah = [
    [8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8],
    [7, 8, 7, 6, 5, 4, 3, 2, 2, 3, 4, 5, 6, 7, 8, 7],
    [6, 7, 8, 7, 6, 5, 4, 3, 3, 4, 5, 6, 7, 8, 7, 6],
    [5, 6, 7, 8, 7, 6, 5, 4, 4, 5, 6, 7, 8, 7, 6, 5],
    [4, 5, 6, 7, 8, 7, 6, 5, 5, 6, 7, 8, 7, 6, 5, 4],
    [3, 4, 5, 6, 7, 8, 7, 6, 6, 7, 8, 7, 6, 5, 4, 3],
    [2, 3, 4, 5, 6, 7, 8, 7, 7, 8, 7, 6, 5, 4, 3, 2],
    [1, 2, 3, 4, 5, 6, 7, 8, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 8, 7, 6, 5, 4, 3, 2, 1],
    [2, 3, 4, 5, 6, 7, 8, 7, 7, 8, 7, 6, 5, 4, 3, 2],
    [3, 4, 5, 6, 7, 8, 7, 6, 6, 7, 8, 7, 6, 5, 4, 3],
    [4, 5, 6, 7, 8, 7, 6, 5, 5, 6, 7, 8, 7, 6, 5, 4],
    [5, 6, 7, 8, 7, 6, 5, 4, 4, 5, 6, 7, 8, 7, 6, 5],
    [6, 7, 8, 7, 6, 5, 4, 3, 3, 4, 5, 6, 7, 8, 7, 6],
    [7, 8, 7, 6, 5, 4, 3, 2, 2, 3, 4, 5, 6, 7, 8, 7],
    [8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8]]

skorbenteng = [
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
    [5, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 5],
    [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
    [5, 5, 5, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 5, 5, 5],
    [4, 4, 5, 5, 5, 8, 8, 8, 8, 8, 8, 5, 5, 5, 4, 4],
    [4, 4, 4, 4, 5, 5, 5, 8, 8, 5, 5, 5, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4],
    [3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3],
    [3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3],
    [2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 3, 3, 3, 2, 2],
    [2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2],
    [2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2],
    [2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1],
    [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

skorpion = [
    [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
    [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
    [6, 6, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 6, 6],
    [5, 5, 6, 6, 7, 7, 8, 8, 8, 8, 7, 7, 6, 6, 5, 5],
    [5, 5, 6, 6, 7, 7, 8, 8, 8, 8, 7, 7, 6, 6, 5, 5],
    [5, 5, 6, 6, 7, 7, 7, 8, 8, 7, 7, 7, 6, 6, 5, 5],
    [2, 2, 3, 3, 4, 5, 5, 6, 6, 5, 5, 4, 3, 3, 2, 2],
    [2, 2, 3, 3, 4, 5, 5, 6, 6, 5, 5, 4, 3, 3, 2, 2],
    [1, 1, 2, 2, 3, 4, 4, 5, 5, 4, 4, 3, 2, 2, 1, 1],
    [1, 1, 2, 2, 3, 4, 4, 5, 5, 4, 4, 3, 2, 2, 1, 1],
    [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1],
    [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

piecepositionscores = {"N": skorkuda, "wR": skorbenteng, "bR": skorbenteng[::-1], "B": skorgajah, "wP": skorpion,
                       "bP": skorpion[::-1]}

Skakmat = 1000
Remis = 0
Depth = 0

'''
memilih langkah random (chooses a random move)
'''


def findrandommove(validmoves):
    return validmoves[random.randint(0, len(validmoves) - 1)]


'''
memilih langkah terbaik (chooses the 'best' move)
'''


def findbestmove(gs, validmoves, returnqueue):
    global nextmove, counter
    nextmove = None
    random.shuffle(validmoves)
    counter = 0
    findmovenegamaxaplhabeta(gs, validmoves, Depth, -Skakmat, Skakmat, 1 if gs.whitetomove else -1)
    print(counter, "langkah terevaluasi")
    returnqueue.put(nextmove)
    return nextmove


'''
algoritma negamax alpha beta pruning (negamax alpha beta pruning algorithm)
'''


def findmovenegamaxaplhabeta(gs, validmoves, depth, alpha, beta, turnmultiplier):
    global nextmove, counter
    counter += 1
    if depth == 0:
        return turnmultiplier*scoreboard(gs)

    maxscore = -Skakmat
    for move in validmoves:
        gs.makemove(move)
        nextmoves = gs.getvalidmoves()
        score = -findmovenegamaxaplhabeta(gs, nextmoves, depth - 1, -beta, -alpha, -turnmultiplier)
        if score > maxscore:
            maxscore = score
            if depth == Depth:
                nextmove = move
                print(move, ":", score)
        gs.undomove()
        if maxscore > alpha:  # pruning terjadi
            alpha = maxscore
        if alpha >= beta:
            break
    return maxscore


'''
papan skor (scoe board)
'''


def scoreboard(gs):
    if gs.checkmate:
        if gs.whitetomove:
            return -Skakmat  # hitam menang
        else:
            return Skakmat
    if gs.stalemate:
        return Remis

    score = 0
    for row in range(len(gs.board)):
        for col in range(len(gs.board[row])):
            square = gs.board[row][col]
            if square != "--":
                # skor secara posisi
                piecepositionscore = 0
                if square[0] == 'w':
                    if square[1] != "K":
                        if square[1] == "P":  # buat pion
                            piecepositionscore = piecepositionscores["wP"][row][col]
                        if square[1] == "N" or "G" or "H" or "U" or "Y" or "Z":
                            piecepositionscore = piecepositionscores["N"][row][col]
                        if square[1] == "M":
                            piecepositionscore = piecepositionscores["N"][row][col]*0.5 + \
                                                 piecepositionscores["wP"][row][col]*0.5
                        if square[1] == "B" or "X":  # buat gajah dan xiphodon
                            piecepositionscore = piecepositionscores["B"][row][col]
                        if square[1] == "R" or "V":  # buat benteng dan viscount
                            piecepositionscore = piecepositionscores["wR"][row][col]
                        if square[1] == "S":  # buat shrook
                            piecepositionscore = piecepositionscores["wR"][row][col]*0.5 + \
                                                 piecepositionscores["wP"][row][col]*0.5
                        if square[1] == "T":  # buat thalia
                            piecepositionscore = piecepositionscores["B"][row][col]*0.5 + \
                                                 piecepositionscores["wP"][row][col]*0.5
                        if square[1] == "W":  # buat warrior
                            piecepositionscore = piecepositionscores["N"][row][col]*0.5 + \
                                                 piecepositionscores["wP"][row][col]*0.5
                        if square[1] == "Q":  # buat ratu
                            piecepositionscore = (piecepositionscores["wR"][row][col])*0.5 + (
                                piecepositionscores["B"][row][col])*0.5
                        if square[1] == "A" or "J":  # buat archbishop
                            piecepositionscore = (piecepositionscores["N"][row][col])*0.5 + (
                                piecepositionscores["B"][row][col])*0.5
                        if square[1] == "I" or "C":  # buat chancellor
                            piecepositionscore = (piecepositionscores["N"][row][col])*0.5 + (
                                piecepositionscores["wR"][row][col])*0.5
                        if square[1] == "F" or "O":  # buat ferz dan man
                            piecepositionscore = (piecepositionscores["N"][row][col])*(1/3) + (
                                piecepositionscores["wR"][row][col])*(1/3) + (piecepositionscores["B"][row][col])*(1/3)
                        if square[1] == "D":  # buat duchess
                            piecepositionscore = (piecepositionscores["N"][row][col])*(2/3) + (
                                piecepositionscores["B"][row][col])*(1/3)
                        if square[1] == "E":  # buat esquire
                            piecepositionscore = (piecepositionscores["N"][row][col])*(2/3) + (
                                piecepositionscores["wR"][row][col])*(1/3)
                        if square[1] == "L":  # buat lance
                            piecepositionscore = (piecepositionscores["N"][row][col])*0.5 + (
                                piecepositionscores["wR"][row][col])*0.25 + (piecepositionscores["B"][row][col])*0.25
                    score += nilaibidak[square[1]]*0.01 + piecepositionscore*0.25
                elif square[0] == 'b':
                    if square[1] != "K":
                        if square[1] == "P":  # buat pion
                            piecepositionscore = piecepositionscores["bP"][row][col]
                        if square[1] == "N" or "G" or "H" or "U" or "Y" or "Z":  # buat kuda, gajah, hawk, upasaka, yishi dan zebra
                            piecepositionscore = piecepositionscores["N"][row][col]
                        if square[1] == "M":  # buat man
                            piecepositionscore = piecepositionscores["N"][row][col]*0.5 + \
                                                 piecepositionscores["bP"][row][col]*0.5
                        if square[1] == "B" or "X":  # buat gajah dan xiphodon
                            piecepositionscore = piecepositionscores["B"][row][col]
                        if square[1] == "R" or "V":  # buat benteng dan viscount
                            piecepositionscore = piecepositionscores["bR"][row][col]
                        if square[1] == "S":  # buat shrook
                            piecepositionscore = piecepositionscores["bR"][row][col]*0.5 + \
                                                 piecepositionscores["bP"][row][col]*0.5
                        if square[1] == "T":  # buat thalia
                            piecepositionscore = piecepositionscores["B"][row][col]*0.5 + \
                                                 piecepositionscores["bP"][row][col]*0.5
                        if square[1] == "W":  # buat warrior
                            piecepositionscore = piecepositionscores["N"][row][col]*0.5 + \
                                                 piecepositionscores["bP"][row][col]*0.5
                        if square[1] == "Q":  # buat ratu
                            piecepositionscore = (piecepositionscores["bR"][row][col])*0.5 + (
                                piecepositionscores["B"][row][col])*0.5
                        if square[1] == "A" or "J":  # buat archbishop
                            piecepositionscore = (piecepositionscores["N"][row][col])*0.5 + (
                                piecepositionscores["B"][row][col])*0.5
                        if square[1] == "I" or "C":  # buat chancellor
                            piecepositionscore = (piecepositionscores["N"][row][col])*0.5 + (
                                piecepositionscores["bR"][row][col])*0.5
                        if square[1] == "F" or "O":  # buat ferz dan man
                            piecepositionscore = (piecepositionscores["N"][row][col])*(1/3) + (
                                piecepositionscores["bR"][row][col])*(1/3) + (piecepositionscores["B"][row][col])*(1/3)
                        if square[1] == "D":  # buat duchess
                            piecepositionscore = (piecepositionscores["N"][row][col])*(2/3) + (
                                piecepositionscores["B"][row][col])*(1/3)
                        if square[1] == "E":  # buat esquire
                            piecepositionscore = (piecepositionscores["N"][row][col])*(2/3) + (
                                piecepositionscores["bR"][row][col])*(1/3)
                        if square[1] == "L":  # buat lance
                            piecepositionscore = (piecepositionscores["N"][row][col])*0.5 + (
                                piecepositionscores["bR"][row][col])*0.25 + (piecepositionscores["B"][row][col])*0.25
                    score -= nilaibidak[square[1]]*0.01 + piecepositionscore*0.25
    return score
