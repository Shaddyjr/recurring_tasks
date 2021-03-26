from django.forms.models import model_to_dict
from contact_management.services.contact_management_service import ContactMangementService


class ContactManagementAPI():
    def _format_model_list(self, model_list: dict) -> list:
        return [model_to_dict(mdoel) for mdoel in model_list]

    def get_all_contacts(self) -> list:
        contacts = ContactMangementService().get_all_contacts()
        return self._format_model_list(contacts)
    
    def get_contact_by_id(self, contact_id: int) -> dict:
        contact = ContactMangementService().get_contact_by_id(contact_id)
        return model_to_dict(contact)

    def create_contact(self, first_name: str, last_name: str, cadence: str = None) -> None:
        ContactMangementService().create_contact(first_name, last_name, cadence)

    def log_interaction(self, contact_id: int, direction: int) -> None:
        ContactMangementService().log_interaction(contact_id, direction)

    def get_interactions_by_contact_id(self, contact_id: int) -> list:
        interactions = ContactMangementService().get_interactions_by_contact_id(contact_id)
        return self._format_model_list(interactions)
    
    def get_last_interactions_by_contact(self) -> list:
        interactions = ContactMangementService().get_last_interactions_by_contact()
        return self._format_model_list(interactions)
    