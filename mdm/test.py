from django.test import TestCase
from configurations.management import call_command
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase


class CommandsTestCase(TestCase):
    def test_import_airport(self):
        " Test import_airport command."

        args = ['../modeling/airports.csv']
        opts = {}
        call_command('import_airport', *args, **opts)

    def test_import_board(self):
        " Test import_board command."

        args = ['../modeling/boards.csv']
        opts = {}
        call_command('import_board', *args, **opts)

    def test_import_hotel(self):
        " Test import_hotel command."

        args = ['../modeling/hotels.csv']
        opts = {}
        call_command('import_hotel', *args, **opts)

    def test_import_market(self):
        " Test import_market command."

        args = ['../modeling/markets.csv']
        opts = {}
        call_command('import_market', *args, **opts)

    def test_import_roomtype(self):
        " Test import_roomtype command."

        args = ['../modeling/roomtypes.csv']
        opts = {}
        call_command('import_roomtype', *args, **opts)

    def test_import_supplier(self):
        " Test import_supplier command."

        args = ['../modeling/suppliers.csv']
        opts = {}
        call_command('import_supplier', *args, **opts)


class AirportRestApiTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('mdm/', include('mdm.urls')),
    ]

    def test_list(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('airportmodel-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 0)


class BagTypeRestApiTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('mdm/', include('mdm.urls')),
    ]

    def test_list(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('bagtypemodel-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 0)


class BoardRestApiTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('mdm/', include('mdm.urls')),
    ]

    def test_list(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('boardmodel-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 0)


class FlightProviderRestApiTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('mdm/', include('mdm.urls')),
    ]

    def test_list(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('flightprovidermodel-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 0)


class HotelRestApiTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('mdm/', include('mdm.urls')),
    ]

    def test_list(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('hotelmodel-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 0)


class MarketRestApiTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('mdm/', include('mdm.urls')),
    ]

    def test_list(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('marketmodel-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 0)


class RoomTypeRestApiTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('mdm/', include('mdm.urls')),
    ]

    def test_list(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('roomtypemodel-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 0)


class SupplierRestApiTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('mdm/', include('mdm.urls')),
    ]

    def test_list(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('suppliermodel-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 0)
