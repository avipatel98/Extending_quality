from faker import Faker
fake = Faker('en_UK')
seed_count = 0
first_name = ""
for n in range (0, 3):
    while first_name != "Dr Mathew Ellis":
        Faker.seed(seed_count)
        first_name = fake.name()
        seed_count += 1
    print(seed_count - 1)