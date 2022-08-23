import xml.etree.ElementTree as ET


class XML_Parser:
    def __init__(self, xml_file):
        self.xml_file = xml_file
        self.tree = ET.parse(self.xml_file)
        self.root = self.tree.getroot()

    def get_tag_text(self, tag_name) -> str:
        return self.root.findtext(tag_name)

    def get_tag_list(self, tag_name) -> list:
        return self.root.findall(tag_name)

    def set_tag_text(self, tag_name, new_tag_text) -> None:
        self.root.find(tag_name).text = new_tag_text
        self.tree.write(self.xml_file)

    def create_tag(self, tag_name, tag_text) -> None:
        new_tag = ET.SubElement(self.root, tag_name)
        new_tag.text = tag_text
        self.tree.write(self.xml_file)
