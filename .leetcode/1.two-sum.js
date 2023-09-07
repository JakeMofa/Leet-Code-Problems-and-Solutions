/*
 * @lc app=leetcode id=1 lang=javascript
 *
 * [1] Two Sum
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

var twoSum =  function(nums, target){
    let hashmap = {};

    for(let i = 0; i < nums.length; i++){
        // current + x =  target
        // x = target - current
        let complement =  target - nums[i];
        if(complement in hashmap){
            return[i,hashmap[complement]];
        }
        hashmap[nums[i]] = i
    }
}
// @lc code=end

