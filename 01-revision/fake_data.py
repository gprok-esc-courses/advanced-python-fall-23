from faker import Faker

faker = Faker()

for i in range(10):
    print(faker.user_name())
    fdate = faker.date_this_year()
    print(fdate)
    fdate_str = fdate.strftime("%Y-%m-%d")
    print(fdate_str)
    print(faker.address())