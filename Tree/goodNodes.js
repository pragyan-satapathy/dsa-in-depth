// https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var goodNodes = function(root) {
    let count = 0

    function isGood(root, good) {
        if (!root) return

        if (root.val >= good) {
            count +=1
            good = root.val
        }

        isGood(root.left, good)
        isGood(root.right, good)
    }
    isGood(root, root.val)
    return count
};