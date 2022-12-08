class test_class:
    my_list = []

a_list = []
tc1 = test_class()

tc1.my_list = [1,2,3]
a_list.append(tc1)

tc1 = test_class()
tc1.my_list.append(7)

print(a_list)
print(tc1.my_list)