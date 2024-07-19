// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract GatekeeperOne {
    address public entrant;

    modifier gateOne() {
        require(msg.sender != tx.origin);
        _;
    }

    modifier gateTwo() {
        require(gasleft() % 8191 == 0);
        _;
    }

    modifier gateThree(bytes8 _gateKey) {
        /* 
        # Gate 1
        bytes8 = 16 hex chars
        1 byte = 8 bits
        8 bytes = 64 bits
        bytes8 _gateKey = uint64(_gateKey) just numerical representation
        uint32(uint64(_gateKey) -> truncate first 32 bits i.e. 4 bytes
        uint16(uint64(_gateKey) -> truncate first 16 bits i.e. 2 bytes
        B1 B2 B3 B4 == 0 0 B3 B4
        B1 B2 B3 B4 != 1 0 B3 B4
        */
        require(uint32(uint64(_gateKey)) == uint16(uint64(_gateKey)), "GatekeeperOne: invalid gateThree part one");
        require(uint32(uint64(_gateKey)) != uint64(_gateKey), "GatekeeperOne: invalid gateThree part two");
        require(uint32(uint64(_gateKey)) == uint16(uint160(tx.origin)), "GatekeeperOne: invalid gateThree part three");
        _;
    }

    function enter(bytes8 _gateKey) public gateOne gateTwo gateThree(_gateKey) returns (bool) {
        entrant = tx.origin;
        return true;
    }
}
