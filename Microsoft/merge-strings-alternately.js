// https://leetcode.com/problems/merge-strings-alternately/description/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days
// https://leetcode.com/problems/merge-strings-alternately/submissions/1493876930/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days

var mergeAlternately = function(word1, word2) {
    let result = ''
    const minLen = Math.min(word1.length, word2.length)
    for (let i = 0; i < minLen; i++){
        result += word1[i]+word2[i]
    }
    if (word1.length > minLen) {
        result += word1.slice(minLen, word1.length)
    }else {
        result += word2.slice(minLen, word2.length)
    }
    return result
};