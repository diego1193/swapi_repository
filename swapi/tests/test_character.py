import json
from graphene_django.utils.testing import GraphQLTestCase
from swapi.schema import schema


class SeconTestCase(GraphQLTestCase):

    fixtures = ['app/fixtures/unittest.json']
    GRAPHQL_SCHEMA = schema

    def test_character_query(self):
        response = self.query(
            '''
            query{
                allCharacter{
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
        self.assertEqual(len(content['data']['allCharacter']['edges']), 2)
    
    def test_character_mutation(self):
        add_response = self.query(
            '''
                mutation addCharacter{
                    addCharacter(input:{name: "Leo Rou", gender: "male", height: "189", mass: "100", hairColor: "BLACK", eyeColor: "brown", skinColor: "light", birthYear: "5ABYU", films: [{title:"Revenge of the Sith"}]}){
                        character{
                            id,
                            name,
                            gender,
                            height,
                            mass,
                            hairColor,
                            eyeColor, 
                            skinColor, 
                            birthYear,
                            films{
                                edges{
                                    node{
                                        title
                                    }
                                }
                            }
                            }
                        }
                    }
            ''',
        )
        self.assertResponseNoErrors(add_response)
        add_content = json.loads(add_response.content)
        add_expected_result = {"id": "Q2hhcmFjdGVyTm9kZToz", "name": "Leo Rou", "gender": "male", "height": "189", "mass": "100", "hairColor": "BLACK", "eyeColor": "brown", "skinColor": "light", "birthYear": "5ABYU", "films": {"edges": [{"node": {"title": "Revenge of the Sith"}}]}}
        self.assertEqual(add_content['data']['addCharacter']['character'], add_expected_result)

        update_response = self.query(
            '''
                mutation addCharacter{
                    addCharacter(input:{id: "Q2hhcmFjdGVyTm9kZToz",name: "Leo Rou", gender: "male", height: "188", mass: "100", hairColor: "black", eyeColor: "brown", skinColor: "light", birthYear: "5ABYU", films: [{title:"Revenge of the Sith"}]}){
                        character{
                            id,
                            name,
                            gender,
                            height,
                            mass,
                            hairColor,
                            eyeColor, 
                            skinColor, 
                            birthYear,
                            films{
                                edges{
                                    node{
                                        title
                                    }
                                }
                            }
                            }
                        }
                    }
            ''',
        )
        self.assertResponseNoErrors(update_response)
        update_content = json.loads(update_response.content)
        update_expected_result = {"id": "Q2hhcmFjdGVyTm9kZToz", "name": "Leo Rou", "gender": "male", "height": "188", "mass": "100", "hairColor": "black", "eyeColor": "brown", "skinColor": "light", "birthYear": "5ABYU", "films": {"edges": [{"node": {"title": "Revenge of the Sith"}}]}}
        self.assertEqual(update_content['data']['addCharacter']['character'], update_expected_result)