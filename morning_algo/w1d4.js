/* 
    String: Is Palindrome
    Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards

    Do not ignore spaces, punctuation and capitalization
 */

    const str1 = "a x a";
    const expected1 = true;

    const str2 = "racecar";
    const expected2 = true;

    const str3 = "Dud";
    const expected3 = false;

    const str4 = "oho!";
    const expected4 = false;

/**
   * Determines if the given str is a palindrome (same forwards and backwards).
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str
   * @returns {boolean} Whether the given str is a palindrome or not.
   */
    
newstring = ""
function isPalindrome(str) {
var re = /[^A-Za-z0-9]/g;
str = str.toLowerCase().replace(re, '');
var len = str.length;
for (var i = 0; i < len/2; i++) {
    if (str[i] !== str[len - 1 - i]) {
        return false;
    }
    }
    return true;
}
isPalindrome(str1);

