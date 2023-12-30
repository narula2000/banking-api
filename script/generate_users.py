from django.contrib.auth.models import User
from customer.models import Customer
from faker import Faker

number_of_users = 15
fake = Faker()

for i in range(number_of_users):
    user = User.objects.create_user(
        username=fake.user_name(),
        email=fake.email(),
        password='password',
        first_name=fake.first_name(),
        last_name=fake.last_name(),
    )
    user.save()
    customer = Customer.objects.create(user=user)
    customer.save()
