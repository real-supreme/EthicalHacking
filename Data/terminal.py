from os import name, system


def clear_terminal_screen():
    # for windows
    if name == "nt":
        system("cls")

    # for linux
    else:
        system("clear")
        system("tput reset")
