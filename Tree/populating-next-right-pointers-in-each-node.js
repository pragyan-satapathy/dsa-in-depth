// https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/


// Iterative way
// ===============
var connect = function(root) {
    if (!root) return root
    let q = [root]
    while(q.length) {
        const s = q.length
        let  i = 0
        let b = []
        while(i < s) {
            i++
            let a = q.shift()
            
            if (q[0] || (q[0] == 0))  a.next = q[0] 
            else {
                a.next = null
            }
            a.left && b.push(a.left)
            a.right && b.push(a.right)

        }
        q = [...b]
    }
    return root
};



// recursive -1
// ============
var connect = function(root) {
    if (!root) return root
    let ans = []
    let traversal = (curr, level) => {
        if (!ans[level]) {
            ans[level] = []
        }
        ans[level].push(curr)
        curr.left && traversal(curr.left, level + 1)
        curr.right && traversal(curr.right, level + 1)
    }
    traversal(root,0)
    for(let i in ans) {
        for(let j in ans[i]) {
            ans[i][j].next = ans[i][Number(j)+1] || null
        }
    }
    return root
};




// recursive -2
// ============
var connect = function(root) {
    if (!root) return root
    function link(curr) {
        if (curr.left) curr.left.next = curr.right
        if (curr.right && curr.next) {
            curr.right.next  = curr.next.left
        }
        curr.left && link(curr.left)
        curr.right && link(curr.right)
    }
    link(root)
    return root
};