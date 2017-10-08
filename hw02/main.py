def bin_search(data_list, x):    
    low = 0                             
    high = len(data_list) - 1          
    while low <= high:        
        mid = (low + high) // 2             
        if data_list[mid] == x:               
            return mid        
        elif data_list[mid] > x:              
            high = mid - 1        
        else:                                   
            low = mid + 1    
    return 
print(bin_search([1,2,3,4,5], 4))
