/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const arr = nums.concat()
    nums.sort((a,b)=>a-b)
    let i = 0
    let j = nums.length-1
    while(nums[i]+nums[j]!=target) {
        if(nums[i]+nums[j]>target){
            j--
        }else{
            i++
        }
    }
    i=arr.indexOf(nums[i])
    j=arr.lastIndexOf(nums[j])
    let arr1=[i,j]
    return arr1
};