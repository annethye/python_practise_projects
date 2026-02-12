'''
Hacking The Fender

The Fender, a notorious computer hacker and general villain of the people, has compromised several top-secret passwords
including your own. Your mission, should you choose to accept it, is threefold. You must acquire access to The Fender's
systems, you must update his 'passwords.csv' file to scramble the secret data. The last thing you need to do is add the
signature of Slash Null, a different hacker whose nefarious deeds could be very conveniently halted by The Fender if 
they viewed Slash Null as a threat.
'''

# Are you there? We've opened up a communications link to The Fender's secret computer. We need you to write a program 
# that will read in the compromised usernames and passwords that are stored in a file called "passwords.csv".

# Import the CSV module and the json module
import csv
import json

# Let's create a list of users whose passwords have been compromised
compromised_users = []

# Open the password file and and store it in a file object
with open('passwords.csv') as password_file:
  # pass the file object holder to the CSV reader for parsing
  password_csv = csv.DictReader(password_file)
  # Iterate through each line in the CSV and save each row as a temporary variable
  for password_row in password_csv:
    # Add each username to the list of compromised users
    compromised_users.append(password_row['Username'])

print(compromised_users)
# ['jean49', 'haydenashley', 'michaelastephens', 'denisephillips', 'andrew24', 'kaylaabbott', 'tmartinez', 
# 'mholden', 'randygilbert', 'watsonlouis', 'mdavis', 'patrickprice', 'kgriffith', 'hannasarah', 'xaviermartin',
#  'hrodriguez', 'erodriguez', 'danielleclark', 'timothy26', 'elizabeth19']


# Open the file compromised_users.txt in write mode and save as a file object
with open('compromised_users.txt', 'w') as compromised_user_file:
  # Iterate over each of the compromised users
  for compromised_user in compromised_users:
    # Write the username of each compromised user to the compromised user file
    compromised_user_file.write(compromised_user + '\n')
# We've now got the data we need to employ as insurance against The Fender.


# Your boss needs to know that you were successful in retrieving that compromised data. We'll need to send him 
# an encoded message over the internet. Let’s use JSON to do that.
# Open a new JSON file in write-mode and save the file object to a variable
with open('boss_message.json', 'w') as boss_message:
  # Create a Python dictionary object that relays a boss message
  boss_message_dict = {'recipient': 'Boss', 'message': 'Mission Success'}
  # Write out boss_message_dict to boss_message 
  json.dump(boss_message_dict, boss_message)


# Now that we've safely recovered the compromised users we'll want to overwrite the 'passwords.csv' file completely.
# Enemy of the people, Slash Null, is who we want The Fender to think was behind this attack. He has a signature, 
# whenever he hacks someone he adds this signature to one of the files he touches. Here is the signature:

slash_null_sig ='''
 _  _     ___   __  ____             
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
\_)__)\____/\____/\____/
'''

# Open 'passwords.csv' in write-mode and save the file object to a variable
with open('passwords.csv', 'w') as new_passwords_obj:
  # Write slash_null_sig to new_passwords_obj. Now we have the file to replace passwords.csv with!
  new_passwords_obj.write(slash_null_sig)


# What an incredible success! We'll take care of moving the new passwords file over the old one in case you want to 
# practice hacking The Fender in the future. Thank you for your service, programmer.

'''
Files used in project:

Compromised_users.txt:
jean49
haydenashley
michaelastephens
denisephillips
andrew24
kaylaabbott
tmartinez
mholden
randygilbert
watsonlouis
mdavis
patrickprice
kgriffith
hannasarah
xaviermartin
hrodriguez
erodriguez
danielleclark
timothy26
elizabeth19

passwords.csv:
Username,Password
jean49,Da*E%OuGuc9$V1m
haydenashley,l$r^9eGg8f@BZhy
michaelastephens,$1sp++bga8H+eCr
denisephillips,Vj)T7AsfRHkfpvw
andrew24,T^mH8LMM&0C3VVk
kaylaabbott,!nN05pv3tc(DBO(
tmartinez,V46_Xx85_gKg7rt
mholden,(sd44x3x*A7D1dA
randygilbert,A7+E0YfB+MLPJ8Z
watsonlouis,i!4(DEkBLNq)C7G
mdavis,c$2VXHnxQ+6ifpx
patrickprice,Es_r0GlF&zDkJKG
kgriffith,%0dUpqgwFfA$Dma
hannasarah,c(9au%x)tyC#HDd
xaviermartin,e7!gWemxlde3K6p
hrodriguez,od@9P!dfQj8NH&A
erodriguez,hB+4A(si*vdHl4c
danielleclark,2lv3HKAs+Or8R48
timothy26,oz7ExOUI2&*S87h
elizabeth19,x3C8yYtI!(e3+z(

Updated: passwords.csv:

 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( (___)  \___ \/ (_/\/    \___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/

'''