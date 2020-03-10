from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import csv
from django.http import HttpResponse
from .models import Fish

# Create your views here.
@login_required
def get_fish_template(request):
    fields = [item.name for item in Fish()._meta.get_fields()]

    ignore_export = ['_state', 'id', 'created', 'modified']
    header_list = ['species', 'category', 'strain_name', 'common_name', 'line_number', 'background', 
                   'genotype', 'phenotype', 'origin',
                   'availability', 'link', 'quarantine', 'mta', 'public', 'line_description', 'comments',
                   'maintainer', 'ownership']

    # add those fields that are not in either list to the end of the header_list
    for item in fields:
        if item not in ignore_export and item not in header_list:
            header_list.append(item)

    # prepare response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="fish_template.csv"'

    writer = csv.writer(response)
    writer.writerow(header_list)

    return response
