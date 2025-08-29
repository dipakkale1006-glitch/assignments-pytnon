#task_1

'''file1=open('Sample.txt.py','r')
reading=file1.read()
print(reading)
file1.close()'''

'''file1=open(Sample.xt.,'r')
reading=file1.read()
print(reading)
file1.close()'''

#task_2








user_input = input("Enter text to the file: ")

with open("output.txt..py", "w") as file:
    file.write(user_input + "\n")


additional_data = input("Enter additional data to append: Learning file handling in pythin. Data successfully appended ")

with open("output.txt", "a") as file:
    file.write(additional_data + "\n")


print("\nFinal content of 'output.txt': \n Hello, python! Learning file handling in python ")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)
