import random 
import array
# maximum length of password needed

MAX_LEN = 15

# declare arrays of the character that we need in our password
# represented as chars to enable easy string concatenation

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

LOWERCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
'x', 'y', 'z']

UPPERCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W'
'X', 'Y', 'Z']

SYMBOLS = ['@', '!', '#', '$','%','^','&','*','()']

#combines all the character arrays above to form one array
COMBINED_LIST = DIGITS + LOWERCASE_CHARACTERS + UPPERCASE_CHARACTERS + SYMBOLS

#randomly select at least one character from each character set above

random_digit = random.choice(DIGITS)
random_upper = random.choice(UPPERCASE_CHARACTERS)
random_lower = random.choice(LOWERCASE_CHARACTERS)
random_symbol = random.choice(SYMBOLS)

#combine the character randomly selected above
# at this point, the password contains only 4 characters but we want a 10 -character password

temporal_password = random_digit + random_upper + random_lower + random_symbol

# it is now certain that we have atleast one character from each set of characters
# we fill the rest of the password length by selecting randomly from the combined list of character above

for x in range(MAX_LEN - 3):
    temporal_password = temporal_password + random.choice(COMBINED_LIST)

# convert temporary password into array and shuffle to prevent it from having a consistent pattern
# where the beginning of the password is predictable

    temporal_password_list = array.array('u', temporal_password)
    random.shuffle(temporal_password_list) 

# transverse the temporary password array and append the chars to form the password

password = " "

for x in temporal_password_list:
    password = password + x

#print out the password

print(password)