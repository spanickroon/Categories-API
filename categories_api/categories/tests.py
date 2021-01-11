"""Module with tests."""

from django.urls import include, path
from rest_framework import status
from rest_framework.test import APITestCase

import json
import os


class CategoriesApiTest(APITestCase):
    """A class that contains test methods."""

    main_url = 'http://testserver/categories/'

    def read_json_data(self, file_path: str) -> object:
        """The method that reads data from the json file."""
        with open(file_path) as rf:
            return json.loads(rf.read())

    def test_post_data_status_code(self) -> None:
        """Testing post request for status code."""
        url = self.main_url
        data = {
            'name': '',
            'children': []
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_data_count_categories(self) -> None:
        """Testing post request for number of categories."""
        url = self.main_url
        data = {
            'name': '',
            'children': []
        }
        response = self.client.post(url, data, format='json')
        correct_answer = {'status': 201, 'count_categories': 1}

        self.assertEqual(response.data, correct_answer)

    def test_post_data(self) -> None:
        """Testing post request for correctness."""
        url = self.main_url
        data = self.read_json_data(
            os.path.join(
                'static',
                'test_data',
                'test_data_post.json')
        )
        response = self.client.post(url, data, format='json')
        correct_answer = {'status': 201, 'count_categories': 15}

        self.assertEqual(response.data, correct_answer)

    def test_get_data_id_2_8(self) -> None:
        """Testing a get request for getting categories with IDs 2 and 8."""
        url = self.main_url
        data = self.read_json_data(
            os.path.join(
                'static',
                'test_data',
                'test_data_post.json')
        )

        response = self.client.post(url, data, format='json')
        correct_answer = {'status': 201, 'count_categories': 15}

        self.assertEqual(response.data, correct_answer)

        url = self.main_url + '2/'
        correct_data = self.read_json_data(
            os.path.join(
                'static',
                'test_data',
                'test_data_get_1.json')
        )

        request = self.client.get(url, format='json')

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(request.content), correct_data)

        url = self.main_url + '8/'
        correct_data = self.read_json_data(
            os.path.join(
                'static',
                'test_data',
                'test_data_get_2.json')
        )

        request = self.client.get(url, format='json')

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(request.content), correct_data)


def main():
    test_obj = CategoriesApiTest()


if __name__ == '__main__':
    main()
