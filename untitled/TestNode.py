from xml.etree.ElementTree import Element, tostring, SubElement
from basics import init, Node, Equipments

class TestNode(object):

    def __init__(self, testinfo):
        self.root = Element(self.rootTag)
        self.root.append(type("TestDate", (Node,), {"__init__": init})(testinfo.TestDate, None).__ToNode__())
        # append Personnel

        self.root.append(testinfo.Personnel.__ToNode__())

        # append equipmentused

        self.root.append(Equipments[self.Equip].__ToNode__())

        self.root.append(
            type("AmbientAirTemperature", (Node,), {"__init__": init})(testinfo.AirTemperature, None).__ToNode__())
        self.root.append(
            type("DeckSurfaceTemperature", (Node,), {"__init__": init})(testinfo.DeckSurfaceTemperature, None).__ToNode__())
        self.root.append(
            type("TestSite", (Node,), {"__init__": init})(testinfo.TestSite, None).__ToNode__())

    def __ToNode__(self):

        return self.root