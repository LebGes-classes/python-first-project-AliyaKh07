import random


class MazeGenerator:
    """Генерирует лабиринт с использованием алгоритма Recursive Backtracker."""

    def __init__(self, width: int, height: int) -> None:
        """Инициализация размерной сетки лабиринта.

        Args:
            width: Ширина лабиринта.
            height: Высота лабиринта.
        """

        if width % 2 == 0:
            width += 1

        if height % 2 == 0:
            height += 1

        self.width = width
        self.height = height

    def generate(self) -> list:
        """ Функция для генерации лабиринта.

        Returns:
            maze: Лабиринт.
        """

        maze = [[1 for _ in range(self.width)] for _ in range(self.height)]
        start_x, start_y = 1, 1
        self._carve(maze, start_x, start_y)
        maze[start_y][start_x] = 0
        maze[self.height - 2][self.width - 2] = 2  # выход

        return maze

    def _carve(self, maze: list, x: int, y: int) -> None:
        """ Рекурсивная функция для вырезания проходов в лабиринте.

        Args:
            maze: Лабиринт.
            x: Координата х.
            y: Координата y.

        Returns:
            None
        """

        maze[y][x] = 0
        directions = [(0, -2), (2, 0), (0, 2), (-2, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            compare_nx = 1 <= nx < self.width - 1
            compare_ny = 1 <= ny < self.height - 1

            if compare_nx and compare_ny and maze[ny][nx] == 1:
                maze[y + dy // 2][x + dx // 2] = 0

                self._carve(maze, nx, ny)
