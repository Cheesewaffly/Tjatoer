import random

nilaibidak = {"K": 0, "P": 1, "R": 5, "B": 4, "G": 3, "C": 10, "A": 9, "L": 12, "M": 1, "F": 1, "Z": 2, "N": 3, "Q": 11}

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
            [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
            [5, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 5],
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

piecepositionscores = {"N": skorkuda, "wR": skorbenteng, "bR": skorbenteng[::-1], "B": skorgajah, "wP": skorpion, "bP": skorpion[::-1]}

Skakmat = 1000
Remis = 0
Depth = 2

'''
memilih langkah random
'''


def findrandommove(validmoves):
    return validmoves[random.randint(0, len(validmoves) - 1)]


'''
memilih langkah terbaik
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
algoritma negamax alpha beta pruning
'''


def findmovenegamaxaplhabeta(gs, validmoves, depth, alpha, beta, turnmultiplier):
    global nextmove, counter
    counter += 1
    if depth == 0:
        return turnmultiplier * scoreboard(gs)

    maxscore = -Skakmat
    for move in validmoves:
        gs.makemove(move)
        nextmoves = gs.getvalidmoves()
        score = -findmovenegamaxaplhabeta(gs, nextmoves, depth - 1, -beta, -alpha, -turnmultiplier)
        if score > maxscore:
            maxscore = score
            if depth == Depth:
                nextmove = move
                print(move,":", score)
        gs.undomove()
        if maxscore > alpha:  # pruning terjadi
            alpha = maxscore
        if alpha >= beta:
            break
    return maxscore


'''
papan skor
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
                        if square[1] == "N" or "G" or "F" or "M" or "Z":
                            piecepositionscore = piecepositionscores["N"][row][col]
                        if square[1] == "B":  # buat gajah:
                            piecepositionscore = piecepositionscores["B"][row][col]
                        if square[1] == "R":  # buat gajah:
                            piecepositionscore = piecepositionscores["wR"][row][col]
                        if square[1] == "Q":  # buat ratu:
                            piecepositionscore = (piecepositionscores["wR"][row][col]) * 0.5 + (piecepositionscores["B"][row][col]) * 0.5
                        if square[1] == "A":  # buat archbishop:
                            piecepositionscore = (piecepositionscores["N"][row][col]) * 0.5 + (piecepositionscores["B"][row][col]) * 0.5
                        if square[1] == "C":  # buat chancellor:
                            piecepositionscore = (piecepositionscores["N"][row][col]) * 0.5 + (piecepositionscores["wR"][row][col]) * 0.5
                        if square[1] == "L":  # buat amazon:
                            piecepositionscore = (piecepositionscores["N"][row][col]) * (1/3) + (piecepositionscores["wR"][row][col]) * (1/3) + (piecepositionscores["B"][row][col]) * (1/3)
                    score += nilaibidak[square[1]] + piecepositionscore * 0.25
                elif square[0] == 'b':
                    if square[1] != "K":
                        if square[1] == "P":  # buat pion
                            piecepositionscore = piecepositionscores["bP"][row][col]
                        if square[1] == "N" or "G" or "F" or "M" or "Z":
                            piecepositionscore = piecepositionscores["N"][row][col]
                        if square[1] == "B":  # buat gajah:
                            piecepositionscore = piecepositionscores["B"][row][col]
                        if square[1] == "R":  # buat gajah:
                            piecepositionscore = piecepositionscores["bR"][row][col]
                        if square[1] == "Q":  # buat ratu:
                            piecepositionscore = (piecepositionscores["bR"][row][col]) * 0.5 + (piecepositionscores["B"][row][col]) * 0.5
                        if square[1] == "A":  # buat archbishop:
                            piecepositionscore = (piecepositionscores["N"][row][col]) * 0.5 + (piecepositionscores["B"][row][col]) * 0.5
                        if square[1] == "C":  # buat chancellor:
                            piecepositionscore = (piecepositionscores["N"][row][col]) * 0.5 + (piecepositionscores["bR"][row][col]) * 0.5
                        if square[1] == "L":  # buat amazon:
                            piecepositionscore = (piecepositionscores["N"][row][col]) * (1/3) + (piecepositionscores["bR"][row][col]) * (1/3) + (piecepositionscores["B"][row][col]) * (1/3)
                    score -= nilaibidak[square[1]] + piecepositionscore * 0.25
    return score
