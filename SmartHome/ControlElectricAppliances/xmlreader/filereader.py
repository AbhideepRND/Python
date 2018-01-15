from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import re
import os
from ControlElectricAppliances.xmlreader.xmlstructure import Module, Pin, Channel


class ReadSaxElement(ContentHandler):
    def __init__(self):
        self.module = {}
        self.currentId = None
        self.currentElement = ''
        self._charBuffer = []
        self.attrs = None;

    def startElement(self, name, attrs):
        self.attrs = attrs
        if ("module" == name):
            currentModule = Module(attrs.get('name'), attrs.get('ip'), attrs.get('role').split(','))
            currentId = attrs.get('name')
            self.module[currentId] = currentModule
            self.currentId = currentId
            self.currentModule = currentModule

        if ("channel" == name):
            self.currentElement = name
            self.currentModule.channel = Channel(None, None)

        if ("pin" == name):
            pin =  Pin(attrs.get('no'))
            self.currentModule.setPin(pin)
            self.currentElement = name

    def endElement(self, tag):
        if 'channel' == tag == self.currentElement:
            self.currentModule.channel.inbound = self._charBuffer[0]
            self.currentModule.channel.outbound = self._charBuffer[1]
            self._charBuffer = [];
        if 'pin' == tag == self.currentElement:
            pin = self.currentModule.pin[self.attrs.get('no')]
            pin.description = ''.join(self._charBuffer).strip()
            self._charBuffer = [];

    def characters(self, content):
        matched = re.match(r'(\n|\t){1,}', content, re.I | re.M)
        if matched == None:
            self._charBuffer.append(content)

    def loadXmlConfig(self, filename):
        #filename ="module_config.xml"
        projectPath = os.path.abspath(os.path.dirname('module_Config.xml'))

        filepath = os.path.join(projectPath[0:projectPath.find('SmartHome')], 'SmartHome/data/' + filename)
        saxReader = ReadSaxElement()
        saxparser = make_parser()
        saxparser.setContentHandler(saxReader)
        datasource = open(filepath, 'r')
        saxparser.parse(datasource)
        return saxReader.module
#data = ReadSaxElement.loadXmlConfig(object, "module_config.xml")

#for i,j in data.items():
#    for k,j in j.pin.items():
#        print(j.description)