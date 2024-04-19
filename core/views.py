from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Car


class Home(ListView):
    model = Car
    paginate_by = 10
    template_name = "home.html"


class CreateCar(CreateView, LoginRequiredMixin):
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


class Auction(DetailView):
    model = Car
    template_name = "auction.html"
