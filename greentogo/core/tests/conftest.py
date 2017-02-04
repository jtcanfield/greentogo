import pytest
from core.models import Location, SubscriptionPlan, Subscription, Customer
from faker import Faker
from datetime import datetime


@pytest.fixture(scope="session")
def faker():
    return Faker()


@pytest.fixture
def checkin_location(db):
    loc = Location(service=Location.CHECKIN)
    loc.save()
    return loc


@pytest.fixture
def checkout_location(db):
    loc = Location(service=Location.CHECKOUT)
    loc.save()
    return loc


@pytest.fixture
def subscription_plan1(db):
    plan, _ = SubscriptionPlan.objects.get_or_create(
        code="1BOX", defaults={"description": "1 Box",
                               "number_of_boxes": 1})
    return plan


@pytest.fixture
def subscription_plan2(db):
    plan, _ = SubscriptionPlan.objects.get_or_create(
        code="2BOX", defaults={"description": "2 Boxes",
                               "number_of_boxes": 2})
    return plan


@pytest.fixture
def subscription_plan_unlimited(db):
    plan, _ = SubscriptionPlan.objects.get_or_create(
        code="UNLIMIT", defaults={"description": "Unlimited"})
    return plan


@pytest.fixture
def customer(db, faker):
    customer = Customer(name=faker.name())
    customer.password = faker.password(length=10)
    customer.save()
    customer.emailaddress_set.create(address=faker.email())
    return customer


@pytest.fixture
def subscription1(db, customer, subscription_plan1):
    subscription = Subscription(
        plan=subscription_plan1, admin=customer, started_on=datetime.now())
    subscription.save()
    subscription.customer_set.add(customer)
    return subscription


@pytest.fixture
def subscription2(db, customer, subscription_plan2):
    subscription = Subscription(
        plan=subscription_plan2, admin=customer, started_on=datetime.now())
    subscription.save()
    subscription.customer_set.add(customer)
    return subscription
