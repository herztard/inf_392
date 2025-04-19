
// SPDX-License-Identifier: MIT
pragma solidity ~0.8.22;

contract Voting {
    struct Candidate {
        uint256 id;
        string name;
        uint256 votesCount;
    }

    Candidate[] private candidates;
    mapping(address => uint256) private votes;

    constructor(uint256[] memory _ids, string[] memory _names) {
        require(_ids.length == _names.length, "Голосование. длина не свопадает");
        for (uint256 i = 0; i < _ids.length; i++) {
            candidates.push(Candidate({
                id: _ids[i],
                name: _names[i],
                votesCount: 0
            }));
        }
    }

    function _getCandidateIndexById(uint256 candidateId) private view returns (uint256) {
        for (uint256 i = 0; i < candidates.length; i++) {
            if (candidates[i].id == candidateId) {
                return i;
            }
        }
        return candidates.length;
    }

    function vote(uint256 index) public {
        require(index < candidates.length, "Голосование: out of index");

        uint256 prevCandidateId = votes[msg.sender];
        uint256 prevIndex = _getCandidateIndexById(prevCandidateId);

        if (prevIndex < candidates.length) {
            candidates[prevIndex].votesCount--;
        }
        candidates[index].votesCount++;
        votes[msg.sender] = candidates[index].id;
    }

    function getVote() public view returns (uint256 candidateId, string memory candidateName) {
        uint256 votedId = votes[msg.sender];
        uint256 idx = _getCandidateIndexById(votedId);
        require(idx < candidates.length, "Голосование: голос не найден");
        Candidate storage c = candidates[idx];
        return (c.id, c.name);
    }

    function removeVote() public {
        uint256 votedId = votes[msg.sender];
        uint256 idx = _getCandidateIndexById(votedId);
        require(idx < candidates.length, "Voting: no vote to remove");
        candidates[idx].votesCount--;
        delete votes[msg.sender];
    }

    function summary()
        public
        view
        returns (
            uint256[] memory ids,
            string[] memory names,
            uint256[] memory voteCounts
        )
    {
        uint256 len = candidates.length;
        ids = new uint256[](len);
        names = new string[](len);
        voteCounts = new uint256[](len);
        for (uint256 i = 0; i < len; i++) {
            Candidate storage c = candidates[i];
            ids[i] = c.id;
            names[i] = c.name;
            voteCounts[i] = c.votesCount;
        }
    }
}