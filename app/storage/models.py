from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import uuid


class Team(models.Model):
    """Model representing a team."""
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, blank=True)
    secrets = models.ManyToManyField('Secret', blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular team instance."""
        return reverse('team-detail', args=[str(self.id)])


class Secret(models.Model):
    """Model representing a secret."""
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID for this particular secret across whole storage",
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    content = models.TextField(max_length=1000)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular secret instance."""
        return reverse('my-secret-detail', args=[str(self.id)])
