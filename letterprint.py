letter = '''Dear <|NAME|>,
Warmly Namaste and Greeting !,
You are HIRED in our Company. Welcome To our cloudian Family

Thanks 
Yuvi 

Date: <|DATE|>
'''
name = input("Enter Your Name :\n")
print(name)
date = input("Today's Date:\n")
print(date)
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)
