
# Password Generator

This is a simple command-line based password generator written in Python. It can be used to generate a secure, random password with varying length and character sets.


## Requirements

```javascript
Python 3.6+
```


## Usage

The password generator is run by executing the password_generator.py file. The generated password will have a default length of 8 characters and include lowercase, uppercase, digits and punctuation characters. To generate a password with different length, or custom character set, provide the necessary parameters to the password_generator function.


## Parameters

- size (int): The length of the generated password (default: 8)

- special_chars (boolean):Whether to include special characters in the generated password (default: True)

- digits (boolean): Whether to include digits in the generated password (default: True)



## Example
```py
password_generator()  # Generates an 8-character long password with lowercase, uppercase, digits and punctuation characters
password_generator(10, special_chars=True, digits=True)  # Generates a 10-character long password with the same characters
password_generator(size=8, special_chars=False, digits=True)  # Generates an 8-character long password with only lowercase, uppercase and digits

```

