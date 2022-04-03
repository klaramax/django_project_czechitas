from django.views.generic import CreateView, ListView, TemplateView
import crm.models as models
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = "index.html"


class CompanyCreateView(CreateView):
    model = models.Company
    template_name = "company/create_company.html"
    fields = ["name", "status", "phone_number", "email", "identification_number"]
    success_url = reverse_lazy("index")


class CompaniesListView(ListView):
    template_name = 'company/companies_list.html'
    model = models.Company

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['companies'] = self.get_queryset().order_by('name')
        return context


class OpportunityCreateView(CreateView):
    model = models.Opportunity
    template_name = "opportunity/create_opportunity.html"
    fields = ["company", "sales_manager", "primary_contact", "description", "status", "value"]
    success_url = reverse_lazy("index")
