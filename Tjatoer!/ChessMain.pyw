"""
File driver utama, bertanggung jawab atas user input dan display (Main file driver, responsible for user input and display)
"""
from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import multiprocessing
from multiprocessing import Queue, Process
import pygame as p
import ChessEngine
import SmartMoveFinder

WindowWidth = WindowHeight = 1000
MoveWidth = 880
MoveHeight = WindowHeight
Dimension = 16
Ukr_Petak = WindowHeight//Dimension
FPSMaks = 30  # buat animasi (for animation, though animation is not implemented yet)
Theme = "Textures/Simple/"
Images = {}

p.display.set_caption('Tjatoer!')
programIcon = p.image.load(Theme + "wG.png")
p.display.set_icon(programIcon)

'''
memulai kamus global gambar, akan dipanggil hanya sekali (global dictionary for images, called only once)
'''


def loadimages():
    pieces = ['wA', 'bA', 'wB', 'bB', 'wC', 'bC', 'wD', 'bD', 'wE', 'bE', 'wF', 'bF', 'wG', 'bG', 'wH', 'bH', 'wI',
              'bI', 'wJ', 'bJ', 'wK', 'bK', 'wL', 'bL', 'wM', 'bM', 'wN', 'bN', 'wO', 'bO', 'wP', 'bP', 'wQ', 'bQ',
              'wR',
              'bR', 'wS', 'bS', 'wT', 'bT', 'wU', 'bU', 'wV', 'bV', 'wW', 'bW', 'wX', 'bX', 'wY', 'bY', 'wZ', 'bZ']
    for bidak in pieces:
        Images[bidak] = p.transform.scale(p.image.load(Theme + bidak + ".png"), (Ukr_Petak, Ukr_Petak))
    # gambar bisa dipanggil dengan bilang Images['bidak']


'''
driver utama kode, akan menghandle user input (main driver code, handles user input)
'''


def main():
    p.init()
    screen = p.display.set_mode((WindowWidth + MoveWidth, WindowHeight))
    clock = p.time.Clock()
    screen.fill(p.Color("#202020"))
    movelogfont = p.font.Font("Fonts/OverpassMono-Regular.ttf", 11)
    gs = ChessEngine.GameState()
    validmoves = gs.getvalidmoves()
    movemade = False
    move = ()
    loadimages()  # sebelum while loop (before the while loop)
    running = True
    sqselected = ()  # tdk ada petak yang dipilih, mencatat petak yang user klik (row, col) (no square selected, records selected squares in (row, col))
    playerclicks = []  # mencatat klik user [(row,col),(row,col)] (records user clicks in [(row, col), (row, col)])
    gameover = False
    playerone = True  # kalo manusia putih maka true, sebaliknya false (if human is white then true, else false)
    playertwo = True  # kalo manusia hitam maka true, sebaliknya false (if human is black then true, else false)
    aithinking = False
    movefinderprocess = None
    moveundone = False
    sound = p.mixer.Sound("Sounds/gamestart.mp3")
    sound.play()
    while running:
        humanturn = (gs.whitetomove and playerone) or (not gs.whitetomove and playertwo)
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            # mouse handler
            elif e.type == p.MOUSEBUTTONDOWN:
                if not gameover:
                    if e.button == 1:
                        location = p.mouse.get_pos()  # lokasi pointer mouse (mouse pointer location)
                        col = location[0]//Ukr_Petak
                        row = location[1]//Ukr_Petak
                        if sqselected == (row, col) or col >= len(gs.board[0]):
                            sqselected = ()  # biar gabisa diklik 2 kali (so that the user can't click the same square twice)
                            playerclicks = []  # biar gabisa diklik 2 kali (so that the user can't click the same square twice)
                        else:
                            sqselected = (row, col)
                            playerclicks.append(sqselected)
                        if len(playerclicks) == 2 and humanturn:  # setelah klik kedua (after the second click)
                            move = ChessEngine.Move(playerclicks[0], playerclicks[1], gs.board)
                            for i in range(len(validmoves)):
                                if move == validmoves[i]:
                                    gs.makemove(validmoves[i])
                                    movemade = True
                                    sqselected = ()
                                    playerclicks = []
                            if not movemade:
                                playerclicks = [sqselected]

            # key handler
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:  # undo ketika tekan z (undo when z is pressed)
                    gs.undomove()
                    movemade = True
                    gameover = False
                    if aithinking:
                        movefinderprocess.terminate()
                        aithinking = False
                    moveundone = True
                if e.key == p.K_r:  # reset ketika tekan r (reset when r is pressed)
                    gs = ChessEngine.GameState()
                    validmoves = gs.getvalidmoves()
                    sqselected = ()
                    playerclicks = []
                    movemade = False
                    gameover = False
                    if aithinking:
                        movefinderprocess.terminate()
                        aithinking = False
                    moveundone = True

        # AI move finder
        if not gameover and not humanturn and not moveundone:
            if not aithinking:
                aithinking = True
                print('sedang berfikir...')
                returnqueue = Queue()  # oper data antara thread (gives the data between threads)
                movefinderprocess = Process(target=SmartMoveFinder.findbestmove, args=(gs, validmoves, returnqueue))
                movefinderprocess.start()
            if not movefinderprocess.is_alive():
                move = returnqueue.get()
                print('sudah berfikir''\n''==================================================================')
                if move is None:
                    move = SmartMoveFinder.findrandommove(validmoves)
                gs.makemove(move)
                movemade = True
                aithinking = False

        drawgamestate(screen, gs, validmoves, sqselected, movelogfont)

        if gs.checkmate or gs.stalemate:
            gameover = True
            drawendgametext(screen,
                            'Remis!' if gs.stalemate else 'Hitam Menang!' if gs.whitetomove else 'Putih Menang!')

        if movemade:
            # telah terbuatnya langkah (a move is made)
            validmoves = gs.getvalidmoves()
            movemade = False
            moveundone = False
            playsound(move, gs)
        clock.tick(FPSMaks)
        p.display.flip()


