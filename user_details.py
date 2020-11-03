
#Taking trainee data from users

# Name:
# Capitalising to meet requirement that all strings start with a capital letter
first_name = input('Please enter your first name').capitalize()
middle_name = input('Please enter your middle name').capitalize()
last_name = input('Please enter your last name').capitalize()

# displaying name: first name - middle name - last name
print(f'Hello, {first_name} {middle_name} {last_name}!')
# can also: 
# print('Hello ' + first_name + ' ' + middle_name + ', ' + last_name + '!')

# Date of Birth
dob = input('Please enter your date of birth in the format DD/MM/YYYY.')
# displaying DOB
print(f'Your date of birth is {dob}.')

# Age
age = int(input('Please enter your age to the nearest year'))
# displaying age
print(f'You are {age} years old.')

# Address 
first_line = input('What is the first line of your address?').capitalize()
house_number = input('What is your house number?')
# I have kept this as a string because some people have letters in their house numbers 
# e.g 123B 
post_code = input('What is your post-code?').upper()
city = input('What is your city?').capitalize()
# displaying full address
print(f'Your address is {house_number} {first_line}, {city}, {post_code}.')
# print('Your address is ' + str(house_number) + ' ' + first_line + ', ' + post_code)


# NI number
national_insurance = input('Please enter your National Insurance Number').upper()
# displaying NI number
print(f'Your National Insurance number is {national_insurance}')
# course applied
course = input('What course are you applying to?').capitalize()
# most recent education
education_level = input('What is the highest level qualification you hold? e.g MSc, BSc').capitalize()
degree_name = input('What is the name of your highest level qualification? e.g Chemistry, English Literature etc.').title()
# okay i did look this one up, but it's good to know I think, I could have used this for the name to take it as one input not 3. 

# displaying education 
print(f'The highest level qualification you hold is {education_level} in {degree_name}.')