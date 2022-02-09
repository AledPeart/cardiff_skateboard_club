from django.test import TestCase
from .forms import ProductForm

from django.test import TestCase
from .forms import ProductForm


class TestProductForm(TestCase):
    """
    Test that the product form works
    """

    def test_name_is_required(self):
        """
        Test if form submits without name field
        """
        form = ProductForm({
            'name': '',
            'description': 'test',
            'price': 'test',
            'image': 'test',
        })
        # Form should not be valid - name required
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['name'][0], 'This field is required.')

    def test_description_is_required(self):
        """
        Test if form submits without description field
        """
        form = ProductForm({
            'name': 'test',
            'description': '',
            'price': 'test',
            'image': 'test',
        })
        # Form should not be valid - description required
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['description'][0], 'This field is required.')

    def test_price_is_required(self):
        """
        Test if form submits without price field
        """
        form = ProductForm({
            'name': 'test',
            'description': 'test',
            'price': '',
            'image': 'test',
        })
        # Form should not be valid - price required
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        # Check error message is correct
        self.assertEqual(
            form.errors['price'][0], 'This field is required.')

    def test_image_is_not_required(self):
        """
        Test if form submits without image field
        """
        form = ProductForm({
            'name': 'test',
            'description': 'test',
            'price': 'test',
            'image': '',
        })
        # Form should be valid - image not required
        self.assertTrue(form.is_valid())
       
       
# class TestProductForm(TestCase):

#     def test_product_name_required(self):
#         """
#         Test that the name field is required
#         """
#         form = ProductForm({'name': ''})
#         #Test should fail as form not valid
#         self.assertFalse(form.is_valid())
#         self.assertIn('name', form.errors.keys())
#         #Checks that the error message is correct - should pass
#         self.assertEqual(form.errors['name'][0], 'This field is required.')

#     def test_product_code_field_is_not_required(self):
#         """
#         Test that the product code field is not required
#         """
#         form = ProductForm({'name': 'Test Product Code Field'})
#          #Test should pass as form valid
#         self.assertTrue(form.is_valid())

