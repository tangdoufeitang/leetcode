/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    const add=(arr)=>{
    			for(let i =1;i<arr.length;i++){
    			if(!(arr[i]-arr[i-1])) {
    				arr.splice(i-1,1)
    				add(arr)
    				break
    			}
    			}
    		}
    		add(nums)
	
    return nums.length
};