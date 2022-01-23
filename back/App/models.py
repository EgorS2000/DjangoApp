from django.db import models


class CommonInfo(models.Model):
    creation_date = models.DateTimeField(
        auto_now_add=True,
        help_text = "Object creation time",
        verbose_name="creation_date"
    )
    update_date = models.DateTimeField(
        auto_now=True,
        help_text="Object update time",
        verbose_name="update_date"
    )

    class Meta:
        abstract = True
        verbose_name = "CommonInfo"
        verbose_name_plural = "CommonInfo"


class Bank(CommonInfo):
    name = models.CharField(
        max_length=36,
        null=False,
        help_text="Bank name",
        verbose_name="bank_name"
    )
    web_site = models.URLField(
        null=False,
        help_text="website link",
        verbose_name="bank_website_link"
    )
    email = models.EmailField(
        null=False,
        help_text="bank email",
        verbose_name="bank_email"
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Bank"
        verbose_name_plural = "Banks"


class Company(CommonInfo):
    name = models.CharField(
        max_length=36,
        null=False,
        help_text="Company name",
        verbose_name="company_name"
    )
    web_site = models.URLField(
        null=False,
        help_text="website link",
        verbose_name="company_website_link"
    )
    email = models.EmailField(
        null=False,
        help_text="company email",
        verbose_name="company_email"
    )
    post_index = models.IntegerField(
        null=False,
        help_text="post index",
        verbose_name="company_post_index"
    )
    logo = models.ImageField(
        null=False,
        upload_to="'media/company/% Y/% m/% d/'"
    )
    company = models.ManyToManyField(
        Bank,
        help_text="Banks which work with company",
        verbose_name="company_banks"
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"


class Employee(CommonInfo):
    name = models.CharField(
        max_length=36,
        null=False,
        help_text="Employee name",
        verbose_name="employee_name"
    )
    surname = models.CharField(
        max_length=36,
        null=False,
        help_text="Employee surname",
        verbose_name="employee_surname"
    )
    job_position = models.CharField(
        max_length=36,
        null=False,
        help_text="Employee job position",
        verbose_name="employee_job_position"
    )
    is_manager = models.BooleanField(
        null=False,
        help_text="Employee is manager",
        verbose_name="employee_is_manager"
    )
    is_admin = models.BooleanField(
        null=False,
        help_text="Employee is admin",
        verbose_name="employee_is_admin"
    )
    phone_number = models.CharField(
        max_length=16,
        null=False,
        help_text="Employee phone number",
        verbose_name="employee_phone_number"
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        help_text="Company where employee are working",
        verbose_name="employee_company"
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"