# XML
import xml.dom.minidom
import SystemDependency as sys_dep
rootPath = sys_dep.getRootPath()
print(rootPath)

domtree = xml.dom.minidom.parse(
    rootPath + '/src/Qrala_Config.xml')

qrala = domtree.documentElement


def get(some_string):
    # read XML
    tag_name = qrala.getElementsByTagName(some_string)
    return tag_name[1].firstChild.data


