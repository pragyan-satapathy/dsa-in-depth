// https://leetcode.com/problems/sqrtx/

/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    if (x < 2) return x
    let low = 2
    let high = Math.floor(x/2) // because sqrt of any number < x/2
    while (low <= high) {
        const mid  = Math.floor((low + high) / 2)
        if (mid ** 2 === x) {
            return mid
        }
        if (mid ** 2 > x){
            high = mid -1
        }
        else {
            low = mid + 1
        }
    }
    // example: 30
    return high
};