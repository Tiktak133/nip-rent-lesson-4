from src.models import Apartment
from src.manager import Manager
from src.models import Parameters


def test_load_data():
    parameters = Parameters()
    manager = Manager(parameters)
    assert isinstance(manager.apartments, dict)
    assert isinstance(manager.tenants, dict)
    assert isinstance(manager.transfers, list)
    assert isinstance(manager.bills, list)

    for apartment_key, apartment in manager.apartments.items():
        assert isinstance(apartment, Apartment)
        assert apartment.key == apartment_key

def test_all_tenants_have_valid_apartments_and_rooms():
    parameters = Parameters()
    manager = Manager(parameters)

    for tenant_key, tenant in manager.tenants.items():
        assert tenant.apartment in manager.apartments, f"Tenant {tenant_key} references non-existent apartment {tenant.apartment}"
        apartment = manager.apartments[tenant.apartment]
        assert tenant.room in apartment.rooms, f"Tenant {tenant_key} references non-existent room {tenant.room} in apartment {tenant.apartment}"