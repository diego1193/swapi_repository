import json
from graphene_django.utils.testing import GraphQLTestCase
from swapi.schema import schema


class ThirdTestCase(GraphQLTestCase):

    fixtures = ['app/fixtures/unittest.json']
    GRAPHQL_SCHEMA = schema

    def test_directors_query(self):
        response = self.query(
            '''
                query {
                    allDirectors{
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
        self.assertEqual(len(content['data']['allDirectors']['edges']), 3)
    
    def test_directors_mutation(self):
        
        add_response = self.query(
            '''
            mutation addNewDirector{
                addDirector(input:{name: "J.J. Json"}){
                    director{
                        id,
                        name
                    }
                }
            }
            '''
        )

        self.assertResponseNoErrors(add_response)
        add_context = json.loads(add_response.content)
        add_expected_result = {"id": "RGlyZWN0b3JOb2RlOjQ=", "name": "J.J. Json"}

        self.assertEqual(add_context['data']['addDirector']["director"], add_expected_result)

        update_response = self.query(
            '''
            mutation addNewDirector{
                addDirector(input:{id: "RGlyZWN0b3JOb2RlOjQ=",name: "J.W. Json"}){
                    director{
                        id,
                        name
                    }
                }
            }
            '''
        )
        
        self.assertResponseNoErrors(update_response)
        update_content = json.loads(update_response.content)
        update_expected_result = {"id": "RGlyZWN0b3JOb2RlOjQ=", "name": "J.W. Json"}
        self.assertEqual(update_content['data']['addDirector']['director'], update_expected_result)
