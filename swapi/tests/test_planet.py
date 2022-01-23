import json

from graphene_django.utils.testing import GraphQLTestCase

from swapi.schema import schema


class FifthTestCase(GraphQLTestCase):

    fixtures = ['app/fixtures/unittest.json']
    GRAPHQL_SCHEMA = schema

    def test_planet_query(self):
        response = self.query(
            '''
            query {
                allPlanets{
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
        self.assertEqual(len(content['data']['allPlanets']['edges']), 60)
    
    def test_planet_mutation(self):
        add_response = self.query(
            '''
            mutation addNewPlanet{
                addUpdatePlanet(input:{name: "Exodeen"}){
                    planet{
                        id,
                        name
                    }
                }
            }
            '''
        )
        self.assertResponseNoErrors(add_response)
        
        add_content = json.loads(add_response.content)
        add_expected_result = {"id": "UGxhbmV0Tm9kZTo2MQ==", "name": "Exodeen"}

        self.assertEqual(add_content["data"]["addUpdatePlanet"]["planet"], add_expected_result)

        update_response = self.query(
            '''
            mutation addUpdateNewPlanet{
                addUpdatePlanet(input:{name: "Tatooine", id:"UGxhbmV0Tm9kZTo2MQ=="}){
                    planet{
                        id,
                        name
                    }
                }
            }
            '''
        )

        self.assertResponseNoErrors(update_response)

        update_content = json.loads(update_response.content)
        update_expected_result = {"id": "UGxhbmV0Tm9kZTo2MQ==", "name": "Tatooine"}

        self.assertEqual(update_content["data"]["addUpdatePlanet"]["planet"], update_expected_result)
