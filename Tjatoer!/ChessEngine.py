"""
File ini bertanggung jawab untuk menampung semua informasi permainan dan juga langkah-langkah valid dan mencatat langkah
"""


class GameState:
    def __init__(self):
        # papan caturnya 8x8 daftar 2 dimensional, setiap elemen daftar mempunyai 2 karakter, karakter pertama warnanya, kedua tipenya
        self.board = [
            ["bQ", "bC", "bN", "bA", "bB", "bM", "bF", "bL", "bK", "bF", "bM", "bB", "bA", "bN", "bC", "bQ"],
            ["bR", "bZ", "bZ", "bZ", "bZ", "bZ", "bZ", "bG", "bG", "bZ", "bZ", "bZ", "bZ", "bZ", "bZ", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wZ", "wZ", "wZ", "wZ", "wZ", "wZ", "wG", "wG", "wZ", "wZ", "wZ", "wZ", "wZ", "wZ", "wR"],
            ["wQ", "wC", "wN", "wA", "wB", "wM", "wF", "wL", "wK", "wF", "wM", "wB", "wA", "wN", "wC", "wQ"]]
        self.movefunction = {'P': self.getpawnmoves, 'R': self.getrookmoves, 'N': self.getknightmoves,
                             'B': self.getbishopmoves, 'Q': self.getqueenmoves, 'K': self.getkingmoves,
                             'F': self.getferzmoves, 'M': self.getmanmoves, 'G': self.getalfilmoves,
                             'L': self.getamazonmoves, 'A': self.getarchbishopmoves, 'C': self.getchancellormoves,
                             'Z': self.getwazirmoves}
        self.whitetomove = True
        self.movelog = []
        self.whitekinglocation = (15, 8)
        self.blackkinglocation = (0, 8)
        self.checkmate = False
        self.stalemate = False

    '''
    mengambil langkah sebagai parameter kemudian mengeksekusinya
    '''

    def makemove(self, move):
        self.board[move.startrow][move.startcol] = "--"
        self.board[move.endrow][move.endcol] = move.piecemoved
        self.movelog.append(move)  # mencatat langkah biar bisa diundo
        self.whitetomove = not self.whitetomove  # gantian giliran
        if move.piecemoved == 'wK':
            self.whitekinglocation = (move.endrow, move.endcol)
        elif move.piecemoved == 'bK':
            self.blackkinglocation = (move.endrow, move.endcol)

        # promosi pion
        if move.ispawnpromotion:
            self.board[move.endrow][move.endcol] = move.piecemoved[0] + 'L'

    '''
    undo lngkah terakhir
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
    semua langkah termasuk skak
    '''

    def getvalidmoves(self):
        # 1. membuat semua langkah yang mungkin
        moves = self.getallpossibledmoves()
        # 2. membuat semua langkah lawan yang mungkin
        for i in range(len(moves) - 1, -1, -1):
            self.makemove(moves[i])
            # 3. cek kallo raja kita lg diserang
            self.whitetomove = not self.whitetomove
            if self.incheck():
                moves.remove(moves[i])  # 4. kalau ya maka tdk valid
            self.whitetomove = not self.whitetomove
            self.undomove()
        if len(moves) == 0:
            # antara skakmat atau stalemate
            if self.incheck():
                self.checkmate = True
            else:
                self.stalemate = True
        else:
            self.checkmate = False
            self.stalemate = False
        return moves

    '''
    tau kalau lagi skak
    '''

    def incheck(self):
        if self.whitetomove:
            return self.squareunderattack(self.whitekinglocation[0], self.whitekinglocation[1])
        else:
            return self.squareunderattack(self.blackkinglocation[0], self.blackkinglocation[1])

    '''
    petak yg lagi diserang
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
    semua langkah tidak termasuk skak
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
    semua langkah pion lalu memasukan ke daftar
    '''

    def getpawnmoves(self, r, c, moves):
        if self.whitetomove:  # pion putih
            if self.board[r - 1][c] == "--":  # maju 1 petak
                moves.append(Move((r, c), (r - 1, c), self.board))
                if r == 13 and self.board[r - 2][c] == "--":  # maju 2 petak di langkah pertama
                    moves.append(Move((r, c), (r - 2, c), self.board))
                    if self.board[r - 3][c] == "--":
                        moves.append(Move((r, c), (r - 3, c), self.board))
                        if self.board[r - 4][c] == "--":
                            moves.append(Move((r, c), (r - 4, c), self.board))
                            if self.board[r - 5][c] == "--":
                                moves.append(Move((r, c), (r - 5, c), self.board))
            if c - 1 >= 0:  # makan ke kiri
                if self.board[r - 1][c - 1][0] == 'b':  # ada bidak lawan
                    moves.append(Move((r, c), (r - 1, c - 1), self.board))
            if c + 1 <= 15:  # makan ke kanan
                if self.board[r - 1][c + 1][0] == 'b':  # ada bidak lawan
                    moves.append(Move((r, c), (r - 1, c + 1), self.board))

        else:  # pion hitam
            if self.board[r + 1][c] == "--":  # maju 1 petak
                moves.append(Move((r, c), (r + 1, c), self.board))
                if r == 2 and self.board[r + 2][c] == "--":  # maju 2 petak di langkah pertama
                    moves.append(Move((r, c), (r + 2, c), self.board))
                    if self.board[r + 3][c] == "--":
                        moves.append(Move((r, c), (r + 3, c), self.board))
                        if self.board[r + 4][c] == "--":
                            moves.append(Move((r, c), (r + 4, c), self.board))
                            if self.board[r + 5][c] == "--":
                                moves.append(Move((r, c), (r + 5, c), self.board))
            if c - 1 >= 0:  # makan ke kiri
                if self.board[r + 1][c - 1][0] == 'w':  # ada bidak lawan
                    moves.append(Move((r, c), (r + 1, c - 1), self.board))
            if c + 1 <= 15:  # makan ke kanan
                if self.board[r + 1][c + 1][0] == 'w':  # ada bidak lawan
                    moves.append(Move((r, c), (r + 1, c + 1), self.board))

    '''
    semua langkah benteng lalu memasukan ke daftar
    '''

    def getrookmoves(self, r, c, moves):
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
        warnamusuh = "b" if self.whitetomove else "w"
        for d in directions:
            for i in range(1, 16):
                endrow = r + d[0] * i
                endcol = c + d[1] * i
                if 0 <= endrow <= 15 and 0 <= endcol <= 15:
                    endpiece = self.board[endrow][endcol]
                    if endpiece == "--":  # horizontal bebas
                        moves.append(Move((r, c), (endrow, endcol), self.board))
                    elif endpiece[0] == warnamusuh:  # ketutupan musuh
                        moves.append(Move((r, c), (endrow, endcol), self.board))
                        break
                    else:  # bidak sendiri
                        break
                else:  # diluar papan
                    break

    '''
    semua langkah kuda lalu memasukan ke daftar
    '''

    def getknightmoves(self, r, c, moves):
        langkahkuda = ((-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (-1, -2), (1, 2), (1, -2))
        warnateman = "w" if self.whitetomove else "b"
        for m in langkahkuda:
            endrow = r + m[0]
            endcol = c + m[1]
            if 0 <= endrow <= 15 and 0 <= endcol <= 15:
                endpiece = self.board[endrow][endcol]
                if endpiece[0] != warnateman:
                    moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    semua langkah gajah lalu memasukan ke daftar
    '''

    def getbishopmoves(self, r, c, moves):
        directions = ((-1, -1), (1, -1), (1, 1), (-1, 1))
        warnamusuh = "b" if self.whitetomove else "w"
        for d in directions:
            for i in range(1, 16):
                endrow = r + d[0] * i
                endcol = c + d[1] * i
                if 0 <= endrow <= 15 and 0 <= endcol <= 15:
                    endpiece = self.board[endrow][endcol]
                    if endpiece == "--":  # horizontal bebas
                        moves.append(Move((r, c), (endrow, endcol), self.board))
                    elif endpiece[0] == warnamusuh:  # ketutupan musuh
                        moves.append(Move((r, c), (endrow, endcol), self.board))
                        break
                    else:  # bidak sendiri
                        break
                else:  # diluar papan
                    break

    '''
    semua langkah mentri lalu memasukan ke daftar
    '''

    def getqueenmoves(self, r, c, moves):
        self.getbishopmoves(r, c, moves)
        self.getrookmoves(r, c, moves)

    '''
    semua langkah raja lalu memasukan ke daftar
    '''

    def getkingmoves(self, r, c, moves):
        langkahraja = ((-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (0, -1), (1, 0), (0, 1))
        warnateman = "w" if self.whitetomove else "b"
        for i in range(8):
            endrow = r + langkahraja[i][0]
            endcol = c + langkahraja[i][1]
            if 0 <= endrow <= 15 and 0 <= endcol <= 15:
                endpiece = self.board[endrow][endcol]
                if endpiece[0] != warnateman:
                    moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    semua langkah ferz lalu memasukan ke daftar
    '''

    def getferzmoves(self, r, c, moves):
        langkahferz = ((-1, 1), (-1, -1), (1, -1), (1, 1))
        warnateman = "w" if self.whitetomove else "b"
        for m in langkahferz:
            endrow = r + m[0]
            endcol = c + m[1]
            if 0 <= endrow <= 15 and 0 <= endcol <= 15:
                endpiece = self.board[endrow][endcol]
                if endpiece[0] != warnateman:
                    moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    semua langkah man lalu memasukan ke daftar
    '''

    def getmanmoves(self, r, c, moves):
        langkahman = ((-1, 0), (0, -1), (1, 0), (0, 1))
        warnateman = "w" if self.whitetomove else "b"
        for m in langkahman:
            endrow = r + m[0]
            endcol = c + m[1]
            if 0 <= endrow <= 15 and 0 <= endcol <= 15:
                endpiece = self.board[endrow][endcol]
                if endpiece[0] != warnateman:
                    moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    semua langkah wazir lalu memasukan ke daftar
    '''

    def getwazirmoves(self, r, c, moves):
        langkahwazir = ((-1, 0), (0, -1), (1, 0), (0, 1), (-1, 1), (-1, -1), (1, -1), (1, 1))
        warnateman = "w" if self.whitetomove else "b"
        for m in langkahwazir:
            endrow = r + m[0]
            endcol = c + m[1]
            if 0 <= endrow <= 15 and 0 <= endcol <= 15:
                endpiece = self.board[endrow][endcol]
                if endpiece[0] != warnateman:
                    moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    semua langkah alfil lalu memasukan ke daftar
    '''

    def getalfilmoves(self, r, c, moves):
        langkahalfil = ((-2, -2), (-2, 2), (2, -2), (2, 2))
        warnateman = "w" if self.whitetomove else "b"
        for m in langkahalfil:
            endrow = r + m[0]
            endcol = c + m[1]
            if 0 <= endrow <= 15 and 0 <= endcol <= 15:
                endpiece = self.board[endrow][endcol]
                if endpiece[0] != warnateman:
                    moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    semua langkah amazon lalu memasukan ke daftar
    '''

    def getamazonmoves(self, r, c, moves):
        self.getrookmoves(r, c, moves)
        self.getbishopmoves(r, c, moves)
        self.getknightmoves(r, c, moves)

    '''
    semua langkah archbisop lalu memasukan ke daftar
    '''

    def getarchbishopmoves(self, r, c, moves):
        self.getbishopmoves(r, c, moves)
        self.getknightmoves(r, c, moves)

    '''
    semua langkah chancellor lalu memasukan ke daftar
    '''

    def getchancellormoves(self, r, c, moves):
        self.getrookmoves(r, c, moves)
        self.getknightmoves(r, c, moves)


class Move:
    # biar bisa baca notasi catur
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
        self.ispawnpromotion = (self.piecemoved == 'wP' and self.endrow == 0) or (
                self.piecemoved == 'bP' and self.endrow == 15)
        self.iscapture = self.piececaptured != '--'
        self.isnormalmove = self.piececaptured == '--'
        self.moveid = self.startrow * 10000 + self.startcol * 1000 + self.endrow * 100 + self.endcol

    def getchessnotation(self):
        return self.getrankfile(self.startrow, self.startcol) + self.getrankfile(self.endrow, self.endcol)

    def getrankfile(self, r, c):
        return self.colstofiles[c] + self.rowstoranks[r]

    '''
    overriding samadengan
    '''

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveid == other.moveid
        return False

    '''
    overriding string
    '''

    def __str__(self):
        endsquare = self.getrankfile(self.endrow, self.endcol)
        # langkah pion
        if self.piecemoved[1] == 'P':
            pawnmovestring = self.colstofiles[self.startcol]
            if self.iscapture:
                return pawnmovestring + 'x' + endsquare + '=L' if self.ispawnpromotion else pawnmovestring + 'x' + endsquare
            else:
                return endsquare + '=L' if self.ispawnpromotion else endsquare

        # langkah bidak lainnya
        movestring = self.piecemoved[1]
        return movestring + 'x' + endsquare if self.iscapture else movestring + endsquare
