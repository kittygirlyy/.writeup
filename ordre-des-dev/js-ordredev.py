import base64

encoded_password = 'MGZmZDM1YjM4NGFjMDg5YzM0YmNmMTZmOTg3YTE0MTM='
expected_base64 = 'A1UFBVUEW1FdVlM8AFBXUxJBBFMTXw8LCmdWVVQEAAUwMTBhYmE='

decoded_password = base64.b64decode(encoded_password).decode()
expected_result = base64.b64decode(expected_base64)

correct_password = ''

for i in range(max(len(decoded_password), len(expected_result))):
    decoded_char = ord(decoded_password[i]) if i < len(decoded_password) else 0
    expected_char = expected_result[i] if i < len(expected_result) else 0
    
    correct_password += chr(decoded_char ^ expected_char)

print(correct_password)
