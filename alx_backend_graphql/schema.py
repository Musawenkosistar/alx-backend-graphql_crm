import graphene


class CRMQuery(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(root, info):
        return "Hello, GraphQL!"


class Query(CRMQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
