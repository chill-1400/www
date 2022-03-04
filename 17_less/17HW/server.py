from http.server import HTTPServer, CGIHTTPRequestHandler
import sqlite3


def server():
    server_data = ("localhost", 8000)
    server = HTTPServer(server_data, CGIHTTPRequestHandler)
    print("Server started")
    server.serve_forever()

if __name__ == "__main__":
    server()

# HTTPServer - за счёт этого класса мы сможем создать локальный сервер
# CGIHTTPRequestHandler - за счет этого класса мы сможем отслеживать переходы пользователя по разным страницам
# server.serve_forever() - чтобы наш локальный сервер работал бесконечно (сайт постоянно обрабатывался)

# python manage.py startapp blog - создание приложения
# в views описываются ф-ии(классы), которые срабатывают при переходе по юрл
