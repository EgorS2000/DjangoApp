from rest_framework import serializers
from App.models import (
    Employee,
    Company,
    Bank
)


class BankSerializer(serializers.ModelSerializer):
    creation_date = serializers.DateTimeField(
        allow_null=False
    )
    update_date = serializers.DateTimeField(
        allow_null=False
    )
    name = serializers.CharField(
        max_length=36,
    )
    web_site = serializers.URLField(
        max_length=100,
    )
    email = serializers.EmailField(
        max_length=100,
    )

    class Meta:
        model = Bank
        fields = ('creation_date', 'update_date', 'name', 'web_site', 'email')


class CompanySerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=36
    )
    web_site = serializers.URLField(
        max_length=100
    )
    email = serializers.EmailField(
        max_length=100
    )
    post_index = serializers.IntegerField()
    logo = serializers.CharField(
        max_length=256
    )

    class Meta:
        model = Company
        fields = ('name', 'web_site', 'email', 'post_index', 'logo')


class EmployeeSerializer(serializers.ModelSerializer):
    creation_date = serializers.DateTimeField(
        allow_null=False
    )
    update_date = serializers.DateTimeField(
        allow_null=False
    )
    name = serializers.CharField(
        max_length=36,
    )
    surname = serializers.CharField(
        max_length=36,
    )
    job_position = serializers.CharField(
        max_length=36,
    )
    is_manager = serializers.BooleanField()
    is_admin = serializers.BooleanField()
    phone_number = serializers.CharField(
        max_length=16
    )

    class Meta:
        model = Employee
        fields = (
            'creation_date', 'update_date', 'name',
            'surname', 'job_position', 'is_manager',
            'is_admin', 'phone_number'
        )
