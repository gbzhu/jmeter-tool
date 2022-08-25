import xml.etree.ElementTree as et
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
cloud_section = config['cloud']
local_file_path = config['local']['local_jmeter_path']
tmp = str(local_file_path).split('.')
cloud_path = tmp[0] + "-cloud." + tmp[1]

tree = et.parse(local_file_path)
root = tree.getroot()

for key in cloud_section.keys():
    xpath = "./hashTree/TestPlan/elementProp/collectionProp/elementProp[@name='" + key + "']"
    elementProp = root.find(xpath)
    stringProp = elementProp[1]
    stringProp.text = cloud_section[key]
tree.write(cloud_path)
