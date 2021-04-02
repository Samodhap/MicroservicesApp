import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Products
from .serializers import ProductCatalogSerializer

# initialize the APIClient app
client = Client()


class GetAllProducts(TestCase):
    def setUp(self):
        Products.objects.create(
            product_serial_num='bp01', product_name='Backpack 1', price='3500', available_quantity='500')
        Products.objects.create(
            product_serial_num='bp02', product_name='Backpack 2', price='5000', available_quantity='300')
        Products.objects.create(
            product_serial_num='bp03', product_name='Backpack 3', price='10000', available_quantity='250')

    def test_get_all_products(self):
        response = client.get(reverse('products'))
        puppies = Products.objects.all()
        serializer = ProductCatalogSerializer(puppies, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetOneProduct(TestCase):
    def setUp(self):
        self.pb1=Products.objects.create(
            product_serial_num='bp01', product_name='Backpack 1', price='3500', available_quantity='500')
        self.pb2=Products.objects.create(
            product_serial_num='bp02', product_name='Backpack 2', price='5000', available_quantity='300')
        self.pb3=Products.objects.create(
            product_serial_num='bp03', product_name='Backpack 3', price='10000', available_quantity='250')

    def test_get_valid_one_product(self):
        response = client.get(reverse('product', kwargs={'pk': self.pb2.pk}))
        product = Products.objects.get(pk=self.pb2.pk)
        serializer = ProductCatalogSerializer(product)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_one_product(self):
        response = client.get(reverse('product', kwargs={'pk': 'dpi'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewProductTest(TestCase):
    def setUp(self):
        self.valid_payload = {
            'product_serial_num': 'bp012',
            'product_name': 'Backpack 12',
            'price': 3500,
            'available_quantity': 100
        }
        self.invalid_payload = {
            'product_serial_num': '',
            'product_name': 'Backpack 16',
            'price': 2000,
            'available_quantity': 300
        }

    def test_create_valid_puppy(self):
        response = client.post(
            reverse('add-products'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_puppy(self):
        response = client.post(
            reverse('add-products'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateProductTest(TestCase):
    def setUp(self):
        self.pb1 = Products.objects.create(
            product_serial_num='bp01', product_name='Backpack 1', price='3500', available_quantity='500')
        self.pb2 = Products.objects.create(
            product_serial_num='bp02', product_name='Backpack 2', price='5000', available_quantity='300')
        self.pb3 = Products.objects.create(
            product_serial_num='bp03', product_name='Backpack 3', price='10000', available_quantity='250')

        self.valid_payload = {
            'product_serial_num': 'bp02',
            'product_name':'Backpack 2',
            'price': 3000,
            'available_quantity': 80
        }
        self.invalid_payload = {
            'product_serial_num': '',
            'product_name': 'Backpack 2',
            'price': 2000,
            'available_quantity': 300
        }

    def test_update_valid_puppy(self):
        response = client.post(
            reverse('update-product', kwargs={'pk': self.pb2.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_invalid_puppy(self):
        response = client.post(
            reverse('update-product', kwargs={'pk': self.pb2.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleProductTest(TestCase):

    def setUp(self):
        self.pb1 = Products.objects.create(
            product_serial_num='bp01', product_name='Backpack 1', price='3500', available_quantity='500')
        self.pb2 = Products.objects.create(
            product_serial_num='bp02', product_name='Backpack 2', price='5000', available_quantity='300')
        self.pb3 = Products.objects.create(
            product_serial_num='bp03', product_name='Backpack 3', price='10000', available_quantity='250')

    def test_valid_delete_puppy(self):
        response = client.delete(
            reverse('delete-product', kwargs={'pk': self.pb2.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_puppy(self):
        response = client.delete(
            reverse('delete-product', kwargs={'pk': 'bpO2'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)