def has22(nums):
    for x in range(0,len(nums)):
        if (nums[x] == 2) and (nums[x+1] == 2):
        	print True
		break
    print False
has22([1,2,2])
