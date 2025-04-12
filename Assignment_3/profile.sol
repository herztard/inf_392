
// SPDX-License-Identifier: MIT
pragma solidity ~0.8.22;


contract Profile {

    struct ProfileData {
        // TODO: define struct properties
    }
    
    mapping (address => ProfileData) profiles;

    function setProfile(string memory username, string memory firstName, string memory lastName, string memory email) ... {
        // TODO: set profile
    }

    function getProfile() ... {
        // TODO: get profile
    }

    function removeProfile() ... {
        // TODO: remove profile
    }
}
