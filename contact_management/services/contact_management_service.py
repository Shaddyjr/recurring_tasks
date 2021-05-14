from django.db.models import Max
from django.utils import timezone
from contact_management.models import RecurringContact, ContactInteraction
from cadence.models import Cadence

class ContactMangementService():
    def _get_cadence(self, cadence: str) -> Cadence:
        return Cadence.objects.get(period=cadence.lower())

    def create_contact(
        self,
        first_name: str,
        last_name: str,
        preferred_cadence: str = None
    ) -> None:
        '''
        Create's a contact with the given information.
        Also creates an initial ContactInteraction associated with the new contact.
        '''
        contact = RecurringContact(
            first_name = first_name,
            last_name = last_name,
        )
        if preferred_cadence:
            contact.preferred_cadence = self._get_cadence(preferred_cadence)
        contact.save()
        self.log_interaction(contact.id)

    def get_contact_by_id(self, contact_id: int) -> RecurringContact:
        return RecurringContact.objects.get(id=contact_id)

    def log_interaction(self, contact_id: int) -> None:
        '''
        Parameters:
            contact_id: id of contact for interaction
        '''
        contact = self.get_contact_by_id(contact_id)
        interactions = self.get_interactions_by_contact_id(contact_id)
        if not interactions:
            new_direction = 1 # default direction if first time contact gets logged
        else:
            new_direction = interactions[0].direction ^ 1 # flip bit
        
        ContactInteraction.objects.create(
            contact=contact,
            direction=new_direction
        )

    def get_all_contacts(self):
        return RecurringContact.objects.all()

    def get_interactions_by_contact_id(self, contact_id: int):
        '''
        Returns queryset of all interactions from given contact
        with most recent first.
        '''
        contact = self.get_contact_by_id(contact_id)
        return ContactInteraction.objects.filter(contact=contact).order_by('-created_at')
    
    def _expand_interaction(self, interation_obj):
        interaction = ContactInteraction.objects.get(id=interation_obj['interaction_id'])
        return {
            'contact': RecurringContact.objects.get(id=interation_obj['contact']),
            'interaction': interaction,
            'time_since_last_interaction': timezone.now() - interaction.created_at, # datetime.timedelta
        }

    def get_last_interactions_by_contact(self):
        '''
        Example return value:
            interactions = <QuerySet [{'contact': 1, 'interaction_id': 6}, {'contact': 2, 'interaction_id': 7}]>
            return value = [{'contact':Contact, 'interaction':Interaction},...]
        '''
        interactions = ContactInteraction.objects.values('contact').annotate(interaction_id=Max('id'))
        # for each interaction, pull out the contact and interaction obj
        return [self._expand_interaction(interation_obj) for interation_obj in interactions]