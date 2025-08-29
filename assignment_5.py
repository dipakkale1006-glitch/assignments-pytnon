#task_1
dictionary={'Alice':85,'mick':70,'nick':65}
input=input("Enter the student's name: ")
if input in dictionary:
    print(input,"'s marks:",dictionary[input])
else:
    print('Student not found')


#task_2

original_list=[1,2,3,4,5,6,7,8,9,10]
print('original list:',original_list)
extracted_liat= (original_list[0:5])
print('Exttacted frist five element:',extracted_liat)
extracted_liat.reverse()
print('Reversed extracted element:',extracted_liat)





