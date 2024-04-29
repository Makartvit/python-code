class ChessFigure:
    def __init__(self, color_figure="white", place_figure=(0, 0)):
        if not self.on_board(place_figure):
            raise ValueError("Ошибка: не в области (0-7).")
        self.color_figure = color_figure
        self.place_figure = place_figure

    def on_board(self, place_figure):
        """(от 0 до 7 по обоим осям)."""
        return 0 <= place_figure[0] <= 7 and 0 <= place_figure[1] <= 7

    def change_color(self):
        """Меняет цвет """
        if self.color_figure == "white":
            self.color_figure = "black"
        else:
            self.color_figure = "white"

    def moving_chess(self, new_place):
        # Перемещает фигуру
        if self.on_board(new_place):
            self.place_figure = new_place
        else:
            print("Ошибка")


class Pawn(ChessFigure):
    def can_move(self, new_place):
        """Проверка области."""
        if not self.on_board(new_place):
            return False

        row_diff = new_place[0] - self.place_figure[0]
        col_diff = new_place[1] - self.place_figure[1]

        if self.color_figure == "white":
            # Белые пешка движутся вниз.
            return row_diff == -1 and col_diff == 0
        else:
            # Черные пешка движутся вверх.
            return row_diff == 1 and col_diff == 0

    def move_pawn(self, new_place):
        """Перемещает, если допустимо"""
        if self.can_move(new_place):
            self.moving_chess(new_place)
        else:
            raise ValueError("Недопустимое перемещение.")


class Bishop(ChessFigure):
    def can_move(self, new_place):
        if not self.on_board(new_place):
            return False

        row_diff = new_place[0] - self.place_figure[0]
        col_diff = new_place[1] - self.place_figure[1]

        if row_diff == col_diff or row_diff == -col_diff:
            return True

    def move(self, new_place):
        """Перемещает, если допустимо"""
        if self.can_move(new_place):
            self.moving_chess(new_place)
        else:
            raise ValueError("Недопустимое перемещение.")


class Rook(ChessFigure):

    def can_move(self, new_place):
        if not self.on_board(new_place):
            return False

        row_diff = new_place[0] - self.place_figure[0]
        col_diff = new_place[1] - self.place_figure[1]

        return row_diff == 0 or col_diff == 0

    def move(self, new_place):
        """Перемещает, если допустимо"""
        if self.can_move(new_place):
            self.moving_chess(new_place)
        else:
            raise ValueError("Недопустимое перемещение.")


class Queen(ChessFigure):

    def can_move(self, new_place):
        if not self.on_board(new_place):
            return False

        row_diff = new_place[0] - self.place_figure[0]
        col_diff = new_place[1] - self.place_figure[1]

        Terms_of_the_Queens_transfer = row_diff == col_diff or row_diff == -col_diff or row_diff == 0 or col_diff == 0

        if Terms_of_the_Queens_transfer:
            return True

    def move(self, new_place):
        """Перемещает, если допустимо"""
        if self.can_move(new_place):
            self.moving_chess(new_place)
        else:
            raise ValueError("Недопустимое перемещение.")


class King(ChessFigure):

    def can_move(self, new_place):
        if not self.on_board(new_place):
            return False

        row_diff = new_place[0] - self.place_figure[0]
        col_diff = new_place[1] - self.place_figure[1]

        Terms_of_the_King_transfer = (-1 <= row_diff <= 1) and (-1 <= col_diff <= 1)

        if Terms_of_the_King_transfer:
            return True

    def move(self, new_place):
        """Перемещает, если допустимо"""
        if self.can_move(new_place):
            self.moving_chess(new_place)
        else:
            raise ValueError("Недопустимое перемещение.")


class Knight(ChessFigure):
    def can_move(self, new_place):
        if not self.on_board(new_place):
            return False

        row_diff = new_place[0] - self.place_figure[0]
        col_diff = new_place[1] - self.place_figure[1]

        # Конь ходит буквой "Г"
        # Проверяем комбинацию шагов
        Terms_of_the_Knight_transfer = (row_diff == 2 and col_diff == 1) or (row_diff == -2 and col_diff == -1) or \
                                       (row_diff == -2 and col_diff == 1) or (row_diff == 2 and col_diff == -1) or \
                                       (row_diff == 1 and col_diff == 2) or (row_diff == -1 and col_diff == -2) or \
                                       (row_diff == 1 and col_diff == -2) or (row_diff == -1 and col_diff == 2)

        return Terms_of_the_Knight_transfer

    def move(self, new_place):
        """Перемещает, если допустимо"""
        if self.can_move(new_place):
            self.moving_chess(new_place)
        else:
            raise ValueError("Недопустимое перемещение.")


class ChessSet:
    def __init__(self):
        # Инициализируем список фигур
        self.figures_list = []

    def add_figure(self, chess_piece):
        # Добавляем фигуру в список
        self.figures_list.append(chess_piece)

    def get_figures(self):
        # Возвращаем список фигур
        return self.figures_list

    def find_movable_figures(self, target_pos):
        # Возвращаем список фигур, которые могут переместиться
        movable_pieces = []
        for piece in self.figures_list:
            if piece.can_move(target_pos):
                movable_pieces.append(piece)  # Добавляем фигуры в этот список
        return movable_pieces  # Возвращаем измененный список


pawn = Pawn("white", (6, 0))

pawn.move_pawn((5, 0))

print("Текущая позиция пешки:", pawn.place_figure)

bishop = Bishop("white", (5, 5))

bishop.moving_chess((3, 3))

bishop.change_color()

print(f"Текущая позиция слона: {bishop.place_figure}, Цвет слона: {bishop.color_figure}")

king = King("white", (2, 7))

king.move((1, 6))

print(f"Текущая позиция king: {king.place_figure}, Цвет king: {king.color_figure}")

knight = Knight("white", (2, 2))

knight.move((4, 3))

print(f"Текущая позиция knight: {knight.place_figure}, Цвет knight: {knight.color_figure}")

chess_set = ChessSet()

# Добавляем фигуры
king = King("white", (4, 7))
rook = Rook("white", (3, 1))
bishop = Bishop("white", (4, 4))
queen = Queen("white", (2, 2))
knight = Knight("white", (5, 5))
pawn = Pawn("white", (6, 6))

chess_set.add_figure(king)
chess_set.add_figure(rook)
chess_set.add_figure(bishop)
chess_set.add_figure(queen)
chess_set.add_figure(knight)
chess_set.add_figure(pawn)

target_position = (1, 1)

# Получаем список фигур, которые могут переместиться в указанное место
movable_figures = chess_set.find_movable_figures(target_position)

print("Фигуры, которые могут попасть в", target_position, ":")
for figure in movable_figures:
    print(figure.__class__.__name__)
