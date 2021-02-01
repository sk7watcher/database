from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DeleteView, DetailView, UpdateView, CreateView, ListView
from .models import UserProfile, Hospital
from .forms import UserRegisterForm


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserProfile

    def get_object(self, queryset=None):
        return UserProfile.objects.filter(user_prof=self.request.user).get()


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "user/registration.html"
    success_message = "patient created successfully"

    def form_valid(self, form):
        obj = form.save()
        UserProfile(user_prof=obj).save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('login')


class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = UserProfile
    success_message = "profile updated successfully"
    fields = ['name_prof', 'image_prof', 'hosp_prof']

    def get_object(self, queryset=None):
        return UserProfile.objects.filter(user_prof=self.request.user).get()

    def get_success_url(self):
        return reverse('profile-detail')

    def test_func(self):
        profile = self.get_object()
        if profile.user_prof == self.request.user:
            return True
        return False


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "user/user_confirm_delete.html"

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('base-home')


# ********* ImagesViews bellow *********
class HospitalDetailView(LoginRequiredMixin, DetailView):
    model   =   Hospital
    template_name = "hospital/hospital_detail.html"


class HospitalCreateView(SuccessMessageMixin, CreateView):
    model = Hospital
    # form_class = UserRegisterForm
    template_name = "hospital/hospital_form.html"
    success_message = "Hospital added successfully"
    fields = ['name_hosp', 'address_hosp']

    # def form_valid(self, form):
    #     obj = form.save()
    #     UserProfile(user_prof=obj).save()
    #     return super().form_valid(form)

    def get_success_url(self):
        return reverse('user-hospital-list')


class HospitalListView(LoginRequiredMixin, ListView):
    model = Hospital
    paginate_by = 8
    template_name = "hospital/hospital_list.html"



class HospitalDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Hospital
    template_name = "hospital/hospital_confirm_delete.html"


    def get_success_url(self):
        return reverse('user-hospital-list')

    def test_func(self):
        # patient = self.get_object()
        # if patient.doctor_pati == self.request.user:
            # return True
        # return False
        return True