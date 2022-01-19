/* 
    Given a string,
    return a new string with the duplicates excluded
    Bonus: Keep only the last instance of each character.
*/

const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "wednesday"
const expected3 = "wednsay"
const expectedBonus3 = "wnesday"

/**
 * De-dupes the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string that may contain duplicates.
 * @returns {string} The given string with any duplicate characters removed.
 */
// function stringDedupe(str) {
//     const splitName = str.split("")
//     const index = array.indexOf(5)
//         for (i = 0; i < splitName.length; i++){ 
//         if (index > -1){
//             array.splice(index, 1);
//         }
//         if (arr[i] == arr[j]) {
//         arr.splice(index,i)
//         }
//     }
// }

// console.log(stringDedupe(str1))







// function stringDedupe(str) {
//     let obj = "";
    
//     for (let i = 0; i < str.length; i++){
//         if(obj.hasOwnProperty(str[i])){
//             obj -= str[i]
//         }
//         else{
//             obj += str[i]
//         }
//     }
//     return obj
// }

// console.log(stringDedupe(str2))


function stringDedupe(str){
    let newString = "";

    for (let i = 0; i < str.length; i++){
        if (newString.hasOwnProperty(str[i])){
            newString -= str[i]
        }
        else{
            newString += str[i]
        }
    }
    return newString
}

console.log(stringDedupe(str2))