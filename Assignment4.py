
person = {
    "first_name": "Javed",
    "last_name": "Choudhry",
    "age": 50,
    "city": "Islamabad",
    }
print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person['city'])

person = {
    
    "first_name": "Javed",
    "last_name": "Choudhry",
    "age": 50,
    "city": "Islamabad",
}
   
person["qualification"] = "Master"
print(person)

person = {
    
    "first_name": "Javed",
    "last_name": "Choudhry",
    "age": 50,
    "city": "Islamabad",
    "qualification": "MASTER"
}
person["qualification"] = "Phd"  
print(person)

del person["qualification"]  
print(person)





    cities = [
    {
        "islamabad": 1,
        "country": "Pakistan",
        "Population": "1.1 million",
        "fact": "Capital"
    },
    {
        "new_york": 2,
        "country": "United States",
        "Population": "8.5 million",
        "fact": "largest city in the UInited States"
    },

     {
        "makkah": 3,
        "country": "Saudi Arabia",
        "Population": "1.67 million",
        "fact": "holiest city of muslim"
     }
]
print(cities)


#QUESTION NO. 3


prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")


def favorite_book(title):
       print(title + " is one of my favorite books.")

favorite_book('Khutbat E Bahawal Pur By Dr. Muhammad Hamidullah')


from random import randint

print ("random number between 1 - 30."
       "\nuser guess the number!")

number = 0

while number < 1 or number >30:
    number = int(input("\n\nEnter a number: "))
    if number > 30:
        print ("Number must be lower than!")
    if number < 1:
        print ("Number must be greater than!")

guess = randint(1, 30)

print ("The user takes a guess...", guess)

while guess != number:
    if guess > number:
        guess -= 1
        guess = randint(1, guess)
    else:
        guess += 1
        guess = randint(guess, 30)
    print ("The user takes a guess...", guess)

print ("The user guessed", guess, "and it was correct!")


