class Group:

    def __init__(self, base_url=None, username=None, password=None):
        self.base_url = base_url
        self.username = username
        self.password = password

    def __repr__(self):
        return "%s:%s;%s;".format(self.base_url, self.username, self.password)
