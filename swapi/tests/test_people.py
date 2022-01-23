import json
from graphene_django.utils.testing import GraphQLTestCase
from swapi.schema import schema


class FirstTestCase(GraphQLTestCase):
    
    fixtures = ['app/fixtures/unittest.json']
    GRAPHQL_SCHEMA = schema

    def test_people_query(self):
        response = self.query(
            '''
            query {
                allPeople{
                    edges{
                        node{
                            name
                        }
                    }
                }
            }
            ''',
        )
        self.assertResponseNoErrors(response)

        content = json.loads(response.content)
        self.assertEqual(len(content['data']['allPeople']['edges']), 82)

    def test_people_mutation(self):
        # This validates the status code and if you get errors
        add_response = self.query(
            '''
                mutation addNewPeople{
                    addPeople(input:{name: "Mauricio Flow", gender: "male", height: "190", mass: "100", hairColor: "black", eyeColor: "brown", skinColor: "light", birthYear: "7ABY", homeWorldId: 32}){
                        people{
                            id,
                            name,
                            gender,
                            height,
                            mass,
                            hairColor,
                            eyeColor,
                            skinColor,
                            birthYear
                            homeWorld{
                                name,
                            }
                        }
                    }
                }
            ''',
        )
        self.assertResponseNoErrors(add_response)

        add_content = json.loads(add_response.content)
        add_expected_result = {"id": "UGVvcGxlTm9kZTo4NA==", "name": "Mauricio Flow", "gender": "MALE", "height": "190", "mass": "100", "hairColor": "BLACK", "eyeColor": "BROWN", "skinColor": "light", "birthYear": "7ABY", "homeWorld": {"name": "Chandrila"}}
        self.assertEqual(add_content['data']['addPeople']['people'], add_expected_result)

        udpdate_response = self.query(
            '''
                mutation addNewPeople{
                    addPeople(input:{id: "UGVvcGxlTm9kZTo4NA==", name: "Mauricio Flow", gender: "male", height: "190", mass: "100", hairColor: "black", eyeColor: "brown", skinColor: "light", birthYear: "7ABY", homeWorldId: 32}){
                        people{
                            id,
                            name,
                            gender,
                            height,
                            mass,
                            hairColor,
                            eyeColor,
                            skinColor,
                            birthYear
                            homeWorld{
                                name,
                            }
                        }
                    }
                }
            ''',
        )
        self.assertResponseNoErrors(add_response)

        update_content = json.loads(udpdate_response.content)
        update_expected_result = {"id": "UGVvcGxlTm9kZTo4NA==", "name": "Mauricio Flow", "gender": "MALE", "height": "190", "mass": "100", "hairColor": "BLACK", "eyeColor": "BROWN", "skinColor": "light", "birthYear": "7ABY", "homeWorld": {"name": "Chandrila"}}
        self.assertEqual(update_content['data']['addPeople']['people'], update_expected_result)
