nums = input('Sample inputs: ').split(',')
n1 = int(nums[0])
n2 = int(nums[1])
if nums[2] == '1':
    re = n1+n2
    print(('output : '+nums[0]+'+'+nums[1]+'='+str(re)))
if nums[2] == '2':
    re = n1-n2
    print(('output : '+nums[0]+'-'+nums[1]+'='+str(re)))
if nums[2] == '3':
    re = n1*n2
    print(('output : '+nums[0]+'*'+nums[1]+'='+str(re)))
if nums[2] == '4':
    re = n1/n2
    print(('output : '+nums[0]+'/'+nums[1]+'='+str(re)))
if nums[2] == '5':
    re = n1**n2
    print(('output : '+nums[0]+'**'+nums[1]+'='+str(re)))
