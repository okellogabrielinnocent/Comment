from datetime import datetime
from typing import List


class Responses:

    class Response:
        def __init__(self, id, com, com_id):
            self.id = id
            self.comment = com
            self.comment_id = com_id
            self.date = datetime.now()

    responses: List[Response] = []

    def add_response(self, comment_id):
        resp = ""
        while not resp:
            resp = input("Add response")

        self.responses.append(self.Response(
            len(self.responses),
            resp,
            len(self.responses) + 1,
        ))

    def delete_response(self, comment_id):
        resp = ""
        while not resp:
            resp = input("Add response")

        self.responses.append(self.Response(
            len(self.responses),
            resp,
            len(self.responses) + 1,
        ))



