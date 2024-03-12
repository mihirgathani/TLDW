

"""
Test suite for the chat_to_search module.
"""
import unittest
from unittest.mock import patch
from utils.chat_to_search import get_search_result

class TestGetSearchResult(unittest.TestCase):
    """
    Test case for the get_search_result function.
    """

    @patch('utils.chat_to_search.get_search_result')
    def test_chatbot(self, mock_get_search_result):
        """
        Test when call chatbot api
        """
        mock_get_search_result.return_value = "Mocked chatbot response"

        result = get_search_result('context', 'hello')
        self.assertNotEqual(result, "", "Result should not be empty.")

if __name__ == '__main__':
    unittest.main()
