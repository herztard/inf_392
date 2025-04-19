
// SPDX-License-Identifier: MIT
pragma solidity ~0.8.22;


contract Profile {
    struct ProfileData {
        string username;
        string firstName;
        string lastName;
        string email;
    }

    mapping(address => ProfileData) private profiles;

    function setProfile(
        string memory username,
        string memory firstName,
        string memory lastName,
        string memory email
    ) public {
        profiles[msg.sender] = ProfileData({
            username: username,
            firstName: firstName,
            lastName: lastName,
            email: email
        });
    }

    function getProfile()
        public
        view
        returns (
            string memory username,
            string memory firstName,
            string memory lastName,
            string memory email
        )
    {
        ProfileData storage p = profiles[msg.sender];
        require(bytes(p.username).length > 0, "Profile: not set");
        return (p.username, p.firstName, p.lastName, p.email);
    }

    function removeProfile() public {
        ProfileData storage p = profiles[msg.sender];
        require(bytes(p.username).length > 0, "Profile: not set");
        delete profiles[msg.sender];
    }
}
