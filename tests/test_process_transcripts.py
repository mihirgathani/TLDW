"""
Module for testing the processTranscripts module.
"""

import unittest
from utils.process_transcripts import get_video_id,\
get_video_transcript, formatTranscript, getTranscript


class TestProcessTranscripts(unittest.TestCase):
    """
    Test cases for processTranscripts module.
    """

    def test_smoke(self):
        """Smoke test to check if transcript can be fetched."""
        with self.assertRaises(ValueError):
            getTranscript('https://www.youtube.com/watch?v=tlWuP7wESZw')

    def test_video_id_blank(self):
        """Test handling of blank video ID."""
        with self.assertRaises(ValueError):
            get_video_id('')

    def test_video_id_wrong_length(self):
        """Test handling of incorrect video ID length."""
        with self.assertRaises(ValueError):
            get_video_id('https://www.youtube.com/watch?v=tlWuP7wESZw456')

    def test_improper_id_len(self):
        """Test handling of improper video ID."""
        with self.assertRaises(ValueError):
            get_video_id('https://www.youtube.com/watch?y=tlWuP7wESZw456')

    def test_alphanumeric(self):
        """Test handling of non-alphanumeric characters in video ID."""
        with self.assertRaises(ValueError):
            get_video_id('https://www.youtube.com/watch?v=tlWuP#wESZw456')

    def test_transcript_language(self):
        """Test fetching transcript in a different language."""
        with self.assertRaises(ValueError):
            get_video_transcript('https://www.youtube.com/watch?v=LpP4rtjACM8')  # Hindi video

    def test_empty_transcript(self):
        """Test handling of empty transcript."""
        with self.assertRaises(ValueError):
            formatTranscript('https://www.youtube.com/watch?v=LpP4rtjACM8')  # Hindi video

    def test_invalid_url(self):
        """Test handling of invalid URL."""
        with self.assertRaises(ValueError):
            getTranscript('https://www.reddit.com/watch?v=LpP4rtjACM8')
