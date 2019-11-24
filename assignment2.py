In [8]:
sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
if(avg>=90):
    print("Grade: A")
elif(avg >=80 and avg<90):
    print("Grade: B")
elif(avg >=70 and avg<80):
    print("Grade: C")
elif(avg >=60 and avg<70):
    print("Grade: D")
else:
    print("Grade: F")
Enter marks of the first subject: 85
Enter marks of the second subject: 90
Enter marks of the third subject: 75
Enter marks of the fourth subject: 87
Enter marks of the fifth subject: 78
Grade: B
In [3]:
number = int(input("Enter a number: "))
if (number % 2) == 0:
   print("{0} is Even".format(number))
else:
   print("{0} is Odd".format(number))
Enter a number: 3
3 is Odd
In [4]:
length_of_the_list = [2, 6, 8, 'a','b','c', 20, 25, 90]
print("Lenght of the list = ", len(length_of_the_list))
Lenght of the list =  9
In [5]:
lst = []
numeric_item = int(input('How many numeric items: '))
for n in range(numeric_item):
    numbers = int(input('Enter numeric number '))
    lst.append(numbers)
print("Sum of all the numeric item is :", sum(lst))
How many numeric items: 5
Enter numeric number 1
Enter numeric number 2
Enter numeric number 3
Enter numeric number 4
Enter numeric number 5
Sum of all the numeric item is : 15
In [6]:
lst = []
numeric_number = int(input('How many numbers: '))
for n in range(numeric_number):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Lasrgest number from a numeric list is :", max(lst), )
How many numbers: 5
Enter number 12
Enter number 34
Enter number 21
Enter number 1
Enter number 5
Lasrgest number from a numeric list is : 34
In [7]:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
for x in a:
    if x<5:
        new_list.append(x)
print(new_list)
[1, 1, 2, 3]
In [ ]:

