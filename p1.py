#Write a Python program to get a list, sorted in increasing order by
# the last element in each tuple from a given list of non-empty tuples

num=int(input("enter the number of tuples in list: "))
tup_list=[]
for i in range(num):
    input1=input('enter elements of tuple separated by \',\': ')
    tup1=tuple(map(int,input1.split(',')))
    tup_list.append(tup1)
tup_list.sort(key=lambda tup: tup[-1])
print(tup_list)