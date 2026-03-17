def get_array_element(array,n):
    return array[n]

def set_array_element(array,n,element):
    array[n] = element

def length_array(array):
    return f"length of array is {len(array)} "

def resize_array(old_array, new_size):
    new_array = [None] * new_size
   
    elements_to_copy = min(len(old_array), new_size)
    
    for i in range(elements_to_copy):
        new_array[i] = old_array[i]
        
    return new_array

def array_element_types(array):
    element_type_array = [None] * len(array) 
    for i in range(len(array)):
        element_type_array[i] = type(array[i])

    return element_type_array
    

test_array = [1,2.5,'the',4,5,6,7]
print(length_array(test_array))

test_array2 =  resize_array(test_array,10)
print(test_array2)

print(length_array(test_array2))

    

print(array_element_types(test_array))