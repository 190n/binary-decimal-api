#!/usr/bin/env python3

import cgi
import cgitb
import json


def binary_to_decimal(binary):
    total = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            exponent = len(binary) - i - 1
            total += 2 ** exponent
    return total


# Tell the client that we are sending JSON data (as opposed to HTML or plain text)
print('Content-Type: application/json\r\n\r\n')

# Create object to access query string parameters
form = cgi.FieldStorage()
# Save the binary value that was sent
binary = form.getvalue('binary')
if binary is not None:      # If a binary value was sent, respond with a JSON representation of the
                            # decimal equivalent
    print(json.dumps({
        'decimal': binary_to_decimal(binary)
    }))
else:                       # If no value was sent, respond with a null value
    print(json.dumps({
        'decimal': None
    }))
