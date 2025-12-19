from utils import clear_screen
from game import MazeGame
from menu import Menu
from maze_generator import MazeGenerator


class GameApp:
    """Отвечает за запуск, координацию и завершение игрового процесса."""

    def __init__(self) -> None:
        """Инициализация основных настроек игры.

        Attributes:
            self.running: Флаг, отвечающий за работу программы.
            self.difficulties: Список с уровнями игры.
        """
        self.running = True
        self.difficulties = {
            "1": ("Легкий", 9, 7),
            "2": ("Средний", 13, 11),
            "3": ("Сложный", 17, 15),
        }

    def run(self) -> None:
        """ Отвечает за показ меню, запуск уровня и выход из программы."""

        while self.running:
            choice = Menu.show_main_menu()
            if choice in self.difficulties:
                self.play_level(choice)
            elif choice == "4":
                self.running = False
            else:
                input("Неверный ввод. Нажмите Enter...")

    def play_level(self, choice: str) -> None:
        """Отвечает за запуск и управление лабиринтом выбранной сложности

        Args:
            choice: Выбор игрока.
        """

        level_name, width, height = self.difficulties[choice]
        generator = MazeGenerator(width, height)
        maze = generator.generate()
        start = (1, 1)
        exit_pos = (width - 2, height - 2)

        game = MazeGame(maze, start, exit_pos)

        while True:
            clear_screen()
            game.render(level_name)

            if game.is_won():
                print("\n✅ Поздравляем! Вы нашли выход!")
                input("Нажмите Enter, чтобы вернуться в меню...")

                return

            action = input("\nХод: ").strip().lower()

            if action in ("w", "a", "s", "d"):
                game.move(action)
            elif action == "r":
                game.reset()
            elif action == "q":
                menu_choice = Menu.show_pause_menu()
                if menu_choice == "2":

                    return


if __name__ == "__main__":
    app = GameApp()
    app.run()
