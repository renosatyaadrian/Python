import sys, timeit

data_list = [1,2,3,3,4,5,6,7,7,'a','b','c',3.125]
data_tuple = (1,2,3,3,4,5,6,7,7,'a','b','c',3.125)

#List Command
print('We can ',dir(data_tuple))
print('We can ',dir(data_list))

#Count Memory
size_list = sys.getsizeof(data_list)
size_tuple = sys.getsizeof(data_tuple)

print('Memory:',size_list)
print('Memory:',size_tuple)

#Count Time Processing
time_list = timeit.timeit(stmt="1,2,3,4,5,6,7,8,2,8,9",number=100000)
time_tuple = timeit.timeit(stmt="1,2,3,4,5,6,7,8,2,8,9",number=100000)

print('Time :',time_list)
print('Time :',time_tuple)
