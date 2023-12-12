from faker import Faker
import faker_commerce

faker_gen = Faker()
faker_gen.add_provider(faker_commerce.Provider)

for i in range(10):
    print(faker_gen.name(), faker_gen.date(), faker_gen.email(), faker_gen.ecommerce_name())




#faker_gen.name(), faker_gen.providers.date_time, faker_gen.email())