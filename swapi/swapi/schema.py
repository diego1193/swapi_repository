import graphene

from app.schema import Query as sw_query, Mutation as sw_mutation


class Query(sw_query):
    pass


class Mutation(sw_mutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)