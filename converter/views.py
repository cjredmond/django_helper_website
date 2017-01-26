from django.shortcuts import render
from django.views.generic import TemplateView
from converter.helper import model_add

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        items = self.request.GET
        prop_1 = ""
        prop_1_type = ""
        prop_2 = ""
        prop_2_type = ""
        model_name = ""
        fields = []
        if self.request.GET:
            model_name = items['model_name']
            if items['prop_1']:
                prop_1 = items['prop_1']
                if items['prop_1_type']:
                    prop_1_type = items['prop_1_type']
                    fields.append([prop_1, prop_1_type])
            if items['prop_2']:
                prop_2 = items['prop_2']
                if items['prop_2_type']:
                    prop_2_type = items['prop_2_type']
                    fields.append([prop_2, prop_2_type])


        context['model'] = model_name
        context['prop_1'] = prop_1
        context['prop_1_type'] = prop_1_type
        context['prop_2'] = prop_2
        context['prop_2_type'] = prop_2_type
        context['model_info'] = model_add(model_name, fields)

        return context
