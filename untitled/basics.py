from xml.etree.ElementTree import Element, tostring, SubElement


class Node(object):

    def __init__(self, identifier, data):
        self.data = data

    def __ToNode__(self):

        root = Element(self.__class__.__name__)

        # http://stackoverflow.com/questions/25231989/how-to-check-if-a-variable-is-a-dictionary-in-python

        if isinstance(self.data, str):

            root.text = self.data

            return root

        if isinstance(self.data, list):

            for node in self.data:

                root.append(node.__ToNode__())

            return root

        if isinstance(self.data, dict):

            for entry in self.list:

                sub = SubElement(root, entry)
                if self.data[entry] != "":
                    sub.text = self.data[entry]

            return root


# interface
class BridgeInformation(Node):

    identifier = "BridgeInformation"

    def __init__(self, BridgeInfo):

        self.data = dict()
        self.data["ltbpcmn:StructureID"]    = BridgeInfo.ID
        self.data["ltbpcmn:LTBPBridgeName"] = BridgeInfo.BridgeName
        self.data["ltbpcmn:State"]          = BridgeInfo.State
        self.list                           = ["ltbpcmn:StructureID", "ltbpcmn:LTBPBridgeName", "ltbpcmn:State"]
        # self.data["ltbpcmn:ProtocolName"] = ProtocolName


# interface
class Inspectors(Node):

    def __init__(self, FirstName, SecondName, Company):

        self.data = dict()

        self.data['ltbpcmn:firstName'] = FirstName
        self.data['ltbpcmn:surname'] = SecondName
        self.data['ltbpcmn:Company'] = Company
        self.list = ['ltbpcmn:firstName', 'ltbpcmn:surname', 'ltbpcmn:Company']

#interface / view
class Personnel(Node):

    def __init__(self, inspectors):

        self.data = inspectors


#interface / view
class EquipmentUsed(Node):

    def __init__(self, Name, Model, Manufacturer):

        self.data = dict()

        self.data["ltbpcmn:Name"] = Name
        self.data["ltbpcmn:Model"] = Model
        self.data["ltbpcmn:Manufacturer"] = Manufacturer

        self.list = ["ltbpcmn:Name", "ltbpcmn:Model", "ltbpcmn:Manufacturer"]

# model
class TestInfo(object):

    def __init__(self, TestDate, personnel, AirTemperature, DeckSurfaceTemperature, BridgeDeckThickness, TestSite):

        # TestDate  : data collection date
        # personnel : person who collected the data
        # AirTemperature
        # DeckSurfaceTemperature
        # TestSite

        self.TestDate               = str(TestDate)
        self.Personnel              = personnel
        self.AirTemperature         = str(AirTemperature)
        self.DeckSurfaceTemperature = str(DeckSurfaceTemperature)
        self.BridgeDeckThickness    = str(BridgeDeckThickness)
        self.TestSite               = str(TestSite)

# model
class BridgeInfo(object):

    def __init__(self, ID, BridgeName, State):

        self.ID = ID
        self.BridgeName = BridgeName
        self.State = State


def init(self, data, list = None):

    self.data = data
    if list != None:
        self.list = list



# class NDE001Info:
#
#     def __init__(self, BridgeInfo, ):
#         pass


Equipments      = dict()       # preset equipment for
inspectors      = list()
Bridge          = None
operationInfo   = None


Equipments["ER"]  = EquipmentUsed("Wenner Probe"     , "Resipod Resistivity Meter"   , "Proceq")
Equipments["IE"]  = EquipmentUsed("Infratek Cane"    , ""                            , "Infratek Solution")
Equipments["USW"]  = EquipmentUsed("Infratek Cane"    , ""                            , "Infratek Solution")

if __name__ == "__main__":

    # test = BridgeInfomation("1806", "test", "10", "NDE001")
    # test = type("testing", (Node,), {"__init__" : __init}) ("hello")
    # print tostring(test.__ToNode__())

    print tostring(Equipments["ER"].__ToNode__())


