from django.db import models


class AdoptionCandidateManager(models.Manager):
    def available(self):
        value, human = self.model.ADOPTION_STATES[0]
        return self.get_query_set().filter(
            status=value
        )
