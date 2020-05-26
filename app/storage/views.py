from django.shortcuts import render
from .models import Team, Secret


def index(request):
    """View function for home page of site."""
    num_teams = Team.objects.all().count()
    num_secrets = Secret.objects.all().count()

    return render(
        request,
        'index.html',
        context={
            'num_teams': num_teams,
            'num_secrets': num_secrets,
        },
    )
