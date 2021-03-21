from contact_management.models import RecurringContact, ContactInteraction

class ContactMangementService():
    def create_contact(self, first_name, last_name, cadence = None):
        contact = RecurringContact(
            first_name = first_name, 
            last_name = last_name,
        )
        if cadence:
            contact.preferred_cadence = cadence
        contact.save()

    def get_contact_by_name(self, first_name, last_name):
        pass
    
    def get_contact_by_id(self, contact_id):
        pass

    def log_interaction(self, contact_id, direction):
        pass

    def get_all_contacts(self):
        pass

    def get_interactions_by_contact_id(self, contact_id):
        pass