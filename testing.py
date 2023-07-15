# # Below is for continue
# '''
# for i in range(10):
#     if i == 7:
#         continue
#     else:
#         ("completed")
#         print(i)
# '''
# # Below is for break example
# '''
# for i in range(10):
#     if i == 6:
#         break
#     print(i)
# '''
# # Below is for pass example
# '''
# for i in range(10):
#     if i == 2:
#         pass
#         print(i)
# '''
# import datetime
# # If elif remove my Dictionary
# def first():
#     print("calling first")
# def second():
#     print("callin Second")
# def third():
#     print("calling third")
# def default():
#     print("Calling default")

# var = (int(input("enter the value: ")))
# start = datetime.datetime.now()

# dict = {0:first,
#                1:second,
#                2:third}
# final = dict.get(var, default)
# final()
# '''
# if var == 0:
#     first()
# elif var == 1:
#     second()
# elif var == 2:
#     third()
# else:
#     default()
# end = datetime.datetime.now()
# calculate = (end-start)
# print(calculate)
# '''

for i in range(5):
	if i % 2==0:
		continue
	print(i)
