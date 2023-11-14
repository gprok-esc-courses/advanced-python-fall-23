from faker import Faker

faker_gen = Faker()

for i in range(10):
    print(faker_gen.name(), faker_gen.date(), faker_gen.email())


#faker_gen.name(), faker_gen.providers.date_time, faker_gen.email())