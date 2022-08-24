# XML
import xml.dom.minidom
import SystemDependency as sys_dep

xml_path = sys_dep.get_xml_path()
domtree = xml.dom.minidom.parse(str(xml_path))

qrala = domtree.documentElement


def get(some_string: str) -> str:
    tag_name = qrala.getElementsByTagName(some_string)
    return tag_name[1].firstChild.data

# TODO: obsolete
class XML:
    def __init__(self, xml_path: str):
        self.xml_path = xml_path
        self.domtree = xml.dom.minidom.parse(str(self.xml_path))
        self.qrala = self.domtree.documentElement

    def get(self, tag: str) -> str:
        tag_name = self.qrala.getElementsByTagName(tag)
        return tag_name[1].firstChild.data

    def set(self, some_string: str, some_value: str) -> None:
        tag_name = self.qrala.getElementsByTagName(some_string)
        tag_name[1].firstChild.data = some_value
        self.domtree.write(str(self.xml_path))

    def get_all(self) -> dict:
        # read XML
        tag_name = self.qrala.getElementsByTagName("*")
        return {tag_name[i].tagName: tag_name[i].firstChild.data for i in range(len(tag_name))}

    def set_all(self, some_dict: dict) -> None:
        for key in some_dict:
            tag_name = self.qrala.getElementsByTagName(key)
            tag_name[1].firstChild.data = some_dict[key]
        self.domtree.write(str(self.xml_path))

    def get_all_tags(self) -> list:
        # read XML
        tag_name = self.qrala.getElementsByTagName("*")
        return [tag_name[i].tagName for i in range(len(tag_name))]

    def get_all_values(self) -> list:
        # read XML
        tag_name = self.qrala.getElementsByTagName("*")
        return [tag_name[i].firstChild.data for i in range(len(tag_name))]
