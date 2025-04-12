
// SPDX-License-Identifier: MIT
pragma solidity ~0.8.22;


contract Voting {

    struct Candidate {
        uint256 id;
        string name;
        uint256 votesCount;
    }

    Candidate[] private candidates;
    mapping (address => uint256) private votes;

    constructor() {
        // TODO: init several candidates
    }

    function _getCandidateIndexById(uint256 candidateId) private view returns(uint256) {
        for (uint256 i = 0; i < candidates.length; i++) {
            if (candidates[i].id == candidateId) {
                return i;
            }
        }
        return candidates.length;
    }

    function vote(uint256 index) ... {
        if (index >= candidates.length) return;
        uint256 votedIndex = _getCandidateIndexById(votes[msg.sender]);
        bool isNewVote = votedIndex == candidates.length;

        // TODO: complete the function
        // Hint: If it is a new vote from the user, then increment the votes count of the voting candidate.
        // If the user is changing his vote, then decrement the old candidate's votes count and increment the votes count of a new one.

        votes[msg.sender] = candidate.id;
    }

    function getVote() ... {
        uint256 votedIndex = _getCandidateIndexById(votes[msg.sender]);
        if (votedIndex == candidates.length) revert("No votes");
        // TODO: complete the function.
    }

    function removeVote() ... {
        uint256 votedIndex = _getCandidateIndexById(votes[msg.sender]);
        if (votedIndex == candidates.length) revert("No votes");
        // TODO: complete the function
        // Hint: Decrement the old candidate's votes count.
    }

    function summary() ... {
        // TODO: complete the function
        // Hint: Return summary about the votes, so people can see the votes of all candidates
    }
}
