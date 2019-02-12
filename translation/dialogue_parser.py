from xml.dom import minidom
import json


def parse_dual_lang_xml_file(filename):
    result_string_pairs = []
    xml_doc = minidom.parse(filename)
    units = xml_doc.getElementsByTagName('unit')
    i = 0
    for unit in units:
        en_string = unit.getElementsByTagName('source')[0].childNodes[0].data
        ru_string = unit.getElementsByTagName('target')[0].childNodes[0].data
        string_pair = en_string, ru_string, i
        result_string_pairs.append(string_pair)
        i += 1
    return result_string_pairs


def parse_dual_lang_json_file(filename):
    result_string_pairs = []
    with open(filename, encoding="utf-8") as file:
        units = json.load(file)
    i = 0
    for unit in units:
        en_text = unit["source"]["text"]
        ru_text = unit["target"]["text"]
        string_pair = en_text, ru_text, i
        result_string_pairs.append(string_pair)
        i += 1
    return result_string_pairs
