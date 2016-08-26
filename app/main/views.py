from django.shortcuts import render
from django.contrib import messages

from django.views.generic import TemplateView, FormView

from .forms import ContactForm, CoverForm
from .models import Cover as CoverModel

from products.models import Product


class Test(TemplateView):
    template_name = 'main/test.html'

class Index(TemplateView):
    template_name = 'main/index.html'
    active = 'Home'

    def get_context_data(self, **kwargs):
        """ add extra context """
        context = super(Index, self).get_context_data(**kwargs)
        # context['header'] = self.header
        image = CoverModel.objects.latest('updated')
        products = Product.objects.order_by('-created')[:3]
        context['Home'] = self.active
        context['image'] = image
        context['products'] = products
        return context


class About(TemplateView):
    template_name = 'main/about.html'
    active = 'About'

    def get_context_data(self, **kwargs):
        """ add extra context """
        context = super(About, self).get_context_data(**kwargs)
        # context['header'] = self.header
        context['About'] = self.active
        return context

class Contact(FormView):
    template_name = 'main/contact.html'
    header = 'Contact us'
    active = 'Contact'
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        """ add extra context """
        context = super(Contact, self).get_context_data(**kwargs)
        context['header'] = self.header
        context['Contact'] = self.active
        return context

class Cover(FormView):
    template_name = 'main/form.html'
    form_class = CoverForm
    header = 'Cover Photo'
    success_url = '/'

    def form_valid(self, form):
        form.save(commit=True)
        messages.success(self.request, 'Image upload')
        return super(Cover, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(Cover, self).get_context_data(**kwargs)
        context['header'] = self.header
        return context
