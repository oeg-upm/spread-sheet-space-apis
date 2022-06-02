import requests


class SSSAPIS:

    def __init__(self, username=None, password=None, token=None):
        if not token and (not username or not password):
            err_msg = "Excepts username/password or token"
            raise Exception(err_msg)

        self.username = username
        self.password = password
        self.token = token
        self.base_uri = "https://www.spreadsheetspace.net/API/"

    def get_auth_headers(self):
        headers = {"Content-Type": "application/json"}
        if self.token:
            headers['token'] = self.token
        else:
            headers['username'] = self.username
            headers['password'] = self.password
        return headers

    def createPrivateView(self, data, template=None):
        """
        Create a file/view
        :param template: a path to the template file (xlsx)
        :param data: json
        :return:
        """
        url = self.base_uri + "createPrivateView"
        headers = self.get_auth_headers()
        response = requests.post(url, headers=headers, json=data)
        return response.json()

    def create_private_view(self, description="", recipients=[], table=[[]], isTable=False, hasHeaders=False,
                            rows=-1, cols=-1):
        """
        :param description:
        :param recipients:
        :param table:
        :param isTable:
        :param hasHeaders:
        :param rows:
        :param cols:
        :return:
        """
        data = {
            "description": description,
            "recipients": recipients,
            "table": table,
            "isTable": isTable,
            "hasHeader": hasHeaders,
            "rows": rows,
            "cols": cols
        }
        return self.createPrivateView(data=data)

    def updateView(self, data, template=None):
        """
        Update file/view
        :param template: a path to the template file (xlsx)
        :param data: json
        :return:
        """
        url = self.base_uri + "updateView"
        headers = self.get_auth_headers()
        response = requests.post(url, headers=headers, json=data)
        return response.json()

    def update_view(self, view_id, view_server="https://www.spreadsheetspace.net", table=[[]]):
        data = {
            "viewId": view_id,
            "viewServer": view_server,
            "table": table
        }
        return self.updateView(data)