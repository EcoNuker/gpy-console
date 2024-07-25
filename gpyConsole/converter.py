"""
Class to convert function parameters
"""

import guilded
from guilded.utils import get
import re2


class Converter:
    """
    Holds conversion logic.
    To modify its behavior Subclass it or add converters using the add_converter method.
    """

    def __init__(self, client):
        self.client: guilded.Client = client
        self.convert_mapping = {
            bool: self.bool_converter,
            # guilded.User: self.user_converter,
            int: self.int_converter,
            guilded.Server: self.server_converter,
        }

    def get_id_match(self, id):
        match = re2.search(
            r"[a-zA-Z0-9]{8}", id
        )  # NOTE: discord = re2.search(r"[0-9]{15,21}", id)
        return True if match else False

    def bool_converter(self, param: str):
        if param.lower() in ["y", "yes", "on", "true", "1"]:
            return True
        elif param.lower() in ["n", "no", "off", "false", "0"]:
            return False
        raise TypeError(f"Cannot convert {param} into Bool")

    # def user_converter(self, param):
    #     if self.get_id_match(param):
    #         return self.client.get_user(int(param))
    #     else:
    #         for user in self.client.users:
    #             if user.name + "#" + user.discriminator == param:
    #                 return user
    #         else:
    #             raise TypeError(f"Cannot convert {param} to User")

    def int_converter(self, param):
        try:
            return int(param)
        except TypeError:
            raise TypeError(f"Cannot convert {param} to int")

    def server_converter(self, param):
        if self.get_id_match(param):
            return self.client.get_server(param)
        else:
            server = get(self.client.servers, name=param)
            if server:
                return server
            else:
                raise TypeError(f"Cannot convert {param} to Server")

    def get_converter(self, type):
        try:
            return self.convert_mapping[type]
        except KeyError:
            raise TypeError(
                f"{type} can not be converted.\n"
                f"Add a conversion behavior using the add_converter method."
            )

    def add_converter(self, type_, func):
        """
        Adds converter to internal mapping.
        Converter callback must take one positional argument.
        :param type_:
        :param func:
        :return:
        """
        self.convert_mapping.update({type_: func})
