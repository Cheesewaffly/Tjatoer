"""
File ini bertanggung jawab untuk menampung semua informasi permainan dan juga langkah-langkah valid dan mencatat langkah (this file is responsible for all the information in the game)
"""


class GameState:
    def __init__(self):
        # papan caturnya len(self.board[0])xlen(self.board[0]) daftar 2 dimensional, setiap elemen daftar mempunyai 2 karakter, karakter pertama warnanya, kedua tipenya (the board is len(self.board[0])xlen(self.board[0]), every element has 2 characters, the wirst one is the color, the second is the type)
        self.board = [
            ["bY", "bU", "bQ", "bX", "bV", "bO", "bF", "bL", "bK", "bE", "bD", "bV", "bX", "bQ", "bU", "bY"],
            ["bR", "bC", "bG", "bJ", "bB", "bM", "bM", "bM", "bM", "bM", "bM", "bB", "bJ", "bG", "bC", "bR"],
            ["bZ", "bI", "bN", "bA", "bH", "bS", "bT", "bW", "bW", "bT", "bS", "bH", "bA", "bN", "bI", "bZ"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wZ", "wI", "wN", "wA", "wH", "wS", "wT", "wW", "wW", "wT", "wS", "wH", "wA", "wN", "wI", "wZ"],
            ["wR", "wC", "wG", "wJ", "wB", "wM", "wM", "wM", "wM", "wM", "wM", "wB", "wJ", "wG", "wC", "wR"],
            ["wY", "wU", "wQ", "wX", "wV", "wO", "wF", "wL", "wK", "wE", "wD", "wV", "wX", "wQ", "wU", "wY"]]
        self.movefunction = {'P': self.getpawnmoves, 'R': self.getrookmoves, 'N': self.getknightmoves,
                             'B': self.getbishopmoves, 'Q': self.getqueenmoves, 'K': self.getkingmoves,
                             'F': self.getferzmoves, 'M': self.getmanmoves, 'G': self.getgajahmoves,
                             'L': self.getlancemoves, 'A': self.getarchbishopmoves, 'I': self.getimammoves,
                             'O': self.getoknhamoves, 'J': self.getjestermoves, 'C': self.getchariotmoves,
                             'D': self.getduchessmoves, 'E': self.getesquiremoves, 'H': self.gethawkmoves,
                             'X': self.getxiphodonmoves, 'V': self.getviscountmoves, 'S': self.getshrookmoves,
                             'T': self.getthaliamoves, 'U': self.getupasakamoves, 'W': self.getwarriormoves,
                             'Y': self.getyishimoves, 'Z': self.getzebramoves}
        self.whitetomove = True
        self.movelog = []
        self.whitekinglocation = (15, 8)
        self.blackkinglocation = (0, 8)
        self.checkmate = False
        self.stalemate = False

    '''
    mengambil langkah sebagai parameter kemudian mengeksekusinya (takes a move as a parameter and makes that move, this is used to check for checks)
    '''

    def makemove(self, move):
        piecepromote = {'P': 'Q', 'M': 'L', 'S': 'R', 'T': 'B', 'W': 'N'}
        self.board[move.startrow][move.startcol] = "--"
        self.board[move.endrow][move.endcol] = move.piecemoved
        self.movelog.append(move)  # mencatat langkah biar bisa diundo (records the move so it can be undone)
        self.whitetomove = not self.whitetomove  # gantian giliran (changes the turn)
        if move.piecemoved == 'wK':
            self.whitekinglocation = (move.endrow, move.endcol)
        elif move.piecemoved == 'bK':
            self.blackkinglocation = (move.endrow, move.endcol)

        # promosi (promotion)
        if move.ispromotion:
            self.board[move.endrow][move.endcol] = move.piecemoved[0] + piecepromote[move.piecemoved[1]]

    '''
    undo lngkah terakhir (undo the last move)
    '''

    def undomove(self):
        if len(self.movelog) != 0:  # biar ada yg bisa diundo
            move = self.movelog.pop()
            self.board[move.startrow][move.startcol] = move.piecemoved
            self.board[move.endrow][move.endcol] = move.piececaptured
            self.whitetomove = not self.whitetomove
            if move.piecemoved == 'wK':
                self.whitekinglocation = (move.startrow, move.startcol)
            elif move.piecemoved == 'bK':
                self.blackkinglocation = (move.startrow, move.startcol)
            self.checkmate = False
            self.stalemate = False

    '''
    semua langkah termasuk skak (all moves including checks)
    '''

    def getvalidmoves(self):
        # 1. membuat semua langkah yang mungkin (makes all possible moves)
        moves = self.getallpossibledmoves()
        # 2. membuat semua langkah lawan yang mungkin (makes all possible opponent moves)
        for i in range(len(moves) - 1, -1, -1):
            self.makemove(moves[i])
            # 3. cek kallo raja kita lg diserang (checks if the king is in danger)
            self.whitetomove = not self.whitetomove
            if self.incheck():
                moves.remove(moves[i])  # 4. kalau ya maka tdk valid (if the king is in danger then the move is invalid)
            self.whitetomove = not self.whitetomove
            self.undomove()
        if len(moves) == 0:
            # antara skakmat atau stalemate (determines whether its checkmate or stalemate)
            if self.incheck():
                self.checkmate = True
            else:
                self.stalemate = True
        else:
            self.checkmate = False
            self.stalemate = False
        return moves

    '''
    tau kalau lagi skak (checks for checks)
    '''

    def incheck(self):
        if self.whitetomove:
            return self.squareunderattack(self.whitekinglocation[0], self.whitekinglocation[1])
        else:
            return self.squareunderattack(self.blackkinglocation[0], self.blackkinglocation[1])

    '''
    petak yg lagi diserang (squares that are under attack)
    '''

    def squareunderattack(self, r, c):
        self.whitetomove = not self.whitetomove
        oppmoves = self.getallpossibledmoves()
        self.whitetomove = not self.whitetomove
        for move in oppmoves:
            if move.endrow == r and move.endcol == c:  # petak yg sedang diserang
                return True
        return False

    '''
    semua langkah tidak termasuk skak (all moves not including checks)
    '''

    def getallpossibledmoves(self):
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn == 'w' and self.whitetomove) or (turn == 'b' and not self.whitetomove):
                    bidak = self.board[r][c][1]
                    self.movefunction[bidak](r, c, moves)  # berdasarkan tipe bidak
        return moves

    '''
    semua langkah pion lalu memasukan ke daftar (gets all the pawn moves and adds those to the valid moves list to be filtered)
    '''

    def getpawnmoves(self, r, c, moves):
        if self.whitetomove:  # pion putih (white pawn)
            if self.board[r - 1][c] == "--":  # maju 1 petak (move 1 squre forward)
                moves.append(Move((r, c), (r - 1, c), self.board))
                for n in range(2, 5):
                    if r == 12 and self.board[r - n][c] == "--":  # maju 4 petak di langkah pertama (moves upto 4 squares forward in the first move)
                        moves.append(Move((r, c), (r - n, c), self.board))
            if c - 1 >= 0:  # makan ke kiri (captures to the left)
                if self.board[r - 1][c - 1][0] == 'b':  # ada bidak lawan (opponents piece that is blocking)
                    moves.append(Move((r, c), (r - 1, c - 1), self.board))
            if c + 1 < len(self.board[0]):  # makan ke kanan (captures to the right)
                if self.board[r - 1][c + 1][0] == 'b':  # ada bidak lawan (opponents piece that is blocking)
                    moves.append(Move((r, c), (r - 1, c + 1), self.board))

        else:  # pion hitam
            if self.board[r + 1][c] == "--":  # maju 1 petak (move 1 squre forward)
                moves.append(Move((r, c), (r + 1, c), self.board))
                for n in range(2, 5):
                    if r == 3 and self.board[r + n][c] == "--":  # maju 4 petak di langkah pertama (moves upto 4 squares forward in the first move)
                        moves.append(Move((r, c), (r + n, c), self.board))
            if c - 1 >= 0:  # makan ke kiri (captures to the left)
                if self.board[r + 1][c - 1][0] == 'w':  # ada bidak lawan (opponents piece that is blocking)
                    moves.append(Move((r, c), (r + 1, c - 1), self.board))
            if c + 1 < len(self.board[0]):  # makan ke kanan (captures to the right)
                if self.board[r + 1][c + 1][0] == 'w':  # ada bidak lawan (opponents piece that is blocking)
                    moves.append(Move((r, c), (r + 1, c + 1), self.board))

    '''
    semua langkah benteng lalu memasukan ke daftar (gets all the rook moves and adds those to the valid moves list to be filtered)
    '''

    def getrookmoves(self, r, c, moves):
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
        warnamusuh = "b" if self.whitetomove else "w"
        for d in directions:
            for i in range(1, len(self.board[0])):
                endrow = r + d[0] * i
                endcol = c + d[1] * i
                if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece == "--":  # horizontal bebas (moves freely horizontally)
                        moves.append(Move((r, c), (endrow, endcol), self.board))
                    elif endpiece[0] == warnamusuh:  # ketutupan musuh (blocked by enemy piece)
                        moves.append(Move((r, c), (endrow, endcol), self.board))
                        break
                    else:  # bidak sendiri (blocked by own piece)
                        break
                else:  # diluar papan (out of the board)
                    break

    '''
    semua langkah kuda lalu memasukan ke daftar (gets all the knight moves and adds those to the valid moves list to be filtered)
    '''

    def getknightmoves(self, r, c, moves):
        langkahkuda = ((-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (-1, -2), (1, 2), (1, -2))
        warnateman = "w" if self.whitetomove else "b"
        for m in langkahkuda:
            endrow = r + m[0]
            endcol = c + m[1]
            if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                endpiece = self.board[endrow][endcol]
                if endpiece[0] != warnateman:
                    moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    semua langkah gajah lalu memasukan ke daftar (gets all the bishop moves and adds those to the valid moves list to be filtered)
    '''

    def getbishopmoves(self, r, c, moves):
        directions = ((-1, -1), (1, -1), (1, 1), (-1, 1))
        warnamusuh = "b" if self.whitetomove else "w"
        for d in directions:
            for i in range(1, len(self.board[0])):
                endrow = r + d[0] * i
                endcol = c + d[1] * i
                if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece == "--":  # diagonal bebas (moves freely diagonally)
                        moves.append(Move((r, c), (endrow, endcol), self.board))
                    elif endpiece[0] == warnamusuh:  # ketutupan musuh (blocked by enemy piece)
                        moves.append(Move((r, c), (endrow, endcol), self.board))
                        break
                    else:  # bidak sendiri (blocked by own piece)
                        break
                else:  # diluar papan (out of the board)
                    break

    '''
    semua langkah mentri lalu memasukan ke daftar (gets all the queen moves and adds those to the valid moves list to be filtered)
    '''

    def getqueenmoves(self, r, c, moves):
        self.getbishopmoves(r, c, moves)
        self.getrookmoves(r, c, moves)

    '''
    semua langkah hawk lalu memasukan ke daftar (gets all the hawk moves and adds those to the valid moves list to be filtered)
    '''

    def gethawkmoves(self, r, c, moves):
        self.getknightmoves(r, c, moves)
        self.getgajahmoves(r, c, moves)

    '''
    semua langkah raja lalu memasukan ke daftar (gets all the king moves and adds those to the valid moves list to be filtered)
    '''

    def getkingmoves(self, r, c, moves):
        langkahraja = ((-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (0, -1), (1, 0), (0, 1))
        warnateman = "w" if self.whitetomove else "b"
        for i in range(8):
            endrow = r + langkahraja[i][0]
            endcol = c + langkahraja[i][1]
            if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                endpiece = self.board[endrow][endcol]
                if endpiece[0] != warnateman:
                    moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    semua langkah ferz lalu memasukan ke daftar (gets all the ferz moves and adds those to the valid moves list to be filtered)
    '''

    def getferzmoves(self, r, c, moves):
        self.getbishopmoves(r, c, moves)
        self.getrookmoves(r, c, moves)
        self.getknightmoves(r, c, moves)

    '''
    semua langkah duchess lalu memasukan ke daftar (gets all the duchess moves and adds those to the valid moves list to be filtered)
    '''

    def getduchessmoves(self, r, c, moves):
        self.getbishopmoves(r, c, moves)
        self.getgajahmoves(r, c, moves)
        self.getknightmoves(r, c, moves)

    '''
    semua langkah esquire lalu memasukan ke daftar (gets all the esquire moves and adds those to the valid moves list to be filtered)
    '''

    def getesquiremoves(self, r, c, moves):
        self.getgajahmoves(r, c, moves)
        self.getrookmoves(r, c, moves)
        self.getknightmoves(r, c, moves)

    '''
    semua langkah man lalu memasukan ke daftar (gets all the man moves and adds those to the valid moves list to be filtered)
    '''

    def getmanmoves(self, r, c, moves):
        self.getknightmoves(r, c, moves)
        self.getkingmoves(r, c, moves)

    '''
    semua langkah oknha lalu memasukan ke daftar (gets all the oknha moves and adds those to the valid moves list to be filtered)
    '''

    def getoknhamoves(self, r, c, moves):
        self.getrookmoves(r, c, moves)
        self.getbishopmoves(r, c, moves)
        self.getgajahmoves(r, c, moves)

    '''
    semua langkah gajah lalu memasukan ke daftar (gets all the elephant moves and adds those to the valid moves list to be filtered)
    '''

    def getgajahmoves(self, r, c, moves):
        langkahgajah = ((-3, -1), (-3, 1), (3, -1), (3, 1), (-1, 3), (-1, -3), (1, 3), (1, -3))
        warnateman = "w" if self.whitetomove else "b"
        for m in langkahgajah:
            endrow = r + m[0]
            endcol = c + m[1]
            if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                endpiece = self.board[endrow][endcol]
                if endpiece[0] != warnateman:
                    moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    semua langkah jester lalu memasukan ke daftar (gets all the jester moves and adds those to the valid moves list to be filtered)
    '''

    def getjestermoves(self, r, c, moves):
        self.getbishopmoves(r, c, moves)
        self.getgajahmoves(r, c, moves)

    '''
    semua langkah charriot lalu memasukan ke daftar (gets all the chariot moves and adds those to the valid moves list to be filtered)
    '''

    def getchariotmoves(self, r, c, moves):
        self.getrookmoves(r, c, moves)
        self.getgajahmoves(r, c, moves)

    '''
    semua langkah lance lalu memasukan ke daftar (gets all the lance moves and adds those to the valid moves list to be filtered)
    '''

    def getlancemoves(self, r, c, moves):
        self.getrookmoves(r, c, moves)
        self.getbishopmoves(r, c, moves)
        self.getknightmoves(r, c, moves)
        self.getgajahmoves(r, c, moves)

    '''
    semua langkah archbisop lalu memasukan ke daftar (gets all the archbishop moves and adds those to the valid moves list to be filtered)
    '''

    def getarchbishopmoves(self, r, c, moves):
        self.getbishopmoves(r, c, moves)
        self.getknightmoves(r, c, moves)

    '''
    semua langkah imam lalu memasukan ke daftar (gets all the imam moves and adds those to the valid moves list to be filtered)
    '''

    def getimammoves(self, r, c, moves):
        self.getrookmoves(r, c, moves)
        self.getknightmoves(r, c, moves)

    '''
    semua langkah xiphodon lalu memasukan ke daftar (gets all the xiphodon moves and adds those to the valid moves list to be filtered)
    '''

    def getxiphodonmoves(self, r, c, moves):
        warnamusuh = "b" if self.whitetomove else "w"
        if r - 1 > 0:
            if self.board[r - 1][c] == '--':
                d = (-1, 0)
                direction = ((-1, -1), (-1, 1))
                midrow = r + d[0]
                midcol = c + d[1]
                for a in direction:
                    for i in range(1, len(self.board[0])):
                        endrow = midrow + a[0] * i
                        endcol = midcol + a[1] * i
                        if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                            endpiece = self.board[endrow][endcol]
                            if endpiece == "--":  # diagonal bebas (moves freely diagonally)
                                moves.append(Move((r, c), (endrow, endcol), self.board))
                            elif endpiece[0] == warnamusuh:  # ketutupan musuh (blocked by enemy piece)
                                moves.append(Move((r, c), (endrow, endcol), self.board))
                                break
                            else:  # bidak sendiri (blocked by own piece)
                                break
                        else:  # diluar papan (out of the board)
                            break
        if r + 1 < len(self.board[0]):
            if self.board[r + 1][c] == '--':
                d = (1, 0)
                direction = ((1, 1), (1, -1))
                midrow = r + d[0]
                midcol = c + d[1]
                for a in direction:
                    for i in range(1, len(self.board[0])):
                        endrow = midrow + a[0] * i
                        endcol = midcol + a[1] * i
                        if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                            endpiece = self.board[endrow][endcol]
                            if endpiece == "--":  # diagonal bebas (moves freely diagonally)
                                moves.append(Move((r, c), (endrow, endcol), self.board))
                            elif endpiece[0] == warnamusuh:  # ketutupan musuh (blocked by enemy piece)
                                moves.append(Move((r, c), (endrow, endcol), self.board))
                                break
                            else:  # bidak sendiri (blocked by own piece)
                                break
                        else:  # diluar papan (out of the board)
                            break
        if c - 1 > 0:
            if self.board[r][c - 1] == '--':
                d = (0, -1)
                direction = ((-1, -1), (1, -1))
                midrow = r + d[0]
                midcol = c + d[1]
                for a in direction:
                    for i in range(1, len(self.board[0])):
                        endrow = midrow + a[0] * i
                        endcol = midcol + a[1] * i
                        if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                            endpiece = self.board[endrow][endcol]
                            if endpiece == "--":  # diagonal bebas (moves freely diagonally)
                                moves.append(Move((r, c), (endrow, endcol), self.board))
                            elif endpiece[0] == warnamusuh:  # ketutupan musuh (blocked by enemy piece)
                                moves.append(Move((r, c), (endrow, endcol), self.board))
                                break
                            else:  # bidak sendiri (blocked by own piece)
                                break
                        else:  # diluar papan (out of the board)
                            break
        if c + 1 < len(self.board[0]):
            if self.board[r][c + 1] == '--':
                d = (0, 1)
                direction = ((1, 1), (-1, 1))
                midrow = r + d[0]
                midcol = c + d[1]
                for a in direction:
                    for i in range(1, len(self.board[0])):
                        endrow = midrow + a[0] * i
                        endcol = midcol + a[1] * i
                        if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                            endpiece = self.board[endrow][endcol]
                            if endpiece == "--":  # diagonal bebas (moves freely diagonally)
                                moves.append(Move((r, c), (endrow, endcol), self.board))
                            elif endpiece[0] == warnamusuh:  # ketutupan musuh (blocked by enemy piece)
                                moves.append(Move((r, c), (endrow, endcol), self.board))
                                break
                            else:  # bidak sendiri (blocked by own piece)
                                break
                        else:  # diluar papan (out of the board)
                            break
        langkahxiphodon = ((-1, 0), (0, -1), (1, 0), (0, 1))
        warnateman = "w" if self.whitetomove else "b"
        for x in langkahxiphodon:
            endrow = r + x[0]
            endcol = c + x[1]
            if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                endpiece = self.board[endrow][endcol]
                if endpiece[0] != warnateman:
                    moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    semua langkah shrook lalu memasukan ke daftar (gets all the shrook moves and adds those to the valid moves list to be filtered)
    '''

    def getshrookmoves(self, r, c, moves):
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
        warnamusuh = "b" if self.whitetomove else "w"
        for d in directions:
            for i in range(1, 3):
                endrow = r + d[0] * i
                endcol = c + d[1] * i
                if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece == "--":  # horizontal bebas (moves freely horizontally)
                        moves.append(Move((r, c), (endrow, endcol), self.board))
                    elif endpiece[0] == warnamusuh:  # ketutupan musuh (blocked by enemy piece)
                        moves.append(Move((r, c), (endrow, endcol), self.board))
                        break
                    else:  # bidak sendiri (blocked by own piece)
                        break
                else:  # diluar papan (out of the board)
                    break

    '''
    semua langkah thalia lalu memasukan ke daftar (gets all the thalia moves and adds those to the valid moves list to be filtered)
    '''

    def getthaliamoves(self, r, c, moves):
        directions = ((-1, 1), (1, -1), (1, 1), (-1, -1))
        warnamusuh = "b" if self.whitetomove else "w"
        for d in directions:
            for i in range(1, 3):
                endrow = r + d[0] * i
                endcol = c + d[1] * i
                if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece == "--":  # horizontal bebas (moves freely diagonally)
                        moves.append(Move((r, c), (endrow, endcol), self.board))
                    elif endpiece[0] == warnamusuh:  # ketutupan musuh (blocked by enemy piece)
                        moves.append(Move((r, c), (endrow, endcol), self.board))
                        break
                    else:  # bidak sendiri (blocked by own piece)
                        break
                else:  # diluar papan (out of the board)
                    break

    '''
    semua langkah viscount lalu memasukan ke daftar (gets all the viscount moves and adds those to the valid moves list to be filtered)
    '''

    def getviscountmoves(self, r, c, moves):
        warnamusuh = "b" if self.whitetomove else "w"
        if r - 1 > 0 and c - 1 > 0:
            if self.board[r - 1][c - 1] == '--':
                d = (-1, -1)
                direction = ((0, -1), (-1, 0))
                midrow = r + d[0]
                midcol = c + d[1]
                for a in direction:
                    for i in range(1, len(self.board[0])):
                        endrow = midrow + a[0] * i
                        endcol = midcol + a[1] * i
                        if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                            endpiece = self.board[endrow][endcol]
                            if endpiece == "--":  # diagonal bebas (moves freely diagonally)
                                moves.append(Move((r, c), (endrow, endcol), self.board))
                            elif endpiece[0] == warnamusuh:  # ketutupan musuh (blocked by enemy piece)
                                moves.append(Move((r, c), (endrow, endcol), self.board))
                                break
                            else:  # bidak sendiri (blocked by own piece)
                                break
                        else:  # diluar papan (out of the board)
                            break
        if r - 1 > 0 and c + 1 < len(self.board[0]):
            if self.board[r - 1][c + 1] == '--':
                d = (-1, 1)
                direction = ((-1, 0), (0, 1))
                midrow = r + d[0]
                midcol = c + d[1]
                for a in direction:
                    for i in range(1, len(self.board[0])):
                        endrow = midrow + a[0] * i
                        endcol = midcol + a[1] * i
                        if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                            endpiece = self.board[endrow][endcol]
                            if endpiece == "--":  # diagonal bebas (moves freely diagonally)
                                moves.append(Move((r, c), (endrow, endcol), self.board))
                            elif endpiece[0] == warnamusuh:  # ketutupan musuh (blocked by enemy piece)
                                moves.append(Move((r, c), (endrow, endcol), self.board))
                                break
                            else:  # bidak sendiri (blocked by own piece)
                                break
                        else:  # diluar papan (out of the board)
                            break
        if r + 1 < len(self.board[0]) and c - 1 > 0:
            if self.board[r + 1][c - 1] == '--':
                d = (1, -1)
                direction = ((0, -1), (1, 0))
                midrow = r + d[0]
                midcol = c + d[1]
                for a in direction:
                    for i in range(1, len(self.board[0])):
                        endrow = midrow + a[0] * i
                        endcol = midcol + a[1] * i
                        if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                            endpiece = self.board[endrow][endcol]
                            if endpiece == "--":  # diagonal bebas (moves freely diagonally)
                                moves.append(Move((r, c), (endrow, endcol), self.board))
                            elif endpiece[0] == warnamusuh:  # ketutupan musuh (blocked by enemy piece)
                                moves.append(Move((r, c), (endrow, endcol), self.board))
                                break
                            else:  # bidak sendiri (blocked by own piece)
                                break
                        else:  # diluar papan (out of the board)
                            break
        if r + 1 < len(self.board[0]) and c + 1 < len(self.board[0]):
            if self.board[r + 1][c + 1] == '--':
                d = (1, 1)
                direction = ((1, 0), (0, 1))
                warnamusuh = "b" if self.whitetomove else "w"
                midrow = r + d[0]
                midcol = c + d[1]
                for a in direction:
                    for i in range(1, len(self.board[0])):
                        endrow = midrow + a[0] * i
                        endcol = midcol + a[1] * i
                        if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                            endpiece = self.board[endrow][endcol]
                            if endpiece == "--":  # diagonal bebas (moves freely diagonally)
                                moves.append(Move((r, c), (endrow, endcol), self.board))
                            elif endpiece[0] == warnamusuh:  # ketutupan musuh (blocked by enemy piece)
                                moves.append(Move((r, c), (endrow, endcol), self.board))
                                break
                            else:  # bidak sendiri (blocked by own piece)
                                break
                        else:  # diluar papan (out of the board)
                            break
        langkahviscount = ((-1, 1), (1, -1), (1, 1), (-1, -1))
        warnateman = "w" if self.whitetomove else "b"
        for x in langkahviscount:
            endrow = r + x[0]
            endcol = c + x[1]
            if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                endpiece = self.board[endrow][endcol]
                if endpiece[0] != warnateman:
                    moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    semua langkah zebra lalu memasukan ke daftar (gets all the zebra moves and adds those to the valid moves list to be filtered)
    '''

    def getzebramoves(self, r, c, moves):
        directions = ((-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (-1, -2), (1, 2), (1, -2))
        warnamusuh = "b" if self.whitetomove else "w"
        for d in directions:
            for i in range(1, 8):
                endrow = r + d[0] * i
                endcol = c + d[1] * i
                if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece == "--":  # horizontal bebas (moves freely horizontally)
                        moves.append(Move((r, c), (endrow, endcol), self.board))
                    elif endpiece[0] == warnamusuh:  # ketutupan musuh (blocked by enemy piece)
                        moves.append(Move((r, c), (endrow, endcol), self.board))
                        break
                    else:  # bidak sendiri (blocked by own piece)
                        break
                else:  # diluar papan (out of the board)
                    break

    '''
    semua langkah warrior lalu memasukan ke daftar (gets all the warrior moves and adds those to the valid moves list to be filtered)
    '''

    def getwarriormoves(self, r, c, moves):
        langkahwarrior = ((-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (0, -1), (1, 0), (0, 1))
        for m in langkahwarrior:
            endrow = r + m[0]
            endcol = c + m[1]
            if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                endpiece = self.board[endrow][endcol]
                if endpiece == "--":
                    moves.append(Move((r, c), (endrow, endcol), self.board))
        if self.whitetomove:
            if r - 2 >= 0:  # makan ke kiri (captures to the left)
                if self.board[r - 2][c][0] == 'b':  # ada bidak lawan (opponents piece that is blocking)
                    moves.append(Move((r, c), (r - 2, c), self.board))
        else:
            if r + 2 >= 0:  # makan ke kiri (captures to the left)
                if self.board[r + 2][c][0] == 'w':  # ada bidak lawan (opponents piece that is blocking)
                    moves.append(Move((r, c), (r + 2, c), self.board))

    '''
    semua langkah upasaka lalu memasukan ke daftar (gets all the upasaka moves and adds those to the valid moves list to be filtered)
    '''

    def getupasakamoves(self, r, c, moves):
        if self.whitetomove:
            langkahupasaka = ((-2, 1), (-2, -1), (-1, 2), (-1, -2), (-1, 0), (0, -1), (0, 1), (-2, 0), (0, -2), (0, 2), (1, 0))
            warnateman = "w" if self.whitetomove else "b"
            for m in langkahupasaka:
                endrow = r + m[0]
                endcol = c + m[1]
                if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman:
                        moves.append(Move((r, c), (endrow, endcol), self.board))
        else:
            langkahupasaka = ((2, 1), (2, -1), (1, 2), (1, -2), (0, -1), (1, 0), (0, 1), (0, -2), (2, 0), (0, 2), (-1, 0))
            warnateman = "w" if self.whitetomove else "b"
            for m in langkahupasaka:
                endrow = r + m[0]
                endcol = c + m[1]
                if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman:
                        moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    semua langkah yishi lalu memasukan ke daftar (gets all the yishi moves and adds those to the valid moves list to be filtered)
    '''

    def getyishimoves(self, r, c, moves):
        if self.whitetomove:
            langkahyishi = ((-1, -1), (-1, 1), (-2, 1), (-2, -1), (-1, 2), (-1, -2), (-2, -2), (-2, 2), (1, -1), (1, 1))
            warnateman = "w" if self.whitetomove else "b"
            for m in langkahyishi:
                endrow = r + m[0]
                endcol = c + m[1]
                if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman:
                        moves.append(Move((r, c), (endrow, endcol), self.board))
        else:
            langkahyishi = ((1, -1), (1, 1), (2, 1), (2, -1), (1, 2), (1, -2), (2, -2), (2, 2), (-1, 1), (-1, -1))
            warnateman = "w" if self.whitetomove else "b"
            for m in langkahyishi:
                endrow = r + m[0]
                endcol = c + m[1]
                if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman:
                        moves.append(Move((r, c), (endrow, endcol), self.board))


class Move:
    # biar bisa baca notasi catur (so it can somewhat produce chess notation)
    rankstorows = {"1": 15, "2": 14, "3": 13, "4": 12, "5": 11, "6": 10, "7": 9, "8": 8, "9": 7, "10": 6, "11": 5,
                   "12": 4, "13": 3, "14": 2, "15": 1, "16": 0}
    rowstoranks = {v: k for k, v in rankstorows.items()}
    filestocols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11,
                   "m": 12, "n": 13, "o": 14, "p": 15}
    colstofiles = {v: k for k, v in filestocols.items()}

    def __init__(self, startsq, endsq, board):
        self.startrow = startsq[0]
        self.startcol = startsq[1]
        self.endrow = endsq[0]
        self.endcol = endsq[1]
        self.piecemoved = board[self.startrow][self.startcol]
        self.piececaptured = board[self.endrow][self.endcol]
        self.ispromotion = (self.piecemoved[1] == 'P' or 'M' or 'S' or 'T' or 'W') and ((self.piecemoved[0] == 'w' and self.endrow == 0) or (self.piecemoved[0] == 'b' and self.endrow == 15))
        self.iscapture = self.piececaptured != '--'
        self.isnormalmove = self.piececaptured == '--'
        self.moveid = self.startrow * 1000000 + self.startcol * 10000 + self.endrow * 100 + self.endcol

    def getchessnotation(self):
        return self.getrankfile(self.startrow, self.startcol) + self.getrankfile(self.endrow, self.endcol)

    def getrankfile(self, r, c):
        return self.colstofiles[c] + self.rowstoranks[r]

    '''
    overriding samadengan (overriding the equal sign)
    '''

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveid == other.moveid
        return False

    '''
    overriding string
    '''

    def __str__(self):
        piecepromote = {"P": "=Q", "M": "=L", "S": "=R", "T": "=B", "W": "=N"}
        endsquare = self.getrankfile(self.endrow, self.endcol)
        # langkah pion (pawn moves)
        if self.piecemoved[1] == 'P':
            promotionmovestring = self.colstofiles[self.startcol]
            return (promotionmovestring + 'x' + endsquare + piecepromote[self.piecemoved[
                1]] if self.ispromotion else promotionmovestring + 'x' + endsquare) if self.iscapture else (
                endsquare + piecepromote[self.piecemoved[1]] if self.ispromotion else endsquare)

        # langkah bidak lainnya (other pieces' moves)
        if self.piecemoved[1] == 'M' or 'S' or 'T' or 'W':
            promotionmovestring = self.piecemoved[1]
            return (promotionmovestring + 'x' + endsquare + piecepromote[self.piecemoved[
                1]] if self.ispromotion else promotionmovestring + 'x' + endsquare) if self.iscapture else (
                endsquare + piecepromote[self.piecemoved[1]] if self.ispromotion else endsquare)
        movestring = self.piecemoved[1]
        return movestring + 'x' + endsquare if self.iscapture else movestring + endsquare
