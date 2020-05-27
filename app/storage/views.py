from django.shortcuts import render
from .models import Team, Secret
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TeamSerializer


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


class TeamView(APIView):
    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response({'teams': serializer.data})


class TeamDetailView(generic.DetailView):
    model = Team


class MySecretListView(LoginRequiredMixin, generic.ListView):
    model = Secret
    context_object_name = 'my_secret_list'
    template_name = 'storage/my_secret_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Secret.objects.filter(owner=self.request.user).order_by('name')


class MySecretDetailView(LoginRequiredMixin, generic.DetailView):
    model = Secret
    context_object_name = 'my_secret'
    template_name = 'storage/my_secret_detail.html'
