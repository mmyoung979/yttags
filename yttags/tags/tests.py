# Django imports
from django.test import TestCase

# Project imports
from yttags.tags.utils import get_video_data


# Should always work anywhere
class SanityTestCase(TestCase):
    def test_exceptions_get_caught(self):
        self.assertEqual(2 + 2, 4)
        with self.assertRaises(ZeroDivisionError):
            1 / 0


class TagsTestSuite(TestCase):
    def test_tag_collection(self):
        data = get_video_data('7vPL1WG4054')
        self.assertEqual(data['title'], 'Brand Breakdown | Amazon | Forward Vibe')
        self.assertEqual(data['thumbnail'], 'https://i.ytimg.com/vi/7vPL1WG4054/mqdefault.jpg')
        self.assertEqual(data['tags'][0], 'forward vibe')
