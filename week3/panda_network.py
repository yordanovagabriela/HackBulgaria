import re

import json


from graph import bfs


class PandaAlreadyThere(Exception):
    pass


class PandasAlreadyFriends(Exception):
    pass


class Panda:

    def __init__(self, name, email, gender):
        self.name = name
        self.gender = gender
        check_email = ValidateEmail(email)
        if check_email:
            self.email = email
        else:
            raise ValueError
        self.list_of_friends = []

    def __str__(self):
        return "{}".format(self.name)

    def __repr__(self):
        return "{}".format(self.name)

    def __eq__(self, other):
        name_bool = self.name == other.name
        email_bool = self.email == other.email
        gender_bool = self.gender == other.gender
        return name_bool and email_bool and gender_bool

    def __hash__(self):
        return hash(self.name)

    def isMale(self):
        return self.gender == "male"

    def isFemale(self):
        return self.gender == "female"


def ValidateEmail(email):
    if re.search('([^@|\s]+@[^@]+\.[^@|\s]+)', email) == None:
        return False
    else:
        return re.search('([^@|\s]+@[^@]+\.[^@|\s]+)', email).group() == email


class PandaSocialNetwork:

    def __init__(self):
        self.panda_friends = {}
        self.list_of_pandas = []
        self.panda_email = []

    def add_panda(self, panda):
        if panda.email in self.panda_email:
            raise PandaAlreadyThere("PandaAlreadyThere")
        else:
            self.panda_friends[panda] = []
            self.list_of_pandas.append(panda)
            self.panda_email.append(panda.email)

    def has_panda(self, panda):
        if panda in self.panda_friends:
            return True
        return False

    def make_friends(self, panda1, panda2):
        if panda1 not in self.list_of_pandas:
            self.add_panda(panda1)
        if panda2 not in self.list_of_pandas:
            self.add_panda(panda2)
        if panda1 in self.panda_friends[panda2]:
            raise PandasAlreadyFriends("PandasAlreadyFriends")
        self.panda_friends[panda1] += [panda2]
        self.panda_friends[panda2] += [panda1]

    def are_friends(self, panda1, panda2):
        return panda1 in self.panda_friends[panda2]

    def friends_of(self, panda):
        if panda not in self.list_of_pandas:
            return False
        return self.panda_friends[panda]

    def connection_level(self, panda1, panda2):
        graph = self.panda_friends
        if panda1 not in self.list_of_pandas:
            return False
        if panda2 not in self.list_of_pandas:
            return False
        if bfs(graph, panda1, panda2) == 0:
            return "-1"
        return bfs(graph, panda1, panda2)

    def how_many_gender_in_network(self, panda, gender):
        count = 0
        for panda_user in self.network:
            current_connection_level = self.connection_level(panda, panda_user)
            if panda_user != panda and current_connection_level <= level and panda_user.gender() ==gender:
                count += 1
        return count

    def __repr__(self):
        save_dict = {}

        for panda in self.panda_friends:
            friends = [repr(panda_friend) for panda_friend in self.panda_friends[panda]]
            save_dict[repr(panda)] = friends

            return json.dumps(save_dict, indent=True)

    def save(self, filename):
        with open(filename, "w") as f:
            f.write(self.__repr__())

    @staticmethod
    def load(filename):
        pass
