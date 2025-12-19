import os


def clear_screen() -> None:
    """Очищает консоль в зависимости от операционной системы."""

    os.system("cls" if os.name == "nt" else "clear")
