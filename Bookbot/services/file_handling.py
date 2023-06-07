import os

BOOK_PATH = 'book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    zp = ['.', ',', ':', '!', ';', '?']
    if len(text[start:]) <= size:
        size = len(text[start:])

    while text[start + size - 1] not in zp:
        size -= 1

    try:

        if text[start + size + 1] in zp:
            print(text[start + size + 1])
            size -= 2
            while text[start + size - 1] not in zp:
                size -= 1
            return (text[start:start + size], len(text[start:start + size]))
        elif text[start + size] in zp and text[start + size - 1] in zp:
            print(text[start + size + 1])
            size -= 2
            while text[start + size - 1] not in zp:
                size -= 1
            return (text[start:start + size], len(text[start:start + size]))

        else:
            return (text[start:start + size], len(text[start:start + size]))
    except:
        return (text[start:start + size], len(text[start:start + size]))


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path,'r',encoding='utf-8')as file:
        tx=file.read()
        n=1
        m=0
        while m<len(tx):
            book[n]=_get_part_text(tx,m,PAGE_SIZE)[0].strip()
            n+=1
            m+=_get_part_text(tx,m,PAGE_SIZE)[1]


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(os.getcwd(), BOOK_PATH))