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
    mapping(address => uint256) private userBalances;
    uint256 private constant DEFAULT_BALANCE = 35;

    constructor (address owner) payable Ownable(owner) {
        // Creates tickets
        tickets.push(Ticket("a1", 10, address(0)));
        tickets.push(Ticket("a2", 10, address(0)));
        tickets.push(Ticket("a3", 10, address(0)));
        tickets.push(Ticket("a4", 10, address(0)));

        tickets.push(Ticket("b1", 20, address(0)));
        tickets.push(Ticket("b2", 20, address(0)));
        tickets.push(Ticket("b3", 20, address(0)));
        tickets.push(Ticket("b4", 20, address(0)));

        tickets.push(Ticket("c1", 30, address(0)));
        tickets.push(Ticket("c2", 30, address(0)));
        tickets.push(Ticket("c3", 30, address(0)));
        tickets.push(Ticket("c4", 30, address(0)));
    }

    function getUserBalance(address user) public view returns (uint256) {
        if (userBalances[user] == 0) {
            return DEFAULT_BALANCE;
        }
        return userBalances[user];
    }

    function addTicket(Ticket memory ticket) public onlyOwner {
        // Adds a ticket
        // TODO: complete the function
        tickets.push(ticket);
    }

    function getTicketIndex(string memory ticketId) private view returns(uint256 index) {
        // Returns ticket index by ticketId
        // TODO: complete the function
        for (uint256 i = 0; i < tickets.length; i++) {
            if (tickets[i].ticketId.equals(ticketId)) {
                return i;
            }
        }
        revert("Ticket not found");
    }

    function getAvailableTickets() public view returns(Ticket[] memory availableTickets) {
        // Returns available tickets (owner is null)
        // TODO: complete the function
        uint256 count = 0;
        
        for (uint256 i = 0; i < tickets.length; i++) {
            if (tickets[i].owner == address(0)) {
                count++;
            }
        }
        availableTickets = new Ticket[](count);
        
        uint256 index = 0;
        for (uint256 i = 0; i < tickets.length; i++) {
            if (tickets[i].owner == address(0)) {
                availableTickets[index] = tickets[i];
                index++;
            }
        }
        
        return availableTickets;
    }

    function checkIfAvailable(string memory ticketId) public view returns(bool isAvailable) {
        // Checks if a ticket is available by ticketId
        // TODO: complete the function
        uint256 index = getTicketIndex(ticketId);
        return tickets[index].owner == address(0);
    }

    function buyTicket(address owner, string memory ticketId) public {
        // Buys a ticket by ticketId
        // TODO: complete the function
        uint256 index = getTicketIndex(ticketId);
        
        require(tickets[index].owner == address(0), "Ticket is not available");
        
        uint256 balance = getUserBalance(owner);
        require(balance >= tickets[index].cost, "Insufficient balance");
        
        if (userBalances[owner] == 0) {
            userBalances[owner] = DEFAULT_BALANCE - tickets[index].cost;
        } else {
            userBalances[owner] = balance - tickets[index].cost;
        }
        
        tickets[index].owner = owner;
    }

    function checkOwnerTicket(address owner, string memory ticketId) public view returns(bool isOwner) {
        // Checks if ticketId is owned by owner
        // TODO: complete the function
        uint256 index = getTicketIndex(ticketId);
        return tickets[index].owner == owner;
    }

    function getOwnerTickets(address owner) public view returns(Ticket[] memory ownerTickets) {
        // Returns all tickets of the given owner
        // TODO: complete the function
        uint256 count = 0;
        
        for (uint256 i = 0; i < tickets.length; i++) {
            if (tickets[i].owner == owner) {
                count++;
            }
        }
        
        ownerTickets = new Ticket[](count);
        
        uint256 index = 0;
        for (uint256 i = 0; i < tickets.length; i++) {
            if (tickets[i].owner == owner) {
                ownerTickets[index] = tickets[i];
                index++;
            }
        }
        
        return ownerTickets;
    }

}