'''
bertugas menggambar grafik pada permainan (is tasked with drawing the graphics of the game)
'''


def drawgamestate(screen, gs, validmoves, sqselected, movelogfont):
    drawboard(screen)  # menggambar petak pada papan (draws squares on the board)
    highlightsquares(screen, gs, validmoves, sqselected)
    drawpieces(screen, gs.board)  # menggmbar bidak diatas petak (puts the pieces on the squares)
    drawmovelog(screen, gs, movelogfont)


'''
bertugas memainkan suara (is tasked with playing the game sounds)
'''


def playsound(move, gs):
    if gs.checkmate:
        sound = p.mixer.Sound("Sounds/checkmate.mp3")
        sound.play()
    elif gs.stalemate:
        sound = p.mixer.Sound("Sounds/stalemate.mp3")
        sound.play()
    elif gs.incheck():
        sound = p.mixer.Sound("Sounds/check.mp3")
        sound.play()
    else:
        if move.iscapture:
            sound = p.mixer.Sound("Sounds/capture.mp3")
            sound.play()
        else:
            sound = p.mixer.Sound("Sounds/move.mp3")
            sound.play()


'''
menggambar petak (draws the squares)
'''


def drawboard(screen):
    warnawarna = [p.Color("#FFCE9E"), p.Color("#D18B47")]
    for r in range(Dimension):
        for c in range(Dimension):
            warna = warnawarna[((r + c)%2)]
            p.draw.rect(screen, warna, p.Rect(c*Ukr_Petak, r*Ukr_Petak, Ukr_Petak, Ukr_Petak))


'''
highlight petak (highlights the squares)
'''


def highlightsquares(screen, gs, validmoves, sqselected):
    if (len(gs.movelog)) > 0:
        lastmove = gs.movelog[-1]
        s = p.Surface((Ukr_Petak, Ukr_Petak))
        s.set_alpha(100)
        s.fill(p.Color('red'))
        screen.blit(s, (lastmove.endcol*Ukr_Petak, lastmove.endrow*Ukr_Petak))
    if sqselected != ():
        r, c = sqselected
        if gs.board[r][c][0] == (
                'w' if gs.whitetomove else 'b'):  # petak yg dipilih adalah bidak yg bisa jalan (selected square is a piece that is able to move)
            # highlight petak
            s = p.Surface((Ukr_Petak, Ukr_Petak))
            s.set_alpha(100)  # trasparansi (transparancy)
            s.fill(p.Color('purple'))
            screen.blit(s, (c*Ukr_Petak, r*Ukr_Petak))
            # highlight langkah
            s.fill(p.Color('yellow'))
            for move in validmoves:
                if move.startrow == r and move.startcol == c:
                    screen.blit(s, (move.endcol*Ukr_Petak, move.endrow*Ukr_Petak))


'''
menggambar bidak (draws the pieces)
'''


def drawpieces(screen, board):
    for r in range(Dimension):
        for c in range(Dimension):
            bidak = board[r][c]
            if bidak != "--":
                screen.blit(Images[bidak], p.Rect(c*Ukr_Petak, r*Ukr_Petak, Ukr_Petak, Ukr_Petak))


"""
movelog (draws the movelog)
"""


def drawmovelog(screen, gs, font):
    movelogrect = p.Rect(WindowWidth, 0, MoveWidth, MoveHeight)
    p.draw.rect(screen, p.Color('#202020'), movelogrect)
    movelog = gs.movelog
    movetexts = []
    for i in range(0, len(movelog), 2):
        movestring = str(i//2 + 1) + "." + str(movelog[i]) + " "
        if i + 1 < len(movelog):  # memastikan hitam sudah jalan (makes sure that black has made a move)
            movestring += str(movelog[i + 1]) + "  "
        movetexts.append(movestring)
    movesperrow = 8
    padding = 5
    texty = padding
    linespacing = 2
    for i in range(0, len(movetexts), movesperrow):
        text = ""
        for j in range(movesperrow):
            if i + j < len(movetexts):
                text += movetexts[i + j]
        textobject = font.render(text, False, p.Color('White'))
        textlocation = movelogrect.move(padding, texty)
        screen.blit(textobject, textlocation)
        texty += textobject.get_height() + linespacing


'''
menggambar text (draws the game over text)
'''


def drawendgametext(screen, text):
    font = p.font.Font("Fonts/HelveticaNeueLTPro-Bd.otf", 52)
    textobject = font.render(text, False, p.Color('Black'))
    textlocation = p.Rect(0, 0, WindowWidth, WindowHeight).move(WindowWidth/2 - textobject.get_width()/2,
                                                                WindowHeight/2 - textobject.get_height()/2)
    screen.blit(textobject, textlocation)


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
