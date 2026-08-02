# 2024-10-15 Sekiro (Miscellaneous)

*[image unavailable]*

Connect to the instance and fight the Samurai

*[image unavailable]*

Get timed out, and the commands seem to kill the instance too, so lets script this, I'm not fast enough to keep up with the correct commands to kep it alive.

```powershell
#import the things
import random
import time
import socket

# Function to send a move based on the opponent's action
def send_move(connection, opponent_move):
    if opponent_move == "advance":
        move = "retreat"
    elif opponent_move == "retreat":
        move = "strike"
    elif opponent_move == "block":
        move = "retreat" 
    elif opponent_move == "strike":
        move = "block" 
    else:
        move = "strike"  # Default to strike if no clear pattern
    
    print(f"Sending move: {move}")
    connection.sendall(f"{move}\n".encode('utf-8'))
    time.sleep(0.5)  
    # Small delay to make sure the command is processed

def connect_to_game():
    try:
        host = "challenge.ctf.games"
        port = 30855
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            
            while True:
                response = s.recv(4096).decode('utf-8')
                print(response)

                if "Opponent move: " in response:
                    if "advance" in response:
                        send_move(s, "advance")
                    elif "retreat" in response:
                        send_move(s, "retreat")
                    elif "block" in response:
                        send_move(s, "block")
                    elif "strike" in response:
                        send_move(s, "strike")
                
                if "disconnected" in response:
                    print("Disconnected from server. Reconnecting...")
                    break

                # Sleep between moves
                time.sleep(1)
    
    except Exception as e:
        print(f"Error occurred: {e}")

while True:
    connect_to_game()
```

*[image unavailable]*

*[image unavailable]*

```text
flag{a1ae4e5604576818132ce3bfebe95de5}
```

*[image unavailable]*

```python
flag{a1ae4e5604576818132ce3bfebe95de5}
```

*[image unavailable]*
