"""
Custom preprocessors.
A preprocessing function needs: 
1. One input parameter of the Statement type.
2. To return a Statement instance as well.
"""

def ignore_special_characters(statement):
    """
    Remove any special characters from the statement text.
    """

    import re
    
    #Any special characters that needs to be ignored, should be inserted into this list.
    badChars = ['?']

    temp = ''
    for i in badChars:
        temp += i

    statement.text = re.sub(rf'[{temp}]', '', statement.text)

    return statement
