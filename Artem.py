from Makogon_6 import Pawn, Rook, Knight, Bishop, Queen, King


class ChessFigure:
    def __init__(self, color, place):
        if not self.is_within_board(place):
            raise ValueError("Ошибка: вне пределов шахматной доски.")
        self.color = color
        self.place = place

    def is_within_board(self, place):
        return 0 <= place[0] <= 7 and 0 <= place[1] <= 7

    def move(self, new_place):
        if self.can_move(new_place):
            self.place = new_place
        else:
            raise ValueError("Недопустимое перемещение.")


# Класс шахматной доски
class ChessBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]  # 8x8 пустая доска

    def place_figure(self, figure):
        x, y = figure.place
        if self.board[x][y] is not None:
            raise ValueError("Ошибка: Клетка занята.")
        self.board[x][y] = figure  # Помещаем фигуру на доску

    def move_figure(self, start, end):
        if not self.is_within_board(start) or not self.is_within_board(end):
            raise ValueError("Ошибка: вне пределов доски.")
        figure = self.board[start[0]][start[1]]
        if figure is None:
            raise ValueError("Ошибка: в начальной клетке нет фигуры.")
        figure.move(end)  # Перемещаем фигуру
        self.board[end[0]][end[1]] = figure  # Обновляем позицию на доске
        self.board[start[0]][start[1]] = None  # Очищаем начальную позицию

    def is_within_board(self, place):
        return 0 <= place[0] <= 7 and 0 <= place[1] <= 7


# Класс шахматной игры
class ChessGame:
    def __init__(self):
        self.board = ChessBoard()  # Создаем доску
        self.turn = "white"  # Начало с белых
        self.setup_board()  # Устанавливаем начальные позиции фигур

    def setup_board(self):
        # Добавляем пешки
        for i in range(8):
            self.board.place_figure(Pawn("white", (6, i)))
            self.board.place_figure(Pawn("black", (1, i)))

        # Добавляем другие фигуры
        figures = [
            Rook("white", (7, 0)), Rook("white", (7, 7)),
            Rook("black", (0, 0)), Rook("black", (0, 7)),
            Knight("white", (7, 1)), Knight("white", (7, 6)),
            Knight("black", (0, 1)), Knight("black", (0, 6)),
            Bishop("white", (7, 2)), Bishop("white", (7, 5)),
            Bishop("black", (0, 2)), Bishop("black", (0, 5)),
            Queen("white", (7, 3)), Queen("black", (0, 3)),
            King("white", (7, 4)), King("black", (0, 4)),
        ]

        for figure in figures:
            self.board.place_figure(figure)  # Расставляем фигуры на доске

    def switch_turn(self):
        # Меняем ход с белых на черных или наоборот
        self.turn = "white" if self.turn == "black" else "black"

    def play(self, start, end):
        # Метод для игры: перемещаем фигуры и меняем ход
        self.board.move_figure(start, end)  # Перемещаем фигуру
        self.switch_turn()  # Меняем ход

    def display_board(self):
        # Отображаем доску в текстовом формате
        for row in self.board.board:
            for cell in row:
                if cell:
                    print(f"{cell.__class__.__name__[0]}{cell.color[0]}", end=" ")
                else:
                    print(".", end=" ")
            print()  # Переходим на следующую строку