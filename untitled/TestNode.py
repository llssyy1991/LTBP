from xml.etree.ElementTree import Element, tostring, SubElement
from basics import init, Node, Equipments

class TestNode(object):

    def __init__(self, testinfo):
        self.root = Element(self.rootTag)
        if self.rootTag == "NDE001-TestInfo":
            self.root.append(type("TestDate", (Node,), {"__init__": init})(testinfo.TestDate, None).__ToNode__())
            self.root.append(testinfo.Personnel.__ToNode__())      # append Personnel
            self.root.append(Equipments[self.Equip].__ToNode__())  # append equipmentused
            self.appendNode("AmbientAirTemperature" , testinfo.AirTemperature        )
            self.appendNode("DeckSurfaceTemperature", testinfo.DeckSurfaceTemperature)
            self.appendNode("TestSite"              , testinfo.TestSite              )

        if self.rootTag == "NDE007-TestInfo":
            self.root.append(testinfo.Personnel.__ToNode__())  # append Personnel
            self.root.append(type("TestDate", (Node,), {"__init__": init})(testinfo.TestDate, None).__ToNode__())
            self.appendNode("AmbientAirTemperature"    , testinfo.AirTemperature           )
            self.appendNode("DeckSurfaceTemperature"   , testinfo.DeckSurfaceTemperature   )
            self.root.append(Equipments[self.Equip].__ToNode__())  # append equipmentused
            self.appendNode("BridgeDeckThickness"      , testinfo.BridgeDeckThickness      ) ############
            self.appendNode("SourceSensorSpacing"      , str(133.35 * 0.00328084)          ) ############
            self.appendNode("SensorOneSensorTwoSpacing", str(133.35 * 0.00328084)          ) ############
            self.appendNode("SamplePerScan"            , str(512)                          )
            self.appendNode("TestSite"                 , testinfo.TestSite                 )

        if self.rootTag == "NDE004-TestInfo":
            self.root.append(testinfo.Personnel.__ToNode__())  # append Personnel
            self.root.append(type("TestDate", (Node,), {"__init__": init})(testinfo.TestDate, None).__ToNode__())
            self.appendNode("AmbientAirTemperature", testinfo.AirTemperature)
            self.appendNode("DeckSurfaceTemperature", testinfo.DeckSurfaceTemperature)
            self.root.append(Equipments[self.Equip].__ToNode__())  # append equipmentused
            # self.appendNode("OverlayMaterial", testinfo.OverlayMaterial)  ############
            # self.appendNode("OverlayThickness", testinfo.OverlayThickness)  ############
            self.appendNode("BridgeDeckThickness", testinfo.BridgeDeckThickness)  ############
            # self.appendNode("SourceType", testinfo.SourceType)  ############
            # self.appendNode("SensorType", testinfo.SensorType)
            self.appendNode("SamplePerScan", str(512))
            self.appendNode("TestSite", testinfo.TestSite)

    def appendNode(self, rootname, element):
        self.root.append(
            type(rootname, (Node, ), {"__init__": init})(element, None).__ToNode__())

    def __ToNode__(self):

        return self.root