from django.views.generic import DeleteView, ListView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin


class OwnerListView(ListView):
    """
    Sub-class of the ListView to pass the request to the form.
    """


class OwnerDetailView(DetailView):
    """
    Sub-class of the DetailView to pass the request to the form.
    """

class OwnerDeleteView(LoginRequiredMixin, DeleteView):
    """
    Sub-class of the DeleteView to restrict a User from deleting other
    user's data.
    """

    def get_queryset(self):
        qs = super(OwnerDeleteView, self).get_queryset()
        return qs.filter(owner=self.request.user)
