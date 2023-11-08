import xml.etree.ElementTree as ET
import json

def parse_xml(xml_string):
    root = ET.fromstring(xml_string)
    data = {
        "title": root.find("GameName").text,
        "attempt_count": int(root.find("AttemptCount").text),
        "start_delay": str(root.find("Offset").text),
        "splits": []
    }
    segments = root.find("Segments")
    for segment in segments.findall("Segment"):
        split_data = {
            "title": segment.find("Name").text,
            "time": "0.000000",
            "best_time": "0.000000",
            "best_segment": "0.000000"
        }
        data["splits"].append(split_data)
    data["theme"] = "live-split"
    data["width"] = 256
    data["height"] = 512
    return json.dumps(data)
