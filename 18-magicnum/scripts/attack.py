#!/usr/bin/python3
from ape import accounts, project
from rich.console import Console

ADDRESS = "0x8E9F7A27cAdbf3AA6796C103d7c7de1AAa0FC98d"

console = Console()


def attack():
    attacker = accounts.load("ctf")
    attacker.set_autosign(True)
    target_contract = project.Privacy.at(ADDRESS)

    console.print(f"[green]Balance Before The Hack: [magenta]{target_contract.balance}")


    console.print(f"[green]Balance After The Hack: [magenta]{target_contract.balance}")

    assert target_contract.balance == 0



def main():
    attack()


if __name__ == "__main__":
    main()