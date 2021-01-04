from django.shortcuts import render, redirect, resolve_url, get_object_or_404
from .models import User, List, Card
from django.views.generic import CreateView, TemplateView, DetailView, UpdateView, ListView, DeleteView
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from .forms import UserForm, SignUpForm, LoginForm, ListForm, CardForm, CardCreateFromHomeForm
from .mixins import OnlyYouMixin




class IndexView(ListView):
    model = List
    template_name = 'index.html'



class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'signup.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('trello:index')
        return render(request, 'signup.html', {'form': form})

class Login(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

class Logout(LogoutView):
    template_name = 'logout.html'


class UserDetailView(OnlyYouMixin, DetailView):
    model = User
    template_name = 'user_detail.html'

class UserUpdateView(OnlyYouMixin, UpdateView):
    model = User
    template_name = 'user_update.html'
    form_class = UserForm

    def get_success_url(self):
        return resolve_url('trello:user_detail', pk=self.kwargs['pk'])


class ListCreateView(CreateView):
    model = List
    template_name = 'create.html'
    form_class = ListForm
    success_url = reverse_lazy('trello:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ListListView(ListView):
    model = List
    template_name = 'list.html'

class ListDetailView(DetailView):
    model = List
    template_name = 'list_detail.html'

class ListUpdateView(UpdateView):
    model = List
    template_name = 'list_update.html'
    form_class = ListForm
    success_url = reverse_lazy('trello:index')


class ListDeleteView(DeleteView):
    model = List
    template_name = 'delete.html'
    form_class = ListForm
    success_url = reverse_lazy('trello:index')

class CardCreateView(CreateView):
    model = Card
    template_name = 'cards/create.html'
    form_class = CardForm
    success_url = reverse_lazy('trello:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CardListView(ListView):
    model = Card
    template_name = 'cards/list.html'

class CardDetailView(DetailView):
    model = Card
    template_name = 'cards/detail.html'


class CardUpdateView(UpdateView):
    model = Card
    template_name = 'cards/update.html'
    form_class = CardForm
    success_url = reverse_lazy('trello:index')

class CardDeleteView(DeleteView):
    model = Card
    template_name = 'cards/delete.html'
    form_class = CardForm
    success_url = reverse_lazy('trello:index')

class CardCreateFromHomeView(CreateView):
    model = Card
    template_name = 'create.html'
    form_class = CardCreateFromHomeForm
    success_url = reverse_lazy('trello:index')

    def form_valid(self, form):
        list_pk = self.kwargs['list_pk']
        list_instance = get_object_or_404(List, pk=list_pk)
        form.instance.list = list_instance
        form.instance.user = self.request.user
        return super().form_valid(form)