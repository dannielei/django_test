import graphene

class Query(graphene.ObjectType):
    hello=graphene.String()

    def resolve_hello(self,info):
        return 'django'

schema=graphene.Schema(query=Query)
