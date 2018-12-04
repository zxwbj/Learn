import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    def test_store_single_respons(self):
        question = "What langage did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('Chinese')

        self.assertIn('Chinese', my_survey.responses)

    def test_store_three_responses(self):
        question = "What langage did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English.', 'France..', 'Japanese...']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)


if '__main__' == __name__:
    unittest.main()
