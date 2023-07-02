import csv
import json
import os


compromised_users = []
print("test")
data_file_path = os.path.join(os.path.dirname(__file__), "passwords.csv")
# Open the 'passwords.csv' file for reading
# with open('passwords.csv') as password_file:
with open(data_file_path) as password_file:
    print("password_file", password_file )
    password_csv = csv.DictReader(password_file)
    print("password_csv", password_csv )


    # Iterate over each row in the CSV file
    for item in password_csv:
        print("password_csv item", item )

        password_row = item
        # Append the 'Username' field of the current row to the compromised_users list
        compromised_users.append(password_row['Username'])

# Open the 'compromised_users.txt' file for writing
with open('compromised_users.txt', 'w') as compromised_user_file:
    # Write each item from the compromised_users list to the file
    for item in compromised_users:
        compromised_user_file.write(item)

# Open the 'boss_message.json' file for writing
with open('boss_message.json', 'w') as boss_message:
    # Create a dictionary containing recipient and message information
    boss_message_dict = {'recipient': 'The Boss', 'message': 'Mission Success'}
    # Write the dictionary to the boss_message.json file in JSON format
    json.dump(boss_message_dict, boss_message)

    # Open the 'new_passwords.csv' file for writing
    with open('new_passwords.csv', 'w') as new_passwords_obj:
        slash_null_sig = ''' _  _     ___   __  ____             
                            / )( \   / __) /  \(_  _)            
                            ) \/ (  ( (_ \(  O ) )(              
                            \____/   \___/ \__/ (__)             
                             _  _   __    ___  __ _  ____  ____  
                             / )( \ / _\  / __)(  / )(  __)(    \ 
                             ) __ (/    \( (__  )  (  ) _)  ) D ( 
                             \_)(_/\_/\_/ \___)(__\_)(____)(____/ 
                               ____  __     __   ____  _  _ 
                               ___   / ___)(  )   / _\ / ___)/ )( \
                              (___)  \___ \/ (_/\/    \\___ \) __ (
                                     (____/\____/\_/\_/(____/\_)(_/
                              __ _  _  _  __    __                
                             (  ( \/ )( \(  )  (  )               
                             /    /) \/ (/ (_/\/ (_/\             
                             \_)__)\____/\____/\____/ '''
        # Write the slash_null_sig variable to the new_passwords.csv file
        new_passwords_obj.write(slash_null_sig)
