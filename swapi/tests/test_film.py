import json
from graphene_django.utils.testing import GraphQLTestCase
from swapi.schema import schema


class FourthTestCase(GraphQLTestCase):

    fixtures = ['app/fixtures/unittest.json']
    GRAPHQL_SCHEMA = schema

    def test_film_query(self):
        response = self.query(
            '''
            query {
                allFilms{
                    edges{
                        node{
                            id,
                            title,
                        }
                    }
                }
            }
            '''
        )
        self.assertResponseNoErrors(response)

        content = json.loads(response.content)
        self.assertEqual(len(content['data']['allFilms']['edges']), 6)
    
    def test_film_mutation(self):

        add_response = self.query(
            '''
            mutation addNewFilm{
                addFilm(input:{title:"The Rise of Sky", episodeId:10, openingCrawl: "In a galaxy far far away in the...", releaseDate:"2019-12-20", director: 3, producer: [{name:"J.J. Abrams"}]}){
                    film{
                        id,
                        episodeId,
                        openingCrawl,
                        releaseDate,
                        director{
                            name
                        },
                        producer{
                            edges{
                                node{
                                    name
                                }
                            }
                        }
                    }
                }
            }
            '''
        )

        self.assertResponseNoErrors(add_response)

        add_content = json.loads(add_response.content)
        add_expected_result = {"id": "RmlsbU5vZGU6Nw==", "episodeId": 10, "openingCrawl": "In a galaxy far far away in the...", "releaseDate": "2019-12-20", "director": {"name": "Richard Marquand"}, "producer": {"edges": []}}

        self.assertEqual(add_content['data']['addFilm']['film'], add_expected_result)

        update_response = self.query(
            '''
            mutation addNewFilm{
                addFilm(input:{id: "RmlsbU5vZGU6Nw==" ,title:"The Rise", episodeId:11, openingCrawl: "In a galaxy ...", releaseDate:"2019-12-20", director: 3, producer: [{name:"J.J. Abrams"}]}){
                    film{
                        id,
                        episodeId,
                        openingCrawl,
                        releaseDate,
                        director{
                            name
                        },
                        producer{
                            edges{
                                node{
                                    name
                                }
                            }
                        }
                    }
                }
            }
            '''
        )
        self.assertResponseNoErrors(update_response)
        update_content = json.loads(update_response.content)
        update_expected_result = {"id": "RmlsbU5vZGU6Nw==", "episodeId": 11, "openingCrawl": "In a galaxy ...", "releaseDate": "2019-12-20", "director": {"name": "Richard Marquand"}, "producer": {"edges": []}}
        self.assertEqual(update_content['data']['addFilm']['film'], update_expected_result)
