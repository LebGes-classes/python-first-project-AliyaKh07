class Renderer:
    """Отвечает за отображение лабиринта в консоли."""

    SYMBOLS = {
        "wall": "██",
        "path": "  ",
        "player": "● ",
        "exit": "★ ",
    }

    @staticmethod
    def render(maze: list, player_pos: tuple, level_name: str) -> None:
        """Метод, отвечающий за отображение лабиринта на консоли.

        Args:
            maze: Лабиринт.
            player_pos: Позиция игрока.
            level_name: Название уровня сложности

        Returns:
            None.
            """

        print(f"\n== Уровень сложности: {level_name} ==", end='\n')

        for y, row in enumerate(maze):
            line = ""

            for x, cell in enumerate(row):
                if (x, y) == player_pos:
                    line += Renderer.SYMBOLS["player"]
                elif cell == 1:
                    line += Renderer.SYMBOLS["wall"]
                elif cell == 2:
                    line += Renderer.SYMBOLS["exit"]
                else:
                    line += Renderer.SYMBOLS["path"]

            print(line)

        print("\nУправление: W/A/S/D | R — перезапуск | Q — меню")

