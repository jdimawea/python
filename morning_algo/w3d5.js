/* 
    Given an int to represent how much change is needed
    calculate the fewest number of coins needed to create that change,
    using the standard US denominations
*/

const cents1 = 25;
const expected1 = { quarter: 1 };

const cents2 = 50;
const expected2 = { quarter: 2 };

const cents3 = 9;
const expected3 = { nickel: 1, penny: 4 };

const cents4 = 99;
const expected4 = { quarter: 3, dime: 2, penny: 4 };


/**
 * Calculates the fewest coins of the standard American denominations needed
 *    to reach the given cents amount.
 * @param {number} cents
 * @param {string} sick
 * @returns {Object<string, number>} - A denomination table where the keys are
 *    denomination names and the value is the amount of that denomination
 *    needed.
 */


function fewestCoinChange(cents) {
    newDict = {}
    while(cents > 0) {
        if(cents >= 25) {
            cents -= 25;
            if("quarter" in newDict) {
                newDict["quarter"] += 1;
            } else {
                newDict["quarter"] = 1;
            }
        } else if(cents >= 10) {
            cents -= 10;
            if("dime" in newDict) {
                newDict["dime"] += 1;
            } else {
                newDict["dime"] = 1;
            }
        } else if(cents >= 5) {
            cents -= 5;
            if("nickle" in newDict) {
                newDict["nickle"] += 1;
            } else {
                newDict["nickle"] = 1;
            }
        } else {
            cents -= 1;
            if("penny" in newDict) {
                newDict["penny"] += 1;
            } else {
                newDict["penny"] = 1;
            }
        }
    }return newDict
}

console.log(fewestCoinChange(cents1))
console.log(fewestCoinChange(cents2))
console.log(fewestCoinChange(cents3))
console.log(fewestCoinChange(cents4))


/* 
    Missing Value
    You are given an array of length N that contains, in no particular order,
    integers from 0 to N . One integer value is missing.
    Quickly determine and return the missing value.
*/

const nums1 = [3, 0, 1];
const expected1 = 2;

const nums2 = [3, 0, 1, 2];
const expected2 = null;
// Explanation: nothing is missing

const nums5 = [2, 5, 9, 1, 0, 7, 6, 8, 4]
const expected5 = 3

/* 
    Bonus: now the lowest value can now be any integer (including negatives),
    instead of always being 0. 
*/

const nums3 = [2, -4, 0, -3, -2, 1];
const expected3 = -1;

const nums4 = [5, 2, 7, 8, 4, 9, 3];
const expected4 = 6;

/**
 * Determines what the missing int is in the given unordered array of ints
 *    which spans from 0 to N where only one int is missing. With this missing
 *    int, a consecutive sequence of ints could be formed from the array.
 * Bonus: Given ints can span from N to M (start and end anywhere).
 * @param {Array<number>} unorderedNums
 * @returns {number|null} The missing integer needed to be able to form an unbroken
 *    consecutive set of integers from the given array or null if none is missing.
 */
function missingValue(unorderedNums) {
    let min = unorderedNums[0]
    let max = unorderedNums[0]
    for(var i = 0; i < unorderedNums.length; i++) {
        if (min > unorderedNums[i]) {
            min = unorderedNums[i];
        }
        if (max < unorderedNums[i]) {
            max = unorderedNums[i];
        }
    }
    while (min < max) {
        if (unorderedNums.includes(min)) {
            min += 1;
        } else {
            return min;
        }
    }return null
}

console.log(missingValue(nums1))
console.log(missingValue(nums2))
console.log(missingValue(nums5))
console.log(missingValue(nums3))
console.log(missingValue(nums4))
