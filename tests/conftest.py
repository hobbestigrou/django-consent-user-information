import pytest
from faker import Faker


@pytest.fixture(scope='module')
def password():
    """To generate a password"""
    fake = Faker()
    return fake.password()


@pytest.fixture
def user(django_user_model, password):
    """To create an user"""
    fake = Faker()
    username = fake.user_name()
    mail = fake.email()
    user = django_user_model.objects.create(username=username, email=mail)

    user.set_password(password)
    user.save()

    return user
