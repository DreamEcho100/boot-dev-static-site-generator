import unittest
import os

from main import PUBLIC_DIR_NAME, STATIC_DIR_NAME, build, extract_title

class TestTextNode(unittest.TestCase):

    def test_build(self):
        self.assertTrue(os.path.exists(path=f'./{STATIC_DIR_NAME}'))
        build()
        self.assertTrue(os.path.exists(path=f'./{PUBLIC_DIR_NAME}'))

        # Recursuve check between the two directories
        def compare_dirs(dir1, dir2):
            for item in os.listdir(dir1):
                if os.path.isdir(f'{dir1}/{item}'):
                    compare_dirs(f'{dir1}/{item}', f'{dir2}/{item}')
                else:
                    self.assertTrue(os.path.exists(f'{dir2}/{item}'))

        compare_dirs(f'./{STATIC_DIR_NAME}', f'./{PUBLIC_DIR_NAME}')

    def test_valid_title(self):
        markdown = "# My Document Title"
        self.assertEqual(extract_title(markdown), "My Document Title")

    def test_title_with_special_characters(self):
        markdown = "# Title with !@#$%^&*() special characters"
        self.assertEqual(extract_title(markdown), "Title with !@#$%^&*() special characters")

    def test_empty_markdown(self):
        markdown = ""
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_no_title_present(self):
        markdown = "This is just plain text, no heading here."
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_multiline_markdown(self):
        markdown = "# First Heading\nThis is some content.\n# Second Heading"
        self.assertEqual(extract_title(markdown), "First Heading")

    def test_malformed_heading(self):
        markdown = " # Indented heading"
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_no_space_after_hash(self):
        markdown = "#Heading without space"
        with self.assertRaises(ValueError):
            extract_title(markdown)


if __name__ == "__main__":
    unittest.main()
