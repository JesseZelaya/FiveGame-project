# Author:Jesse Zelaya
# Date: May 28th, 2020
# Description: Creates 15x15 board for a tic tac toe style game that allows a user to interface game play
#              and checks for wins, draw, and legal moves.


class FiveBoard:
    def __init__(self):
        """
        Class creates 15x15 board for a tic tac toe style game that allows a user to interface game play
        and checks for wins, draw, and legal moves.
        :param self:
        :return:
        """
        row_14 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        row_13 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        row_12 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        row_11 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        row_10 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        row_9 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        row_8 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        row_7 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        row_6 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        row_5 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        row_4 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        row_3 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        row_2 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        row_1 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        row_0 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

        self._board_list = [row_0, row_1, row_2, row_3, row_4,
                            row_5, row_6, row_7, row_8, row_9,
                            row_10, row_11, row_12, row_13, row_14]
        self._board_state = "UNFINISHED"
        self._move_count = 0

    def _check_legal_moves(self, row_to, col_to, piece):
        """
        Checks if there is a legal move to make. If the board state
        is anything, but UNFINISHED then the function returns false
        if the move is legal it returns true.
        :param row_to: row destination
        :param col_to: column destination
        :param piece: x or o
        :return: returns false if not legal, true if legal
        """
        # if the board is not unfinished then it was won/drawn
        if self._board_state != "UNFINISHED":
            #print("game is not unfinished")
            return False
        # make sure the position is empty to make the move
        elif self._board_list[row_to][col_to] != '':
            #print("position is not empty")
            return False
        else:
            return True

    def _check_if_won(self, row_to, col_to, piece):
        """
        Function starts with vertical possible win, it counts pieces upward until it
        hits an empty string or an opposite piece. if that happens then it counts
        downward until it hits an empty string or opposite piece. If the piece count is
        greater than or equal to five it means there was a win.

        The same process is used to determine horizontal and diagonal wins
        :param row_to: row where player wants to move to
        :param col_to: column where player wants to move to
        :return: True if player has won, false if noone has won
        """
        piece_count = 0
        # counts pieces upward from the row_to col_to place
        for i in range(0,5):
            if row_to + i < 15:
                if self._board_list[row_to + i][col_to] == piece:
                    piece_count += 1
                else:
                    break
            else:
                break
        # counts the pieces downward not counting starting place
        for i in range(1, 6):
            if row_to >= 0:
                if self._board_list[row_to - i][col_to] == piece:
                    piece_count += 1
                else:
                    break
            else:
                break
        if piece_count >= 5:
            return True
        # if no vertical win detected then horizontal is checked in the
        # same manner as vertical
        elif piece_count < 5:
            piece_count = 0
            for i in range(0, 5):
                if col_to + i < 15:
                    if self._board_list[row_to][col_to + i] == piece:
                        piece_count += 1
                    else:
                        break
                else:
                    break
            for i in range(1, 6):
                if col_to - 1 >= 0:
                    if self._board_list[row_to][col_to - i] == piece:
                        piece_count += 1
                    else:
                        break
                else:
                    break
            if piece_count >= 5:
                #print("horizontal win")
                return True
            # if no horizontal win then check diagonally from upper right to lower left
            # in the same manner from upper right to lower left
            elif piece_count < 5:
                piece_count = 0
                for i in range(0, 5):
                    if col_to + i < 15 and row_to + i < 15:
                        if self._board_list[row_to + i][col_to + i] == piece:
                            piece_count += 1
                        else:
                            break
                    else:
                        break
                for i in range(1, 6):
                    if col_to - i >= 0 and row_to - i >= 0:
                        if self._board_list[row_to - i][col_to - i] == piece:
                            piece_count += 1
                        else:
                            break
                    else:
                        break
                if piece_count >= 5:
                    #print("backslash won")
                    return True
                # if back slash didn't win then check forward slash
                # in the same manner from the lower left to the upper right diagonal
                elif piece_count < 5:
                    piece_count = 0
                    for i in range(0,5):
                        if row_to + i < 15 and col_to - i >= 0:
                            if self._board_list[row_to + i][col_to - i] == piece:
                                piece_count += 1
                            else:
                                break
                        else:
                            break
                    for i in range(1, 6):
                        if row_to - i >= 0 and col_to + i < 15:
                            if self._board_list[row_to - i][col_to + i] == piece:
                                piece_count += 1
                            else:
                                break
                        else:
                            break
                    if piece_count >= 5:
                        #print("forward slash won")
                        return True
                    else:
                        #print("error or NO WIN")
                        return False

    def get_current_state(self):
        """
        allows player to get current state of the game
        :return: _board_state
        """
        return self._board_state

    def printer(self):
        """
        prints the 15x15 board
        :return: none
        """
        print("\n")
        for nn in range(len(self._board_list) - 1, - 1, - 1):
            print(self._board_list[nn])

    def make_move(self, row_to, col_to, piece):
        """
        allows player to make move. calls on other methods to
        see if the move is legal and updates boardstatus
        depending on wins, draw, or unfinished game
        :param row_to: where player wants to place piece (row)
        :param col_to: where player wants to place piece (column)
        :param piece: x or o char
        :return: True if game won or draw or unfinished, false if no legal
                 move or if game is already won or drawn
        """
        # check if the move is legal and make move
        if self._check_legal_moves(row_to, col_to, piece) is True:
            self._board_list[row_to][col_to] = piece
            self._move_count += 1
            # check if game is won
            if self._check_if_won(row_to, col_to, piece) is True:
                if piece == "x":
                    self._board_state = "X_WON"
                    return True
                elif piece == "o":
                    self._board_state = "O_WON"
                    return True
                # check if game is draw
            elif self._check_draw() is True:
                self._board_state = "DRAW"
                return True
            # return true is legal move was made, but game unfinished (no need to update status)
            else:
                return True
        # return false if no legal move such as already won or drawn
        # or space already taken.
        else:
            return False

    def _check_draw(self):
        """
        checks for a draw if no one has won and board is filled
        :return: True if Draw, False if not
        """
        if self._move_count >= 225 and self._board_state == "UNFINISHED":
            return True
        else:
            return False

# Testing for game

# board = FiveBoard()
# board.make_move(6, 14, 'o')
# board.make_move(5, 14, 'o')
# board.make_move(3, 14, 'o')
# board.make_move(2, 14, 'o')
# board.make_move(1, 14, 'o')
# board.make_move(0, 14, 'o')


board = FiveBoard()
player = 'x'
for row in range(0, 15):
    if player == 'x':
        player = 'o'
    else:
        player = 'x'
    for col in range(0, 15):
        if row == 14 and col == 14:
            continue
        board.make_move(row, col, player)
        if col % 2 == 0:
            if player == 'x':
                player = 'o'
            else:
                player = 'x'
board.printer()

