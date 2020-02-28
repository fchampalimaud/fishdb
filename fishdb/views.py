from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from fishdb.admin import FishResource
import csv
from django.http import HttpResponse

# Create your views here.
@login_required
def get_fish_template(request):
    fish_resource = FishResource()
    dataset = fish_resource.export()
    
    # prepare response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="fish_template.csv"'

    if dataset.csv:
        header = dataset.csv.splitlines()
        if len(header) > 0:
            csv_list = header[0].split(',')
            writer = csv.writer(response)
            writer.writerow(csv_list)

    return response