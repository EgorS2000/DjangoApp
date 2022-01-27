import json
from faker import Faker
import pytest
from rest_framework.test import APIClient

from App.models import Employee, PersonalData, Company, Bank

fake = Faker()


@pytest.mark.django_db
def test_employee_salary_increasing(api_client=APIClient()):
    bank1 = Bank.objects.create(
        name=fake.pystr(),
        web_site=fake.pystr(),
        email=fake.pystr()
    )

    bank2 = Bank.objects.create(
        name=fake.pystr(),
        web_site=fake.pystr(),
        email=fake.pystr()
    )

    company = Company.objects.create(
        name=fake.pystr(),
        web_site=fake.pystr(),
        email=fake.pystr(),
        post_index=fake.pyint(),
        logo='test/test.png',
    )
    company.bank.add(bank1, bank2)

    employee = Employee.objects.create(
        name=fake.pystr(),
        surname=fake.pystr(),
        job_position=fake.pystr(),
        is_manager=fake.pybool(),
        is_admin=fake.pybool(),
        phone_number=fake.pyint(),
        company=company
    )

    PersonalData.objects.create(
        date_of_birth='2021-01-25',
        home_address=fake.pystr(),
        salary=fake.pyint(),
        employee=employee
    )

    response = api_client.put(path='/DjangoApp/employees/', data={
        "birthday": "2021-01-25",
        "increase_number": fake.pyint()
    })
    assert response.status_code == 200


@pytest.mark.django_db
def test_companies_filter(api_client=APIClient()):
    bank1 = Bank.objects.create(
        name=fake.pystr(),
        web_site=fake.pystr(),
        email=fake.pystr()
    )

    bank2 = Bank.objects.create(
        name=fake.pystr(),
        web_site=fake.pystr(),
        email=fake.pystr()
    )

    company1 = Company.objects.create(
        name='test1',
        web_site='test1',
        email='test@gmail.com',
        post_index=12345,
        logo='test/test.png',
    )
    company1.bank.add(bank1, bank2)

    company2 = Company.objects.create(
        name='test2',
        web_site='test2',
        email='test@gmail.com',
        post_index=12345,
        logo='test/test.png',
    )
    company2.bank.add(bank1, bank2)

    response = api_client.get(
        path='/DjangoApp/companies/',
        data={
            "date1": "2022-01-22 06:00:00.000000-08:00",
            "date2": "2022-01-31 06:00:00.000000-08:00"
        }
    )

    assert response.status_code == 200
    assert json.loads(response.content) == {"name": "test2",
                                            "web_site": "test2",
                                            "email": "test@gmail.com",
                                            "post_index": 12345,
                                            "logo": "test/test.png"}
