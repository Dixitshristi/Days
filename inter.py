set_a = {1, 2, 3, 4}

list_b = [3, 4, 5, 6]  # Works even as a list

print("A = ",set_a)

print("List B = ",list_b)

result = set_a.intersection(list_b)

print("Using the method with an iterable argument : ", result)  

set_c = {4, 7, 8}

result_multi = set_a.intersection(list_b, set_c)

print("Comparing multiple sets at once : ", result_multi)  
