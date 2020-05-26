from django.shortcuts import render
from .models import Team, Secret
from django.views import generic


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


class TeamListView(generic.ListView):
    model = Team
    paginate_by = 10


class TeamDetailView(generic.DetailView):
    model = Team


class MySecretListView(generic.ListView):
    model = Secret
    context_object_name = 'my_secret_list'
    template_name = 'storage/my_secret_list.html'
    paginate_by = 10


class MySecretDetailView(generic.DetailView):
    model = Secret
    context_object_name = 'my_secret'
    template_name = 'storage/my_secret_detail.html'
