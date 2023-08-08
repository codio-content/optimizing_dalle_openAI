import unittest
import sys
from io import StringIO
from PIL import Image
import os

# Import the student's solution file
import exerc

class TestGenerateImage(unittest.TestCase):
    
    def setUp(self):
        # Redirect stdout
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_prompt_refinement(self):
        # Test if the function is refining the prompt and generating an image
        try:
            exerc.generate_image('my test prompt')
            print("PASS: prompt_refinement")
        except Exception as e:
            print("FAIL: prompt_refinement", str(e))

    def test_image_generation(self):
        # Test if the image is generated and saved
        try:
            # Assert the image file was created
            self.assertTrue(os.path.isfile('my_img.png'))
            print("PASS: image_generation")
        except Exception as e:
            print("FAIL: image_generation", str(e))

    def tearDown(self):
        # Revert stdout
        sys.stdout = self.held


if __name__ == '__main__':
    unittest.main()
