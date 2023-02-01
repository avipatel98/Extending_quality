import random

first_letter = ['A', 'B', 'C', 'E', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'W', 'X', 'Y', 'Z']
second_lettor = ['A', 'B', 'C', 'E', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'W', 'X', 'Y', 'Z']
special_letter_combos = ['BG', 'GB', 'NK', 'KN', 'TN', 'NT', 'ZZ']
last_letter = ['A', 'B', 'C', 'D']
generated_nns = []
def generate_nn():
    with open('valid_nn.txt', 'w') as f:
        for n in range(1, 1001):
            front_letter_combo = random.choice(first_letter) + random.choice(second_lettor)
            if front_letter_combo not in special_letter_combos:
                unique_nn = front_letter_combo + " " + str(random.randint(0,9)) + str(random.randint(0,9)) + " " + str(random.randint(0,9)) + str(random.randint(0,9)) + " " + str(random.randint(0,9)) + str(random.randint(0,9))
                if unique_nn not in generated_nns:
                    generated_nns.append(unique_nn)
                    f.write(str(n) + ": " + unique_nn  + " " + random.choice(last_letter) + "\n")

generate_nn()
