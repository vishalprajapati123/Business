import pytest
from django.core.exceptions import ValidationError
from B_app.models import Business

@pytest.mark.django_db
def test_create_business():
    Business.objects.create(name="Test", address="Test Address", owner_info="Test Owner", employee_size=10, investor_type="Investor", contact_mail="test@test.com", phone_number=1234567890, investment_stage="Seed", company_type="Private")
    assert Business.objects.count() == 1

@pytest.mark.django_db
def test_create_business_fail():
    with pytest.raises(ValidationError):
        business = Business(name="", address="Test Address", owner_info="Test Owner", employee_size=10, investor_type="Investor", contact_mail="test@test.com", phone_number=1234567890, investment_stage="Seed", company_type="Private")
        business.full_clean()
        business.save()


@pytest.mark.django_db
def test_update_business():
    business = Business.objects.create(name="Test", address="Test Address", owner_info="Test Owner", employee_size=10, investor_type="Investor", contact_mail="test@test.com", phone_number=1234567890, investment_stage="Seed", company_type="Private")
    business.name = "Updated"
    business.save()
    assert Business.objects.get(id=business.id).name == "Updated"

@pytest.mark.django_db
def test_update_business_fail():
    with pytest.raises(Business.DoesNotExist):
        business = Business.objects.get(id=999)
        business.name = "Updated"
        business.save()

@pytest.mark.django_db
def test_delete_business():
    business = Business.objects.create(name="Test", address="Test Address", owner_info="Test Owner", employee_size=10, investor_type="Investor", contact_mail="test@test.com", phone_number=1234567890, investment_stage="Seed", company_type="Private")
    business.delete()
    assert Business.objects.count() == 0

@pytest.mark.django_db
def test_delete_business_fail():
    with pytest.raises(Business.DoesNotExist):
        business = Business.objects.get(id=999)
        business.delete()

@pytest.mark.django_db
def test_search_business():
    Business.objects.create(name="Test", address="Test Address", owner_info="Test Owner", employee_size=10, investor_type="Investor", contact_mail="test@test.com", phone_number=1234567890, investment_stage="Seed", company_type="Private")
    businesses = Business.objects.filter(name__icontains="Test")
    assert businesses.count() == 1
