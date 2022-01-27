from datetime import date, datetime

from django.core.files.storage import default_storage
from django.db.models import F
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import (
    ListAPIView
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from api.serializers import CompanySerializer
from api.utils import is_user_auth, APIPermission, serialization
from App.models import Company, PersonalData


class PersonalDataView(APIView):
    permissions = [IsAuthenticated, APIPermission]

    def put(self, request):
        increase_number, birthday = request.data['increase_number'], request.data['birthday']
        personal_data = PersonalData.objects.filter(date_of_birth=birthday)
        if not personal_data:
            return Response(data={"message": "There is no such employees"}, status=status.HTTP_400_BAD_REQUEST)
        personal_data.update(salary=F('salary')+increase_number)
        return Response(data={"message": "Everything updated"}, status=status.HTTP_200_OK)


class CompaniesView(ListAPIView):
    serializer_class = CompanySerializer
    permissions = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        start_creation_date, finish_creation_date = None, None
        if request.data and 'date1' in request.data and 'date2' in request.data:
            start_creation_date, finish_creation_date = request.data['date1'], request.data['date2']

        company = Company.objects.filter(
            creation_date__gte=start_creation_date,
            creation_date__lte=finish_creation_date,
            update_date__lte=finish_creation_date
        ).order_by('-creation_date').first()

        data = {
            'creation_date': company.creation_date,
            'update_date': company.update_date,
            'name': company.name,
            'web_site': company.web_site,
            'email': company.email,
            'post_index': company.post_index,
            'logo': company.logo
        }

        serializer = serialization(
            serializer=self.serializer_class,
            data=data,
            mode='get'
        )

        return Response(data=serializer.data, status=status.HTTP_200_OK)


@is_user_auth
@api_view(['POST'])
def companies_creation_view(request):
    companies_data = request.data.values()
    files = request.FILES('files')

    serialized_companies_data = []
    for i in range(len(companies_data)):
        file_name = default_storage.save(
            f'categories/{str(date.today().strftime("%d-%m-%Y"))}/'
            f'{str(datetime.now().strftime("%H-%M-%S"))}/{files[i].name}',
            files[i]
        )

        new_data = {
            "name": companies_data[i].get('name'),
            "web_site": companies_data[i].get("web_site"),
            "email": companies_data[i].get("email"),
            "post_index": companies_data[i].get("post_index"),
            "logo": f"/media/{file_name}"
        }
        serialized_data = CompanySerializer(data=new_data)
        if serialized_data.is_valid():
            serialized_companies_data.append(serialized_data.data)

    Company.objects.bulk_create(objs=serialized_companies_data)

    return Response(data=serialized_companies_data, status=status.HTTP_201_CREATED)
