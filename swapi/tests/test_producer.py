import json
from graphene_django.utils.testing import GraphQLTestCase
from swapi.schema import schema


class SixthTestCase(GraphQLTestCase):

    fixtures = ['app/fixtures/unittest.json']
    GRAPHQL_SCHEMA = schema

    def test_producer_query(self):
        response = self.query(
            '''
            query {
                allProducers{
                    edges{
                        node{
                            name
                        }
                    }
                }
            }
            '''
        )
        self.assertResponseNoErrors(response)
        content = json.loads(response.content)
        self.assertEqual(len(content["data"]["allProducers"]["edges"]), 4)

    def test_producer_mutation(self):

        add_response = self.query(
            '''
            mutation addNewProducer{
                addProducer(input:{name: "J.J. Adrian"}){
                    producer{
                        id,
                        name
                    }
                }
            }
            '''
        )
        self.assertResponseNoErrors(add_response)
        add_content = json.loads(add_response.content)
        add_expected_result = {"id": "UHJvZHVjZXJOb2RlOjU=", "name": "J.J. Adrian"}
        self.assertEqual(add_content["data"]["addProducer"]["producer"], add_expected_result)

        update_response = self.query(
            '''
            mutation addNewProducer{
                addProducer(input:{id: "UHJvZHVjZXJOb2RlOjU=",name: "J.J. Adrian Alfonso"}){
                    producer{
                        id,
                        name
                    }
                }
            }
            '''
        )
        self.assertResponseNoErrors(update_response)
        update_content = json.loads(update_response.content)
        update_expected_result = {"id": "UHJvZHVjZXJOb2RlOjU=", "name": "J.J. Adrian Alfonso"}
        self.assertEqual(update_content["data"]["addProducer"]["producer"], update_expected_result)
