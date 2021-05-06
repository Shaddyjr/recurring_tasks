from django.forms.models import model_to_dict
from contact_management.services.contact_management_service import ContactMangementService


class ContactManagementAPI():
    def _format_model_list(self, model_list: dict) -> list:
        return [model_to_dict(model) for model in model_list]

    def get_all_contacts(self) -> list:
        contacts = ContactMangementService().get_all_contacts()
        return self._format_model_list(contacts)
    
    def get_contact_by_id(self, contact_id: int) -> dict:
        contact = ContactMangementService().get_contact_by_id(contact_id)
        return model_to_dict(contact)

    def create_contact(self, first_name: str, last_name: str, preferred_cadence: str = None) -> None:
        ContactMangementService().create_contact(first_name, last_name, preferred_cadence)

    def log_interaction(self, contact_id: int) -> None:
        ContactMangementService().log_interaction(contact_id)

    def get_interactions_by_contact_id(self, contact_id: int) -> list:
        interactions = ContactMangementService().get_interactions_by_contact_id(contact_id)
        return self._format_model_list(interactions)

    def get_last_interactions_by_contact(self) -> list:
        '''
        Returns:
            [{
                'contact': {
                    'id': 1,
                    'first_name': 'bob',
                    'last_name': 'bobby',
                    'preferred_cadence': None
                },
                'interaction': {
                    'id': 6,
                    'contact': 1,
                    'direction': False,
                    'prev_interaction': 5
                },
                'time_since_last_interaction': datetime.timedelta(seconds=6, microseconds=411700),
            },...
            ]
        '''
        contact_interactions = ContactMangementService().get_last_interactions_by_contact()
        output = []
        for contact_interaction in contact_interactions:
            contact=contact_interaction.get("contact")
            interaction=contact_interaction.get("interaction")
            time_since_last_interaction = contact_interaction.get('time_since_last_interaction')
            obj = {
                'contact': model_to_dict(contact),
                'interaction': model_to_dict(interaction),
                'time_since_last_interaction': time_since_last_interaction,
            }
            output.append(obj)
        return output

    