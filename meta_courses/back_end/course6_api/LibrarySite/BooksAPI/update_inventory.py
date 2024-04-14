from django.core.management.base import BaseCommand
from .models import Book

class Command(BaseCommand):
    help = 'Atualiza o campo de inventário para livros existentes'

    def handle(self, *args, **options):
        # Percorre todos os livros e define o campo 'inventory' para um valor padrão
        for book in Book.objects.all():
            if book.inventory is None:
                book.inventory = 0  # Ou qualquer outro valor padrão desejado
                book.save()
        self.stdout.write(self.style.SUCCESS('Inventário atualizado com sucesso!'))