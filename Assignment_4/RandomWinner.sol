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

    constructor (address owner, uint256 _minAmount) ... ) {
        // Sets default values
        require(msg.value >= _minAmount, "Please send money.");
        // TODO: complete the constructor
    }

    function max(uint256 a, uint256 b) internal pure returns (uint256) {
        // Returns the max value
        // TODO: complete the function
    }

    function min(uint256 a, uint256 b) internal pure returns (uint256) {
        // Returns the min value
        // TODO: complete the function
    }

    function random() private returns (uint256) {
        // returns random number
        randomNonce++;
        // TODO: complete the function
    }

    function conifgure(uint256 _minAmount, uint256 _dividend, uint256 _divisor) ... {
        // Changes the configurations
        // TODO: complete the function
    }

    function getTotalAmount() public view returns (uint256) {
        // Returns current total amount
        // TODO: complete the function
    }

    function getWinAmount(uint256 amount) public view returns (uint256) {
        // Returns a possible win amount based on the given amount
        uint256 _totalAmount = totalAmount + amount;
        uint256 winAmount = max(min(2 * amount, _totalAmount - minAmount), 0);
        return winAmount;
    }

    function attempt(address payable account) ... {
        // Makes an attemp
        // With probability of dividend/divisor the user wins the amount returned by getWinAmount(),
        // otherwise the amount user sent is added to the total amount
        uint256 amount = msg.value;

        require(amount > 0, "You have to send money.");

        uint256 winAmount = getWinAmount(amount);

        // TODO: complete the function

        if (isWinner) {
            ...
            return "YOU WON";
        } else {
            return "YOU LOST";
        }
    }

}
