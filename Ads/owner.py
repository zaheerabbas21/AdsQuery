from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin


class OwnerListView(ListView):
    """
    Sub-class of the ListView to pass the request to the form.
    """


class OwnerDetailView(DetailView):
    """
    Sub-class of the DetailView to pass the request to the form.
    """


class OwnerCreateView(LoginRequiredMixin, CreateView):
    """
    * Sub-class of the CreateView to automatically pass the Request to the Form
    and add the owner to the saved object.
    * Saves the form instance, sets the current object for the view, and redirects to get_success_url().
    * commit = false means Copy the form data into the object withoud commiting it to the datatbase, the object can be any name here
    * overrides the form_valid of model mixins to set the current user as owner refer -> https://docs.djangoproject.com/en/3.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.ModelFormMixin.form_valid
    and this -> https://stackoverflow.com/questions/862522/django-populate-user-id-when-saving-a-model/15540149#15540149
    """

    def form_valid(self, form):
        object = form.save(commit=False)
        object.owner = self.request.user
        object.save()
        return super(OwnerCreateView, self).form_valid(form)


class OwnerUpdateView(LoginRequiredMixin, UpdateView):
    """
    * Sub-class of the UpdateView to pass the request to the form and limit the
    queryset to the requesting user.
    * Limit a User to only modifying their own data.
    """

    def get_queryset(self):
        qs = super(OwnerUpdateView, self).get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerDeleteView(LoginRequiredMixin, DeleteView):
    """
    Sub-class of the DeleteView to restrict a User from deleting other
    user's data.
    """

    def get_queryset(self):
        qs = super(OwnerDeleteView, self).get_queryset()
        return qs.filter(owner=self.request.user)

