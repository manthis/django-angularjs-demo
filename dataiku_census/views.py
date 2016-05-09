from django.http import JsonResponse
from django.shortcuts import render

from dataiku_census.models import CensusLearnSql
from dataiku_census.services import Services


def index(request):
    return render(request, 'index.html')


def columns(request):
    # We retrieve the columns names from the model
    listing = Services.get_model_fields_names()

    # We build a dictionary with the values
    columns_list = {'column_list': listing}

    # We return the list of columns as JsonResponse
    return JsonResponse(columns_list)


def stats(request):
    # We get the column name to get stats for
    column_name = request.GET.get('q', '')

    # We ensure the column's name do really exist
    listing = Services.get_model_fields_names()
    if column_name.replace("\"", "") not in listing:
        return JsonResponse([], safe=False)

    # We build the SQL request to be performed
    sql_request = "SELECT census_learn_sql.id, {} as 'column', " \
                  "COUNT(*) as 'count', " \
                  "AVG(census_learn_sql.age) as 'average' " \
                  "FROM census_learn_sql GROUP BY {};" \
                  .format(column_name, column_name)

    # We perform the SQL request
    results = CensusLearnSql.objects.raw(sql_request)

    values = []
    for result in results:
        values.append({'value': result.column, 'count': result.count, 'average': result.average})

    return JsonResponse(values, safe=False)
