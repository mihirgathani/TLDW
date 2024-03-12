

"""
Test suite for the chat_to_search module.
"""
import unittest
from unittest.mock import patch
from unittest import mock
from utils.chat_to_search import get_search_result

class TestGetSearchResult(unittest.TestCase):
    """
    Test case for the get_search_result function.
    """
    @patch('langchain_google_genai.ChatGoogleGenerativeAI')  # Mock the entire class
    def test_get_search_result_with_session_state(self, mock_llm):
        """Tests the get_search_result function with session state."""
        context = "This is some context for the query."
        user_prompt = "What is the answer to the question?"

        # Configure the mock to return a desired response
        mock_response = "Mocked Gemini response for prompt"
        mock_llm.return_value = mock_response

        response = get_search_result(context, user_prompt)
        self.assertNotEqual(response, "", "Result should not be empty.")
        # self.assertNotIn("Invoking Gemini...", response)  # Ensure no actual call

    # @patch('utils.chat_to_search.get_search_result.ChatGoogleGenerativeAI')
    # # @patch('langchain_google_genai.ChatGoogleGenerativeAI')
    # def test_chatbot(self, mock_get_search_result):
    #     """
    #     Test when call chatbot api
    #     """

    #     mock_response = mock.Mock(return_value=None)
    #     mock_response.candidates = [
    #         mock.Mock(content=mock.Mock(parts=[mock.Mock(text='rocks')])),
    #         # You can add more mock candidates if needed
    #     ]

    #     mock_get_search_result.return_value = mock_response
    #     # mock_get_search_result.return_value = "Mocked chatbot response"
    #     # mock_ChatGoogleGenerativeAI = "generate"
    #     result = get_search_result('context', 'hello')
    #     self.assertNotEqual(result, "", "Result should not be empty.")

    # @patch('utils.chat_to_search.ChatGoogleGenerativeAI')
    # @patch('utils.chat_to_search.DuckDuckGoSearchRun')
    # def test_get_search_result_with_valid_input(self, mock_search_run, mock_ggai):
    #     """
    #     Test when valid input is provided.
    #     """
    #     # Set up mock return values and session state
    #     context = "Sample context"
    #     user_prompt = "Sample prompt"
    #     st_session_state = {
    #         "messages": [{"role": "user", "content": user_prompt}],
    #         "context": context
    #     }

    #     mock_response = "Mocked chatbot response"
    #     mock_search_run.return_value.run.return_value = mock_response

    #     # Call the function
    #     with patch.dict('utils.chat_to_search.st.session_state', st_session_state):
    #         result = get_search_result(context, user_prompt)

    #     # Assert that the function returns the expected response
    #     self.assertEqual(result, mock_response)

    # @patch('utils.chat_to_search.ChatGoogleGenerativeAI')
    # @patch('utils.chat_to_search.DuckDuckGoSearchRun')
    # def test_get_search_result_with_invalid_input(self, mock_search_run, mock_ggai):
    #     """
    #     Test when invalid input is provided.
    #     """
    #     # Set up mock return values and session state
    #     context = None
    #     user_prompt = "Sample prompt"
    #     st_session_state = {
    #         "messages": [{"role": "user", "content": user_prompt}],
    #         "context": context
    #     }

    #     mock_response = "Mocked chatbot response"
    #     mock_search_run.return_value.run.return_value = mock_response

    #     # Call the function
    #     with patch.dict('utils.chat_to_search.st.session_state', st_session_state):
    #         result = get_search_result(context, user_prompt)

    #     # Assert that the function returns None for invalid input
    #     self.assertIsNone(result)
if __name__ == '__main__':
    unittest.main()
