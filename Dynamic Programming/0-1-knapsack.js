const sackCapacity = 6
const n = 4
const matrix = Array.from({ length: sackCapacity+1 }, () => new Array(n+1).fill(null));


function knapsack(wt, price, sackCapacity, n) {
    if (n === 0 || sackCapacity === 0) {
        return 0
    }
    if(matrix[sackCapacity][n]) {
        return matrix[sackCapacity][n]
    }
    if (wt[n - 1] <= sackCapacity) {
        matrix[sackCapacity][n] = Math.max((price[n - 1] + knapsack(wt, price, sackCapacity - wt[n-1], n - 1)),
        knapsack(wt, price, sackCapacity, n - 1))
        return matrix[sackCapacity][n]
    }
    matrix[sackCapacity][n] = knapsack(wt, price, sackCapacity, n - 1)
    return matrix[sackCapacity][n]
}

console.log(knapsack([3,2,1,6], [20,1,2,25], sackCapacity, n))