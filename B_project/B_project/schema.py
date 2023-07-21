import graphene
import B_app.schema

class Query(B_app.schema.Query, graphene.ObjectType):
    pass

class Mutation(B_app.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
