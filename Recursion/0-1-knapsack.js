function knapsack(wt, price, sackCapacity, n) {
    if (n === 0 || sackCapacity === 0) {
        return 0
    }
    if (wt[n - 1] <= sackCapacity) {
        return Math.max((price[n - 1] + knapsack(wt, price, sackCapacity - wt[n-1], n - 1)),
        knapsack(wt, price, sackCapacity, n - 1))
    }
    return knapsack(wt, price, sackCapacity, n - 1)
}

console.log(knapsack([3,2,1,6], [20,1,2,25], 6, 4))