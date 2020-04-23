from collections import deque
vehicle = ['bus','truck','car']

vehicle.append('motorcycle')
#print(vehicle)

vehicle.extend('12345')
#print(vehicle)

vehicle.insert(2,'becak')
#print(vehicle)

vehicle.insert(6,'becak')
#print(vehicle)

counting = vehicle.count('becak')
#print(vehicle)

vehicle.remove('1')

vehicle.reverse()
#print(vehicle)

print('-'*50)
same = vehicle
same.append('LOOK AT THIS')
print(same)
print(vehicle)

print('-'*50)
diff = vehicle.copy()
diff.reverse()
print(diff)
print('-'*50)
####LIST####

list_stack = []
list_queue = deque()
string_to_list = "This is a sentence with more than six words."

string_to_list = string_to_list.split()

for i in string_to_list:
    list_stack.append(i)
    list_queue.appendleft(i)
print( "The variable created as a stack" ,list_stack)
print( "The variable created as a queue" ,list_queue)
