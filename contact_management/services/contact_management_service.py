from contact_management.models import RecurringContact, ContactInteraction
from task_management.models import TaskPeriod

class ContactMangementService():
    def _get_cadence(self, cadence):
        return TaskPeriod.objects.get(period=cadence.lower())

    def create_contact(self, first_name, last_name, cadence = None):
        contact = RecurringContact(
            first_name = first_name,
            last_name = last_name,
        )
        if cadence:
            contact.preferred_cadence = self._get_cadence(cadence)
        contact.save()

    def get_contact_by_name(self, first_name, last_name):
        return RecurringContact.objects.get(
            first_name=first_name,
            last_name=last_name
        )
    
    def get_contact_by_id(self, contact_id):
        return RecurringContact.objects.get(id=contact_id)

    def log_interaction(self, contact_id, direction):
        '''
        Parameters:
            contact_id: id of contact for interaction
            direction(int) : 0 = you initiated, 1 = they initiated
        '''
        contact = self.get_contact_by_id(contact_id)
        ContactInteraction.objects.create(
            contact=contact,
            direction=direction
        )

    def get_all_contacts(self):
        return RecurringContact.objects.all()

    def get_interactions_by_contact_id(self, contact_id):
        '''
        Returns queryset of all interactions from given contact
        with most recent first.
        '''
        contact = self.get_contact_by_id(contact_id)
        return ContactInteraction.objects.filter(contact=contact).order_by('-created_at') 