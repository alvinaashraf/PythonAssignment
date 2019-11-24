val1 = input('enter first vale ')
val2 = input('enter second value ')
operator = input('enter operator ')
val1 = int(val1)
val2 = int(val2)

if operator == '+':
    val = val1 + val2
    print(val, 'answer')
elif operator == '-':
    val = val1 - val2
    print(val, 'answer')
elif operator == '*':
    val = val1 * val2
    print(val, 'answer')
elif operator == '/':
    val = val1 / val2
    print(val, 'answer')
else:
    print('enter correct operator')



name = ['noman', 'shahzad', 'faisal', 'feroz', 'hussain' ,'7 ']

val = input('enter value ')

for numeric_value in name:
    if val == '7':
        print('there is the numeric value')
        break
    else:
        print('there is no numeric value ')
        break


customer = {
    "f_name": "Shahid",
    "l_name": "Hashmani",
    "add": "DHA"
}
customer["language"] = "English"
print(customer)




numeric_items = {'a':500,'b':1000,'c':800}
print(sum(numeric_items.values()))


list_of_values = [20,30,40,50,60,30,70,80,40,90,70,100]
list_of_values.sort()
for duplicate_values in range (len (list_of_values) -1):
    if list_of_values[duplicate_values] == list_of_values[duplicate_values+1]:
        print (list_of_values[duplicate_values])



grocery_list = {1: "milk", 2: "oil", 3: "tea", 4: "cosmetics", 5: "tissue_paper", 6: "rice"}
def is_key_exist(x):
  if x in grocery_list:
      print('Key is already exist in a dictionary')
  else:
      print('Key is not exist in a dictionary')
is_key_exist(3)



