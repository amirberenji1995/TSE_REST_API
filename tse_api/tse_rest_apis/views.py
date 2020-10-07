from tse_rest_apis.database.db_manipulation import list_of_symbols, symbols_table, df_filtering

from tse_rest_apis.models import Symbol
from tse_rest_apis.serializer import SymbolSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class SymbolsList(APIView):
    def get(self, request, format = None):
        symbols = list_of_symbols()
        i = 1
        result = {}
        for item in symbols:
            result[i] = item
            i += 1
        # serializer = SymbolSerializer(symbols, many = True)
        return Response(result, status = status.HTTP_200_OK)


class SymbolDetail(APIView):
    def get(self, request, pk,format = None):

        symbols = list_of_symbols()
        if pk in symbols:
            df = symbols_table(pk)

            if 'Starting'in request.headers.keys():
                starting_date = request.headers['Starting']
            else:
                starting_date = df['date'][0]

            if 'Ending'in request.headers.keys():
                ending_dates = request.headers['Ending']
            else:
                ending_dates = df['date'].iloc[-1]

            df = df_filtering(df, starting_date, ending_dates)
            result = df.to_json(orient='records')
            return Response(result, status = status.HTTP_200_OK)
        else:
            result = {'info':'No symbol find with this name.'}
            return Response(result, status = status.HTTP_404_NOT_FOUND)
