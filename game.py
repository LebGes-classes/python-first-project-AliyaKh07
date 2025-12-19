from renderer import Renderer


class MazeGame:
    """Управляет логикой одного уровня игры."""

    def __init__(self, maze: list, start_pos: tuple, exit_pos: tuple) -> None:
        """Инициализация состояния игры.

        Args:
            maze: Лабиринт.
            start_pos: Начальная  позиция игрока.
            exit_pos: Конечная позиция игрока.

        Attributes:
            self.player_pos: Текущая позиция игрока.
         """

        self.maze = maze
        self.player_pos = list(start_pos)
        self.exit_pos = exit_pos
        self.start_pos = list(start_pos)

    def move(self, direction: str) -> None:
        """ Отвечает за перемещение игрока по лабиринту

        Args:
            direction: Направление движения.
        """

        dx, dy = 0, 0

        if direction == "w":
            dy = -1
        elif direction == "s":
            dy = 1
        elif direction == "a":
            dx = -1
        elif direction == "d":
            dx = 1
        else:

            return # если введено что-то неверное, ничего не будет происходить

        new_x = self.player_pos[0] + dx
        new_y = self.player_pos[1] + dy

        if (
            0 <= new_y < len(self.maze)
            and 0 <= new_x < len(self.maze[0])
            and self.maze[new_y][new_x] != 1
        ):
            self.player_pos = [new_x, new_y]

    def is_won(self)-> bool:
        """Проверяет, достиг ли игрок выхода.

        Returns:
            True, если текущая позиция игрока совпадает с конечной.
            False, если текущая позиция игрока не совпадает с конечной.
        """

        return tuple(self.player_pos) == self.exit_pos

    def reset(self) -> None:
        """Сбрасывает позицию игрока к началу уровня."""

        self.player_pos = self.start_pos[:]

    def render(self, level_name: str) -> None:
        """Рисует лабиринт в зависимости от уровня игры."""

        Renderer.render(self.maze, tuple(self.player_pos), level_name)
        