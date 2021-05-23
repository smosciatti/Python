#example 1 sorted list
# data = [4,5,104,105,110,120,130,130,150,
#         160,170,183,185,187,188,191,350,360]
#
# min_vaid = 100
# max_valid = 200
# #process to the low values in the list
# stop = 0
# for index, value in enumerate(data):
#     if value >= min_valid:
#         stop = index
#         break
# print (stop) #debug purpose
# del data[:stop]
# print(data)
#
# #process the high values in the list
# start = 0
# for index in range(len(data) -1, -1,-1): #-1 because otherwise not include first
#    # print (index)
#     if data [index] = max_valid:
#         start = index + 1  #we need to exclude , otherwise will be delete too
#         break
# print (start) #debugging
# del data [ start:]
# print (data)

#example 2 unsorted list too
data =[ 104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]
min_valid = 100
max_valid = 200
print(data)
#mode 1
#for index in range(len(data) -1, -1,-1):
#    print(index)
#     if data[index] < min_valid or data[index] > max_valid:
#         print (index,data)
#         del data[index]

#mode2 reverse
top_index = len(data) -1
for index, value  in enumerate (reversed (data)):

    if value < min_valid or value > max_valid:

        print (top_index - index, value)
        del data[top_index - index]
print (data)