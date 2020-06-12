import random
from copy import deepcopy
import time
import pygame

pygame.init()


class Button:
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.colour = (200, 200, 200)
        self.text = text
        self.block_size = 100

    def drawButton(self):
        rect = pygame.Rect(self.x, self.y,
                           self.block_size, self.block_size)
        return rect

    def isOver(self, mouse):
        if self.x < mouse[0] < self.x + self.block_size:
            if self.y < mouse[1] < self.y + self.block_size:
                return True
        return False

    def destroyButton(self):
        self.y = 1000


class TicTacToe:
    def __init__(self):
        self.colours = {0: (255, 100, 100), 1: (100, 100, 255)}
        self.depth = 3
        self.moves = {1: "X", 0: "O"}
        self.ai_turn = random.choice([1, 0])
        self.state = [['', '', ''], ['', '', ''], ['', '', '']]
        self.screen_dimensions = (302, 302)
        self.block_size = 100
        self.number_of_grids = 3
        self.buttons = []
        self.turn = 1
        self.font = pygame.font.Font("freesansbold.ttf", 100)
        for i in range(0, self.number_of_grids):
            for j in range(0, self.number_of_grids):
                self.buttons.append(Button(j * (self.block_size + 1), i * (self.block_size + 1), self.state[i][j]))
        self.startGame()

    def startGame(self):
        self.screen = pygame.display.set_mode(self.screen_dimensions)
        pygame.display.set_caption("Tic Tac Toe")
        running = True

        while running:
            self.screen.fill([200, 200, 200])
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.turn % 2 != self.ai_turn:
                        k = 0
                        for i in range(0, self.number_of_grids):
                            for j in range(0, self.number_of_grids):
                                if self.buttons[k].isOver(mouse):
                                    self.playMove(i, j)
                                    self.turn += 1
                                    self.buttons[k].destroyButton()
                                k += 1

                if event.type == pygame.MOUSEBUTTONUP:
                    break

            if self.turn % 2 == self.ai_turn and not self.checkWin(self.state, (self.turn + 1) % 2):
                self.drawGrid()
                pygame.display.update()
                time.sleep(1.00)
                cur_state = self.state
                if self.ai_turn == 1:
                    isMax = True
                else:
                    isMax = False
                move = self.minimax(cur_state, self.depth, isMax, self.turn)
                k = 0
                for i in range(0, 3):
                    for j in range(0, 3):
                        try:
                            if move[i][j] != cur_state[i][j]:
                                self.playMove(i, j)
                                self.turn += 1
                                self.buttons[k].destroyButton()
                            k += 1
                        except:
                            pass

            self.drawGrid()

            if self.checkWin(self.state, (self.turn + 1) % 2):
                self.drawCircle((self.turn + 1) % 2)

            if self.checkWin(self.state, self.turn % 2):
                self.drawCircle(self.turn % 2)

            # checking if button is active
            for i in range(0, 9):
                if self.buttons[i].isOver(mouse):
                    self.buttons[i].colour = (255, 255, 255)
                else:
                    self.buttons[i].colour = (200, 200, 200)
            pygame.display.update()

    def drawGrid(self):
        self.screen.fill((255, 255, 255))
        k = 0
        for row in range(self.number_of_grids):
            for column in range(self.number_of_grids):
                rect = self.buttons[k].drawButton()
                pygame.draw.rect(self.screen, self.buttons[k].colour, rect)
                k += 1
        self.displayText()

    def displayText(self):
        for row in range(self.number_of_grids):
            for column in range(self.number_of_grids):
                x = column * (self.block_size + 1) + 10
                y = row * (self.block_size + 1) + 10
                text = self.font.render(self.state[row][column], True, (0, 0, 0))
                self.screen.blit(text, (x, y))

    def playMove(self, i, j):
        self.state[i][j] = self.moves[self.turn % 2]
        win = self.checkWin(self.state, self.turn % 2)
        if win:
            for k in range(0, 9):
                self.buttons[k].y = 500
            if self.turn % 2 != self.ai_turn:
                self.turn = 1 - self.ai_turn

        draw = self.checkDraw(self.state)
        if draw:
            return

    def minimax(self, state, depth, isMax, player):
        if depth == 0 or self.checkWin(state, (player + 1) % 2) or self.checkDraw(state):
            return self.evalPosition(state, player, depth)
        if isMax:
            max_eval = -100
            expanded_nodes = self.getMoves(state, player)
            for node in expanded_nodes:
                eval = self.minimax(node, depth - 1, False, player + 1)
                try:
                    if depth == self.depth and max_eval < eval:
                        best_move = node

                    max_eval = max(max_eval, eval)

                except:
                    if depth == self.depth:
                        return node
                    return 0
            if depth == self.depth:
                try:
                    return best_move
                except:
                    return random.choice(expanded_nodes)
            return max_eval

        else:
            min_eval = 100
            expanded_nodes = self.getMoves(state, player)
            for node in expanded_nodes:
                eval = self.minimax(node, depth - 1, True, player + 1)
                try:
                    if depth == self.depth and eval < min_eval:
                        best_move = node

                    min_eval = min(min_eval, eval)

                except:
                    if depth == self.depth:
                        return node
                    return 0

            if depth == self.depth:
                try:
                    return best_move
                except:
                    return random.choice(expanded_nodes)
            return min_eval

    def getMoves(self, list, player):
        expanded_nodes = []
        for i in range(0, 3):
            for j in range(0, 3):
                if list[i][j] == '':
                    new_state = deepcopy(list)
                    new_state[i][j] = self.moves[player % 2]

                    expanded_nodes.append(new_state)
        return expanded_nodes

    def evalPosition(self, list, player, depth):
        X2 = 0
        X1 = 0
        O1 = 0
        O2 = 0

        if self.checkWin(list, 1):
            return 15 + depth
        if self.checkWin(list, 0):
            return -15 - depth

        # check for 2 consecutive Xs
        for i in range(0, 3):
            if list[i][0] == list[i][1] == 'X' and list[i][2] == '':
                X2 += 1
            elif list[i][1] == list[i][2] == 'X' and list[i][0] == '':
                X2 += 1
            elif list[i][0] == list[i][2] == 'X' and list[i][1] == '':
                X2 += 1
        for j in range(0, 3):
            if list[0][j] == list[1][j] == 'X' and list[2][j] == '':
                X2 += 1
            elif list[0][j] == list[2][j] == 'X' and list[1][j] == '':
                X2 += 1
            elif list[2][j] == list[1][j] == 'X' and list[0][j] == '':
                X2 += 1
        if list[0][0] == list[1][1] == 'X' and list[2][2] == '':
            X2 += 1
        elif list[0][0] == list[2][2] == 'X' and list[1][1] == '':
            X2 += 1
        elif list[2][2] == list[1][1] == 'X' and list[0][0] == '':
            X2 += 1
        if list[2][0] == list[1][1] == 'X' and list[0][2] == '':
            X2 += 1
        elif list[2][0] == list[0][2] == 'X' and list[1][1] == '':
            X2 += 1
        elif list[0][2] == list[1][1] == 'X' and list[2][0] == '':
            X2 += 1

        # check for single Xs
        for i in range(0, 3):
            if list[i][0] == list[i][1] == '' and list[i][2] == 'X':
                X1 += 1
            elif list[i][1] == list[i][2] == '' and list[i][0] == 'X':
                X1 += 1
            elif list[i][0] == list[i][2] == '' and list[i][1] == 'X':
                X1 += 1
        for j in range(0, 3):
            if list[0][j] == list[1][j] == '' and list[2][j] == 'X':
                X1 += 1
            elif list[0][j] == list[2][j] == '' and list[1][j] == 'X':
                X1 += 1
            elif list[2][j] == list[1][j] == '' and list[0][j] == 'X':
                X1 += 1
        if list[0][0] == list[1][1] == '' and list[2][2] == 'X':
            X1 += 1
        elif list[0][0] == list[2][2] == '' and list[1][1] == 'X':
            X1 += 1
        elif list[2][2] == list[1][1] == '' and list[0][0] == 'X':
            X1 += 1
        if list[2][0] == list[1][1] == '' and list[0][2] == 'X':
            X1 += 1
        elif list[2][0] == list[0][2] == '' and list[1][1] == 'X':
            X1 += 1
        elif list[0][2] == list[1][1] == '' and list[2][0] == 'X':
            X1 += 1

        # check for O win

        # check for double Os

        for i in range(0, 3):
            if list[i][0] == list[i][1] == 'O' and list[i][2] == '':
                O2 += 1
            elif list[i][1] == list[i][2] == 'O' and list[i][0] == '':
                O2 += 1
            elif list[i][0] == list[i][2] == 'O' and list[i][1] == '':
                O2 += 1
        for j in range(0, 3):
            if list[0][j] == list[1][j] == 'O' and list[2][j] == '':
                O2 += 1
            elif list[0][j] == list[2][j] == 'O' and list[1][j] == '':
                O2 += 1
            elif list[2][j] == list[1][j] == 'O' and list[0][j] == '':
                O2 += 1
        if list[0][0] == list[1][1] == 'O' and list[2][2] == '':
            O2 += 1
        elif list[0][0] == list[2][2] == 'O' and list[1][1] == '':
            O2 += 1
        elif list[2][2] == list[1][1] == 'O' and list[0][0] == '':
            O2 += 1
        if list[2][0] == list[1][1] == 'O' and list[0][2] == '':
            O2 += 1
        elif list[2][0] == list[0][2] == 'O' and list[1][1] == '':
            O2 += 1
        elif list[0][2] == list[1][1] == 'O' and list[2][0] == '':
            O2 += 1

        # check for single Os
        for i in range(0, 3):
            if list[i][0] == list[i][1] == '' and list[i][2] == 'O':
                O1 += 1
            elif list[i][1] == list[i][2] == '' and list[i][0] == 'O':
                O1 += 1
            elif list[i][0] == list[i][2] == '' and list[i][1] == 'O':
                O1 += 1
        for j in range(0, 3):
            if list[0][j] == list[1][j] == '' and list[2][j] == 'O':
                O1 += 1
            elif list[0][j] == list[2][j] == '' and list[1][j] == 'O':
                O1 += 1
            elif list[2][j] == list[1][j] == '' and list[0][j] == 'O':
                O1 += 1
        if list[0][0] == list[1][1] == '' and list[2][2] == 'O':
            O1 += 1
        elif list[0][0] == list[2][2] == '' and list[1][1] == 'O':
            O1 += 1
        elif list[2][2] == list[1][1] == '' and list[0][0] == 'O':
            O1 += 1
        if list[2][0] == list[1][1] == '' and list[0][2] == 'O':
            O1 += 1
        elif list[2][0] == list[0][2] == '' and list[1][1] == 'O':
            O1 += 1
        elif list[0][2] == list[1][1] == '' and list[2][0] == 'O':
            O1 += 1
        return 3 * X2 + X1 - (3 * O2 + O1) + ((-1) * (player + 1)) * depth

    def checkWin(self, state, player):
        # check same rows
        for row in range(0, 3):
            if state[row][0] == state[row][1] == state[row][2] == self.moves[player]:
                return True
        # check same columns
        for column in range(0, 3):
            if state[0][column] == state[1][column] == state[2][column] == self.moves[player]:
                return True
        # check two diagnols
        if state[0][0] == state[1][1] == state[2][2] == self.moves[player]:
            return True
        if state[0][2] == state[1][1] == state[2][0] == self.moves[player]:
            return True

        return False

    def checkDraw(self, state):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.state[i][j] == '':
                    return False
        if self.checkWin(state, (self.turn + 1) % 2) or self.checkWin(state, self.turn % 2):
            return False
        return True

    def drawCircle(self, player):
        colour = self.colours[player]
        # check same rows
        for row in range(0, 3):
            if self.state[row][0] == self.state[row][1] == self.state[row][2] == self.moves[player]:
                for k in range(0, 3):
                    rect = (k * self.block_size, row * self.block_size, self.block_size, self.block_size)
                    pygame.draw.rect(self.screen, colour, rect)

        # check same columns
        for column in range(0, 3):
            if self.state[0][column] == self.state[1][column] == self.state[2][column] == self.moves[player]:
                for k in range(0, 3):
                    rect = (column * self.block_size, k * self.block_size, self.block_size, self.block_size)
                    pygame.draw.rect(self.screen, colour, rect)

        # check two diagnols
        if self.state[0][0] == self.state[1][1] == self.state[2][2] == self.moves[player]:
            for k in range(0, 3):
                rect = (k * self.block_size, k * self.block_size, self.block_size, self.block_size)
                pygame.draw.rect(self.screen, colour, rect)

        if self.state[0][2] == self.state[1][1] == self.state[2][0] == self.moves[player]:
            for k in range(0, 3):
                rect = (k * self.block_size, (2 - k) * self.block_size, self.block_size, self.block_size)
                pygame.draw.rect(self.screen, colour, rect)

        self.displayText()


T = TicTacToe()
