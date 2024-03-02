import re
def reverse(string):
        truncated = ''
        index = len(string)

        # Loop over the string inversively
        while index > 0:
            truncated += string[index - 1]
            index = index - 1

        return truncated

    
def is_palindrome(string):
        if string == reverse(string):
            return 'The Word "{}" is a palindrome'.format(string)

        return 'The Word "{}" is not a palindrome'.format(string)

def is_palindrome_advanced(string):
        stripped = re.sub(r'[^a-zA-Z]+', '', string)
        reversed = reverse(stripped)

        if stripped.lower() == reversed.lower():
            return 'The Word "{}" is a palindrome'.format(string)

        return 'The Word "{}" is not a palindrome'.format(string)

def find_palindromes(filename=''):
        palindromes = []
        file = open(filename, 'r')

        for line, content in enumerate(file):
            if is_palindrome_advanced(content):
                palindromes.append(content)

        return palindromes
