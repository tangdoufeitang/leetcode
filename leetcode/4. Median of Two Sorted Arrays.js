/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    let nums3 = nums1.concat(nums2) 
    nums3.sort((a,b)=>a-b)
    if(nums3.length%2) {
        let index=parseInt(nums3.length/2)
        return nums3[index]
    }else{
        let index =nums3.length/2-1
        let median = (nums3[index]+nums3[index+1])/2
         return median
    }
};