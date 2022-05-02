lst = [23,45,56,78,99,35]
sorted_list = lambda lst: sorted(lst, reverse=True)
print(sorted_list(lst))
lst = sorted(lst, key=lambda x: x, reverse = False)
print(lst)