# Импорт load_dotenv.
from dotenv import load_dotenv 

# Импорт библиотеки для работы с окружением.
import os  

print('Hello from repository!')

def print_author():
    load_dotenv()
    author = os.getenv('AUTHOR')
    print(f"Автор проекта: {author}")

print_author()