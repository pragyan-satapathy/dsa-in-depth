// https://leetcode.com/problems/power-of-two/


/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function(n) {
    if (n == 1) return true
    // n<1: analyze for n = 6 (6/2,3/2,1.5/2)
    if ((n % 2) !== 0 || n<1) return false
    return isPowerOfTwo(n/2)
};