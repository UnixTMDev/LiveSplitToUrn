import sys
from parser import parse_xml

if len(sys.argv) < 2:
    print("Usage: python <script's filename> input_file.lss [output file]")
    print("output file is optional. Will write to stdout if not provided.")
    print("Note: Does not currently save PBs and segment times.")
    print("Converts LiveScript splits file to a JSON file for use with Urn")
    print("https://github.com/paoloose/urn")
else:
    input_file = sys.argv[1]
    try:
        with open(input_file, 'r') as file:
            xml_data = file.read()
            json_data = parse_xml(xml_data)
            if len(sys.argv) < 3:
                print(json_data)
            else:
                try:
                    out_file = sys.argv[2]
                    with open(out_file, 'w') as f:
                        f.write(json_data)
                    print("Success! Remember that the file isn't prettyprinted.")
                except Exception as e:
                    print(f"Error in saving: {str(e)}")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")

