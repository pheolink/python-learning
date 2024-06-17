import os
from cryptography.fernet import Fernet

# Specify the file name you want to check
key_file_name = "key.key"
ouput_file_name = "passwords.txt"

# Get the current directory path
current_directory = os.getcwd()

# Empty key
fer = None
   
# Creating the key file to encyption
def write_key():
  key = Fernet.generate_key()
  with open(key_file_name, "wb") as key_file:
      key_file.write(key)
  print("New key file created")

# Loading the key file to decyption
def load_key():
  with open(key_file_name, "rb") as key_file:
      loaded_key = key_file.read()
  print("configuring the key")
  return loaded_key

# To view the records
def view():
  output_file_path = os.path.join(current_directory, ouput_file_name)
  if os.path.isfile(output_file_path):
    with open(ouput_file_name, 'r') as f:
      lines_in_file = f.readlines()
      
      # Check if there is at least one non-empty line
      if len(lines_in_file) > 0:
        for line in lines_in_file:
          data = line.rstrip()
          user, passw = data.split("|")
          print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())
      else:
          print('No entries')
  else:
     print("Add atleast one entry")

# To add atleast one entry
def add():
  name = input('Account Name: ')
  pwd = input("Password: ")
  with open(ouput_file_name, 'a') as f:
     f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
  print("Details added")


# Combine the current directory path with the file name
file_path = os.path.join(current_directory, key_file_name)

# Check if the file exists
if os.path.isfile(file_path):
   key = load_key()
   fer = Fernet(key)
else:
    write_key()


while True:
  if fer is not None:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
  
    if mode == 'q':
      break

    if mode in ["view", "v"]:
      view()
    elif mode in ["add", "a"]:
      add()
    else:
      continue

