"""
Test suite for the summarize_transcripts module.
"""

import unittest
from utils.summarize_transcripts import get_ai_extract
from unittest.mock import patch


class TestGetAIExtract(unittest.TestCase):
    """
    Test case for the get_ai_extract function.
    """

    def test_prompt_blank(self):
        """
        Test when the prompt is blank.
        """
        with self.assertRaises(ValueError):
            get_ai_extract('', 'hello')

    def test_text_blank(self):
        """
        Test when the text is blank.
        """
        with self.assertRaises(ValueError):
            get_ai_extract('hello','')

    @patch('summarize.genai_model.generate_content')
    def test_api_call(self, mock_generate_content):
        """
        Test API call behavior.
        """
        # Mocked response from the API client
        mock_response = type('Response', (), {'candidates': [type('Candidate', (), {'content': type('Content', (), {'parts': ['Actual extracted text']})})()]})
        
        
        mock_generate_content.return_value = mock_response

    
        result = get_ai_extract('What is the last word of the sentence', 'tldw rocks')


        self.assertEqual(result, 'rocks')