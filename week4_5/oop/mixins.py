import json
import xml.etree.ElementTree as ET

class Jsonable():
    data = {'type': None, 'dict': None}
    def to_json(self, indent = 4):
        self.data['dict'] = self.__dict__
        self.data['type'] = type(self).__name__
        return json.dumps(self.data, indent =4)
    @classmethod
    def from_json(self, json_string):
        return json.loads(json_string)


class Xmlable():
    data = {'type' : None, 'dict':None}
    
    def to_xml(self):
        r = ET.Element(type(self).__name__)
        self.data['dict'] = self.__dict__
        j = ET.SubElement(r, self.data['dict'])
              
        return ET.tostring(r)


class Automobile(Jsonable, Xmlable):
    def __init__(self, brand, model, hp):
        self.brand = brand
        self.model = model
        self.hp = hp
b = Automobile('BMW', 'e30', 535)
print(repr(b.__dict__))

x = b.to_xml()
print(x)

