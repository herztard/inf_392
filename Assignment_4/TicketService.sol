// contracts/TicketService.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import "@tw3/solidity/contracts/utils/String.sol";
import "@openzeppelin/contracts/access/Ownable.sol";


contract TicketService is Ownable {

    using String for string;

    struct Ticket {
        string ticketId;
        uint256 cost;
        address owner;
    }

    Ticket[] private tickets;

    constructor (address owner) payable Ownable(owner) {
        // Creates tickets
        tickets.push(Ticket("a1", 100000, address(0)));
        tickets.push(Ticket("a2", 100000, address(0)));
        tickets.push(Ticket("a3", 100000, address(0)));
        tickets.push(Ticket("a4", 100000, address(0)));

        tickets.push(Ticket("b1", 200000, address(0)));
        tickets.push(Ticket("b2", 200000, address(0)));
        tickets.push(Ticket("b3", 200000, address(0)));
        tickets.push(Ticket("b4", 200000, address(0)));

        tickets.push(Ticket("c1", 300000, address(0)));
        tickets.push(Ticket("c2", 300000, address(0)));
        tickets.push(Ticket("c3", 300000, address(0)));
        tickets.push(Ticket("c4", 300000, address(0)));
    }

    function addTicket(Ticket memory ticket) public onlyOwner {
        // Adds a ticket
        // TODO: complete the function
    }

    function getTicketIndex(string memory ticketId) private view returns(uint256 index) {
        // Returns ticket index by ticketId
        // TODO: complete the function
    }

    function getAvailableTickets() public view returns(Ticket[] memory availableTickets) {
        // Returns available tickets (owner is null)
        // TODO: complete the function
    }

    function checkIfAvailable(string memory ticketId) public view returns(bool isAvailable) {
        // Checks if a ticket is available by ticketId
        // TODO: complete the function
    }

    function buyTicket(address owner, string memory ticketId) public payable {
        // Buys a ticket by ticketId
        // TODO: complete the function
    }

    function checkOwnerTicket(address owner, string memory ticketId) public view returns(bool isOwner) {
        // Checks if ticketId is owned by owner
        // TODO: complete the function
    }

    function getOwnerTickets(address owner) public view returns(Ticket[] memory ownerTickets) {
        // Returns all tickets of the given owner
        // TODO: complete the function
    }

}
