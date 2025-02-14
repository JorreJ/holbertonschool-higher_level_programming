#!/usr/bin/python3
"""
Module for serializing and deserializing a dictionary to/from an XML file.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary into XML format and saves it to a file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the file where the XML data will be saved.

    Returns:
        None
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    with open(filename, 'wb') as f:
        tree.write(f, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserializes an XML file back into a dictionary.

    Args:
        filename (str): The name of the XML file to read.

    Returns:
        dict: A dictionary containing the parsed XML data.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text

    return dictionary


if __name__ == "__main__":
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }
    xml_file = "data.xml"

    # Serialize the dictionary to XML
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    # Deserialize the XML file back into a dictionary
    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)
