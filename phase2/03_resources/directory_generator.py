import os
import sys
import shutil
import random
from faker import Faker

fake = Faker('en_UK')
Faker.seed(42069)
contents = os.listdir()
directory_name = sys.argv[1]
first_name_list = []
Last_name_list = []

if directory_name not in contents:
    os.makedirs(directory_name)
    os.makedirs(f"{directory_name}/originals/")
    os.makedirs(f"{directory_name}/updates/")
else:
    shutil.rmtree(directory_name)
    os.makedirs(directory_name)
    os.makedirs(f"{directory_name}/originals/")
    os.makedirs(f"{directory_name}/updates/")

try:
    entries_number = sys.argv[2] #Get number of fake data needed
    if entries_number.strip().isdigit():
        entries_number = int(entries_number)
        for n in range(0, entries_number):
            first_name = fake.first_name()
            first_name_list.append(first_name)
            surname = fake.last_name()
            Last_name_list.append(surname)
            address = fake.address()
            with open(f'{directory_name}/originals/{surname}', 'w') as f:
                f.write(first_name + " " + surname + "\n" + address)
    else:
        raise OSError
except OSError:
    print("That is not an integer")

# Get files to update with updated information
try:
    update_number = sys.argv[3]
    if update_number.strip().isdigit():
        update_number = int(update_number)
        for j in range(0, update_number):
            new_address = fake.address()
            z = random.randint(0, len(Last_name_list) - 1)
            x = random.randint(0, 1)
            with open(f'{directory_name}/updates/{Last_name_list[z]}', 'w') as f:
                f.write(first_name_list[z] + " " 
                + Last_name_list[z] + "\n" + new_address)
            if x == 0:
                with open(f'{directory_name}/allowlist', 'w') as e:
                    e.write(Last_name_list[z] + "\n")
    else:
        raise OSError
except OSError:
    print("That is not an integer")
