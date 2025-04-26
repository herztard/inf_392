// contracts/RandomWinner.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import "@openzeppelin/contracts/access/Ownable.sol";

contract RandomWinner is Ownable {

    uint256 private totalAmount;
    uint256 private dividend;
    uint256 private divisor;
    uint256 private randomNonce;
    uint256 private minAmount;

    constructor (address owner, uint256 _minAmount) Ownable(owner) payable {
        // Sets default values
        require(msg.value >= _minAmount, "Please send money.");
        // TODO: complete the constructor
        minAmount = _minAmount;
        totalAmount = msg.value;
        dividend = 1;
        divisor = 4;
        randomNonce = 0;
    }


    function max(uint256 a, uint256 b) internal pure returns (uint256) {
        // Returns the max value
        // TODO: complete the function
        return a > b ? a : b;
    }

    function min(uint256 a, uint256 b) internal pure returns (uint256) {
        // Returns the min value
        // TODO: complete the function
        return a < b ? a : b;
    }

    function random() private returns (uint256) {
        // returns random number
        randomNonce++;
        // TODO: complete the function
        return uint256(keccak256(abi.encodePacked(block.timestamp, block.prevrandao, msg.sender, randomNonce))) % divisor;
    }

    function conifgure(uint256 _minAmount, uint256 _dividend, uint256 _divisor) public onlyOwner {
        // Changes the configurations
        // TODO: complete the function
        require(_divisor > 0, "Divisor must be greater than 0");
        require(_dividend <= _divisor, "Dividend must be less than or equal to divisor");
        minAmount = _minAmount;
        dividend = _dividend;
        divisor = _divisor;
    }

    function getTotalAmount() public view returns (uint256) {
        // Returns current total amount
        // TODO: complete the function
        return totalAmount;
    }

    function getWinAmount(uint256 amount) public view returns (uint256) {
        // Returns a possible win amount based on the given amount
        uint256 _totalAmount = totalAmount + amount;
        uint256 winAmount = max(min(2 * amount, _totalAmount - minAmount), 0);
        return winAmount;
    }

    function attempt(address payable account) public payable returns (string memory) {
        // Makes an attemp
        // With probability of dividend/divisor the user wins the amount returned by getWinAmount(),
        // otherwise the amount user sent is added to the total amount
        uint256 amount = msg.value;

        require(amount > 0, "You have to send money.");

        uint256 winAmount = getWinAmount(amount);

        // TODO: complete the function
        
        bool isWinner = random() < dividend;

        if (isWinner) {
            totalAmount = totalAmount - winAmount;
            account.transfer(winAmount);
            return "YOU WON";
        } else {
            totalAmount = totalAmount + amount;
            return "YOU LOST";
        }
    }

}