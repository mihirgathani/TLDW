"""
Test module for the Streamlit App.

This module contains unit tests to verify the behavior of the Streamlit App.
"""
import unittest
import pandas as pd
from streamlit.testing.v1 import AppTest
from unittest.mock import patch


from utils.process_transcripts import get_transcript
from utils.summarize_transcripts import get_ai_extract
from utils.bert_get_recommendations import get_bert_recs
from utils.minilm_get_recommedations import get_minilm_recs
from utils.tdidf_get_recommendations import get_tdidf_recs
from utils.chat_to_search import get_search_result


class TestStreamlitApp(unittest.TestCase):
    """
    Test case class for Streamlit App.

    This class defines multiple test cases to verify the behavior of the Streamlit App.
    """
    def setUp(self):
        """
        Set up the test environment before each test case execution.

        This method initializes the AppTest instance to test the Streamlit App.
        """
        self.app_test = AppTest.from_file('../streamlit_app.py', default_timeout=100).run()

    def test_empty_youtube(self):
        """
        Test case to check behavior with an empty YouTube link input.

        This test case inputs an empty string as the YouTube link and checks
        if the Streamlit app outputs a ValueError.
        """
        self.app_test.text_input[0].input(" ").run()
        self.assertRaises(ValueError)

    @patch('utils.process_transcripts.get_transcript')
    @patch('utils.summarize_transcripts.get_ai_extract')
    def test_get_transcript_summary_keywords(self, mock_get_transcript, mock_get_ai_extract):
        """
        Test case to verify transcript, summary, and keywords retrieval.

        This test case inputs a valid YouTube link and checks if the Streamlit app
        successfully retrieves the transcript, summary, and keywords from Gemini.
        """
        mock_get_transcript.return_value = "Mocked transcript"
        mock_get_ai_extract.return_value = "Mocked summary"

        self.app_test.text_input[0].input("https://www.youtube.com/watch?v=dQw4w9WgXcQ").run()

        self.assertIsNotNone(self.app_test.session_state.transcript)
        self.assertIsNotNone(self.app_test.session_state.summary)

    @patch('utils.process_transcripts.get_transcript')
    @patch('utils.summarize_transcripts.get_ai_extract')
    def test_selected_content_type_ted(self, mock_get_transcript, mock_get_ai_extract):
        """
        Test case to verify selected content type is 'ted'.

        This test case inputs a valid YouTube link and selects 'TED Talks' as
        the content type. It then checks if the selected_content_type is 'ted'.
        """

        mock_get_transcript.return_value = "Mocked transcript"
        mock_get_ai_extract.return_value = "Mocked summary"

        self.app_test.text_input[0].input("https://www.youtube.com/watch?v=dQw4w9WgXcQ").run()

        self.app_test.radio[0].set_value("TED Talks").run()
        selected_content_type = self.app_test.session_state.selected_content_type
        self.assertEqual(selected_content_type, "ted")

    @patch('utils.process_transcripts.get_transcript')
    @patch('utils.summarize_transcripts.get_ai_extract')
    def test_selected_content_type_podcast(self, mock_get_transcript, mock_get_ai_extract):
        """
        Test case to verify selected content type is 'ted'.

        This test case inputs a valid YouTube link and selects 'TED Talks' as
        the content type. It then checks if the selected_content_type is 'ted'.
        """

        mock_get_transcript.return_value = "Mocked transcript"
        mock_get_ai_extract.return_value = "Mocked summary"

        self.app_test.text_input[0].input("https://www.youtube.com/watch?v=dQw4w9WgXcQ").run()

        self.app_test.radio[0].set_value("Podcasts").run()
        selected_content_type = self.app_test.session_state.selected_content_type
        self.assertEqual(selected_content_type, "podcast")

    @patch('utils.process_transcripts.get_transcript')
    @patch('utils.summarize_transcripts.get_ai_extract')
    def test_sbert_recommender(self, mock_get_transcript, mock_get_ai_extract):
        """
        Test case to verify SBERT recommender behavior.

        This test case inputs a valid YouTube link, selects 'TED Talks' as
        the content type, and clicks on the SBERT Recommender button. It then
        checks if the recommendations are displayed correctly.
        """
        mock_get_transcript.return_value = "Mocked transcript"
        mock_get_ai_extract.return_value = "Mocked summary"

        self.app_test.text_input[0].input("https://www.youtube.com/watch?v=dQw4w9WgXcQ").run()
        self.app_test.radio[0].set_value("TED Talks").run()
        self.app_test.button[0].click().run()
        self.assertEqual(self.app_test.header[2].value, "Top 3 SBERT Recommendations")
        self.assertIsNotNone(self.app_test.get("expandable"))

    @patch('utils.process_transcripts.get_transcript')
    @patch('utils.summarize_transcripts.get_ai_extract')
    def test_minilm_recommender(self, mock_get_transcript, mock_get_ai_extract):
        """
        Test case to verify MiniLM recommender behavior.

        This test case inputs a valid YouTube link, selects 'TED Talks' as the content type,
        and clicks on the MiniLM Recommender button. It then checks if the recommendations
        are displayed correctly.
        """
        mock_get_transcript.return_value = "Mocked transcript"
        mock_get_ai_extract.return_value = "Mocked summary"

        self.app_test.text_input[0].input("https://www.youtube.com/watch?v=dQw4w9WgXcQ").run()
        self.app_test.radio[0].set_value("TED Talks").run()
        self.app_test.button[1].click().run()
        self.assertEqual(self.app_test.header[2].value, "Top 3 MiniLM Recommendations")
        self.assertIsNotNone(self.app_test.get("expandable"))

    @patch('utils.process_transcripts.get_transcript')
    @patch('utils.summarize_transcripts.get_ai_extract')
    def test_tfidf_recommender(self, mock_get_transcript, mock_get_ai_extract):
        """
        Test case to verify TF-IDF recommender behavior.

        This test case inputs a valid YouTube link, selects 'TED Talks' as the content type,
        and clicks on the TF-IDF Recommender button. It then checks if the recommendations
        are displayed correctly.
        """
        mock_get_transcript.return_value = "Mocked transcript"
        mock_get_ai_extract.return_value = "Mocked summary"

        self.app_test.text_input[0].input("https://www.youtube.com/watch?v=dQw4w9WgXcQ").run()
        self.app_test.radio[0].set_value("TED Talks").run()
        self.app_test.button[2].click().run()
        self.assertEqual(self.app_test.header[2].value, "Top 3 TF-IDF Recommendations")
        self.assertIsNotNone(self.app_test.get("expandable"))

    def test_chatbot(self):
        """
        Test case to verify chatbot functionality.

        This test case inputs a valid YouTube link, selects 'TED Talks' as the content type,
        and checks if the chatbot section is displayed correctly. It then inputs a question
        and verifies if the chatbot responds appropriately.
        """
        self.app_test.text_input[0].input("https://www.youtube.com/watch?v=dQw4w9WgXcQ").run()
        self.app_test.radio[0].set_value("TED Talks").run()
        self.assertEqual(self.app_test.header[2].value, "🔎 Learn More - Chat with GEMINI")
        self.app_test.chat_input[0].set_value("What is rick-rolling?").run()
        self.assertEqual(self.app_test.chat_message[1].markdown[0].value, "What is rick-rolling?")
        self.assertIsNotNone(self.app_test.chat_message[0].markdown[0].value)

if __name__ == "__main__":
    unittest.main()
