from factory.django import DjangoModelFactory, mute_signals
from django.db.models import signals
from factory import Faker, PostGenerationMethodCall, RelatedFactory, SubFactory, post_generation
from django.contrib.auth.models import User

from .models import Customer


class CustomerFactory(DjangoModelFactory):
    class Meta:
        model = Customer

    user = SubFactory('customer.factories.UserFactory', customer=None)


@mute_signals(signals.pre_save, signals.post_save)
class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = Faker('user_name')
    email = Faker('email')
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    password = PostGenerationMethodCall('set_password', 'password')
    customer = RelatedFactory(CustomerFactory, factory_related_name='user')
