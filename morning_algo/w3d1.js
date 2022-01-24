/* 
Given an array of ints representing a line of people where the space between
indexes is 1 foot, with 0 meaning no one is there and 1 meaning someone is in
that space,
return whether or not there is at least 6 feet separating every person.
Bonus: O(n) linear time (avoid nested loops that cause re-visited indexes).
*/

const queue1 = [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1];
const expected1 = false;

const queue2 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1];
const expected2 = true;

/**
 * Determines whether each occupied space in the line of people is separated by
 * 6 empty spaces.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<0|1>} queue
 * @returns {Boolean}
 */
function socialDistancingEnforcer(arr) {
    let newObj = {};
    for(let x = 0; x < arr.length; x++){
        if(arr[x] == 1){
            if(newObj['1']){
                newObj['1'] += 1;
            }else{
                newObj['1'] = 1;
                newObj['0'] = 0;
            }
            if(newObj['1'] >= 2){
                if(newObj['0'] < 6){
                    return false
                }else{
                    newObj['0'] = 0;
                }
            }
        }else if(newObj[arr[x]]){
            newObj[arr[x]] += 1;
        }else{
            newObj[arr[x]] = 1;
        }
    }
    return true
}

console.log(socialDistancingEnforcer(queue1))
console.log(socialDistancingEnforcer(queue2))