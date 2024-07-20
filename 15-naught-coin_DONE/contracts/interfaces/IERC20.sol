// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;


interface IERC20 {
    function approve(address spender, uint256 value) external virtual returns (bool);
    function transferFrom(address from, address to, uint256 value) external virtual returns (bool);
    function balanceOf(address account) external view virtual returns (uint256);
}