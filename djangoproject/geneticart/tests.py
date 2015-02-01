from django.test import TestCase
from models import Image


#testing the Image model
class ImageTestCase(TestCase):
    def setUp(self):
        pass

    def test_image_genome(self):
        genome = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        image = Image(genome = genome)

        self.assertEqual(genome, image.genome)
