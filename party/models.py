import uuid

from django.contrib.auth.models import User
from django.db import models


class Party(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    @property
    def name(self):
        if self.title:
            return self.title
        return '{user}\'s Party'.format(user=self.user)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Parties'
        ordering = ('id',)


class PartyUser(models.Model):
    party = models.ForeignKey(Party, related_name='party_user', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='party_user', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{user} is a member of {party}'.format(user=self.user, party=self.party)

    class Meta:
        verbose_name_plural = 'Party users'
        ordering = ('id',)
        unique_together = (('party', 'user'),)


class PartyCategory(models.Model):
    party = models.ForeignKey(Party, related_name='party_category', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{name} of {party}'.format(name=self.name, party=self.party)

    class Meta:
        verbose_name_plural = 'Party categories'
        ordering = ('id',)
        unique_together = (('party', 'name'),)