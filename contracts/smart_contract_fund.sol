// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SmartContractFund {
    address public owner;
    mapping(address => uint256) public balances;
    mapping(address => bool) public isInvestor;

    event Deposited(address indexed investor, uint256 amount);
    event Withdrawn(address indexed investor, uint256 amount);
    event FundManaged(address indexed manager, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    modifier onlyInvestor() {
        require(isInvestor[msg.sender], "Not an investor");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        if (!isInvestor[msg.sender]) {
            isInvestor[msg.sender] = true;
        }
        balances[msg.sender] += msg.value;
        emit Deposited(msg.sender, msg.value);
    }

    function withdraw(uint256 amount) external onlyInvestor {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);
        emit Withdrawn(msg.sender, amount);
    }

    function manageFund(uint256 amount) external onlyOwner {
        // Logic for managing the fund, e.g., investing in tokens
        emit FundManaged(msg.sender, amount);
    }

    function getBalance() external view onlyInvestor returns (uint256) {
        return balances[msg.sender];
    }
}