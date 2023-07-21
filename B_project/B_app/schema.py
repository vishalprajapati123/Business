import graphene
from graphene_django import DjangoObjectType
from .models import Business
from django.db.models import Q


class BusinessType(DjangoObjectType):
    class Meta:
        model = Business
        fields = ("id", "name", "address", "owner_info", "employee_size", "investor_type", "contact_mail", "phone_number", "investment_stage", "company_type")


class Query(graphene.ObjectType):
    all_businesses = graphene.List(BusinessType)
    search_businesses = graphene.List(BusinessType, search=graphene.String())
    specific_business = graphene.Field(BusinessType, id=graphene.Int())
    
    def resolve_specific_business(root, info, id):
        return Business.objects.get(pk=id)
    
    def resolve_all_businesses(root, info):
        return Business.objects.all()
    
    def resolve_search_businesses(root, info, search):
        return Business.objects.filter(Q(name__icontains=search) | Q(address__icontains=search))


class CreateBusiness(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        address = graphene.String(required=True)
        owner_info = graphene.String(required=True)
        employee_size = graphene.Int(required=True)
        investor_type = graphene.String(required=True)
        contact_mail = graphene.String(required=True)
        phone_number = graphene.Int(required=True)
        investment_stage = graphene.String(required=True)
        company_type = graphene.String(required=True)

    business = graphene.Field(lambda: BusinessType)

    def mutate(self, info, name, address, owner_info, employee_size, investor_type, contact_mail, phone_number, investment_stage, company_type):
        business = Business(name=name, address=address, owner_info=owner_info, employee_size=employee_size, investor_type=investor_type, contact_mail=contact_mail, phone_number=phone_number, investment_stage=investment_stage, company_type=company_type)
        business.save()
        return CreateBusiness(business=business)

class UpdateBusiness(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        address = graphene.String()
        owner_info = graphene.String()
        employee_size = graphene.Int()
        investor_type = graphene.String()
        contact_mail = graphene.String()
        phone_number = graphene.Int()
        investment_stage = graphene.String()
        company_type = graphene.String()

    business = graphene.Field(lambda: BusinessType)

    def mutate(self, info, id, name=None, address=None, owner_info=None, employee_size=None, investor_type=None, contact_mail=None, phone_number=None, investment_stage=None, company_type=None):
        business = Business.objects.get(id=id)
        if name is not None:
            business.name = name
        if address is not None:
            business.address = address
        if owner_info is not None:
            business.owner_info = owner_info
        if employee_size is not None:
            business.employee_size = employee_size
        if investor_type is not None:
            business.investor_type = investor_type
        if contact_mail is not None:
            business.contact_mail = contact_mail
        if phone_number is not None:
            business.phone_number = phone_number
        if investment_stage is not None:
            business.investment_stage = investment_stage
        if company_type is not None:
            business.company_type = company_type
        business.save()
        return UpdateBusiness(business=business)

class DeleteBusiness(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    business = graphene.Field(BusinessType)

    def mutate(self, info, id):
        business = Business.objects.get(id=id)
        business.delete()
        return DeleteBusiness(business=None)


class Mutation(graphene.ObjectType):
    create_business = CreateBusiness.Field()
    update_business = UpdateBusiness.Field()
    delete_business = DeleteBusiness.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
