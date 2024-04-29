from django.contrib.auth.views import login_required
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Car


class Home(ListView):
    model = Car
    paginate_by = 10
    template_name = "home.html"


# mixins are read from left to right
class CreateCar(LoginRequiredMixin, CreateView):
    model = Car
    fields = [
        "car_model",
        "car_company",
        "year",
        "made_in",
        "milage",
        "transmission_type",
        "drivetrain",
        "color",
        "available_for_auction",
        "images",
    ]
    template_name = "create.html"
    success_url = reverse_lazy("home_page")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


@login_required
def profile(request):
    # the instance of appuser model / auth user model / setting
    user = request.user
    cars = Car.objects.filter(owner=user)
    return render(request, "profile.html", {"cars": cars, "user": user})


class UpdateCar(LoginRequiredMixin,UpdateView):
    model = Car
    fields = [
        "car_model",
        "car_company",
        "year",
        "made_in",
        "milage",
        "transmission_type",
        "drivetrain",
        "color",
        "available_for_auction",
        "images",
    ]
    template_name = "update.html"
    success_url = reverse_lazy("profile")


class DeleteCar(LoginRequiredMixin,DeleteView):
    model = Car
    template_name = 'delete.html'
    success_url = reverse_lazy("profile")


class Auction(LoginRequiredMixin, DetailView):
    model = Car
    template_name = "auction.html"
