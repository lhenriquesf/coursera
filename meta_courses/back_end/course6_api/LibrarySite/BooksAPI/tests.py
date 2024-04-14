from django.test import TestCase
import json
import unittest
import requests
# Create your tests here.

class TestBookCreation(unittest.TestCase):
    def test_create_book(self):
        # Dados do livro a serem criados
        book_data = {
            "title": "Código limpo",
            "author": "Robert C. Martin",
            "price": 111.00
        }

        # Faz a solicitação POST para criar o livro
        response = requests.post('http://127.0.0.1:8000/api/books', json=book_data)

        # Verifica se a resposta foi bem-sucedida (status code 201)
        self.assertEqual(response.status_code, 201)

        # Verifica se o livro foi criado corretamente no banco de dados
        created_book = response.json()
        self.assertEqual(created_book['title'], book_data['title'])
        self.assertEqual(created_book['author'], book_data['author'])
        self.assertEqual(created_book['price'], book_data['price'])

if __name__ == '__main__':
    unittest.main()

