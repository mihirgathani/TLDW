"""
Test suite for the summarize_transcripts module.
"""

import unittest
from utils.summarize_transcripts import get_ai_extract


class TestGetAIExtract(unittest.TestCase):
    """
    Test case for the get_ai_extract function.
    """

    def test_prompt_blank(self):
        """
        Test when the prompt is blank.
        """
        get_ai_extract('', 'hello')

    def test_text_blank(self):
        """
        Test when the text is blank.
        """
        get_ai_extract('hello','')
