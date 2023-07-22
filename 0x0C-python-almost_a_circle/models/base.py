#!/usr/bin/python3
"""
This module defines a class Base
"""
import json
import csv
from os import path


class Base():
    """ A base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for base class

        Args:
            id (int): Unique ID for the object
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Get the the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list[dict]): a list of dictionaries

        Returns:
            str: JSON strig representation of @list_dictionaries
        """
        if type(list_dictionaries) is not None and not list:
            raise TypeError()

        if list_dictionaries:
            for item in list_dictionaries:
                if type(item) is not dict:
                    raise TypeError()

            return json.dumps(list_dictionaries)

        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file

        Args:
            list_objs: A list of instances who inherits of Base
        """
        list_dictionaries = []
        filename = cls.__name__ + ".json"

        if list_objs is not None:
            if len(list_objs) != 0:
                for item in list_objs:
                    list_dictionaries.append(item.to_dictionary())

        with open(filename, mode="w") as file:
            file.write(Base.to_json_string(list_dictionaries))

        if list_objs is None or list_objs == []:
            return "[]"

    @staticmethod
    def from_json_string(json_string):
        """
        Gets the list of the JSON string representation json_string

        Args:
            json_string: A string representing a list of dictionaries.

        Returns:
            The list of the JSON string representation json_string
        """
        if type(json_string) is not None and not str:
            raise TypeError()

        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance with all attributes already set

        Args:
            dictionary (kwargs): Values to be used to set all attributes

        Returns:
           object: an instance of a class
        """
        if cls.__name__ == "Rectangle":
            obj = cls(4, 3)
        elif cls.__name__ == "Square":
            obj = cls(4)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """
        Gets list of instances

        Returns:
            list: list of instances
        """
        list_instances = []
        filename = cls.__name__ + ".json"
        if path.isfile(filename):
            with open(filename, mode="r", encoding="utf-8") as file:
                list_dict = cls.from_json_string(file.read())
                for item in list_dict:
                    list_instances.append(cls.create(**item))
        return list_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize CSV

        Args:
            list_objs: list of instances of Base class
        """
        if type(list_objs) is not None and not list:
            raise TypeError()

        filename = cls.__name__ + ".csv"

        if list_objs:
            with open(filename, mode="w", encoding="utf-8") as file:
                writer = csv.writer(file)

                for item in list_objs:
                    if not isinstance(item, cls):
                        raise TypeError()

                    li = []
                    li.append(item.id)

                    if type(item).__name__ == "Rectangle":
                        li.append(item.width)
                        li.append(item.height)
                    elif type(item).__name__ == "Square":
                        li.append(item.size)

                    li.append(item.x)
                    li.append(item.y)
                    writer.writerow(li)

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize CSV file

        Return:
            list:list of instances
        """
        filename = cls.__name__ + ".csv"
        list_instances = []

        if path.isfile(filename):
            with open(filename, mode="r", encoding="utf8") as file:
                reader = csv.reader(file)

                for row in reader:
                    d = {}
                    d["id"] = int(row[0])

                    if cls.__name__ == "Rectangle":
                        d["width"] = int(row[1])
                        d["height"] = int(row[2])
                        d["x"] = int(row[3])
                        d["y"] = int(row[4])
                    elif cls.__name__ == "Square":
                        d["size"] = int(row[1])
                        d["x"] = int(row[2])
                        d["y"] = int(row[3])

                    list_instances.append(cls.create(**d))
        return list_instances
