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
            # Белые пешк движутся вниз.
            return row_diff == -1 and col_diff == 0
        else:
            # Черные пешк движутся вверх.
            return row_diff == 1 and col_diff == 0

    def move_pawn(self, new_place: tuple):
        """Перемещает пешку в новое место"""
        if self.can_move(new_place):
            self.moving_chess(new_place)
        else:
            print("Ошибка")


class Bishop(ChessFigure):
    def can_move(self, new_place):

        if not self.on_board(new_place):
            return False

        row_diff = new_place[0] - self.place_figure[0]
        col_diff = new_place[1] - self.place_figure[1]

        if row_diff == col_diff or row_diff == -col_diff:
            return True


pawn = Pawn("white", (6, 0))

# Попытка переместить пешку на новое место
pawn.move_pawn((5, 0))  # Ожидается перемещение

# Печать текущей позиции после перемещения
print("Текущая позиция пешки:", pawn.place_figure)

bishop = Bishop("white", (5, 5))

bishop.moving_chess = (7, 7)

bishop.change_color()

print(f"Текущая позиция слона: {bishop.place_figure}, Цвет слона: {bishop.color_figure}")
