import xml.etree.ElementTree as ET
import requests

WORKDRIVE_ACCESS_TOKEN = "<YOUR_ACCESS_TOKEN>"  # Replace with your WorkDrive OAuth token
WORKDRIVE_FILE_ID = "<YOUR_FILE_ID>"           # Replace with the ID of your XML file in WorkDrive

def clean_xml_content(xml_content):
    """
    Removes non-printable characters from the XML content.
    """
    import re
    # Remove non-XML compatible characters
    cleaned_content = re.sub(r'[^\x09\x0A\x0D\x20-\x7F]', '', xml_content)
    #print("content", cleaned_content)
    return cleaned_content


def handler(request, context=None):
    """
    Fetch the XML file from link and parse employee data.
    """
    # Step 1: Fetch XML file from Zoho WorkDrive
    workdrive_url = f"https://scsanctions.un.org/resources/xml/en/consolidated.xml"

    try:
        response = requests.get(workdrive_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print(response.content.decode('utf-8').splitlines()[4])
        #print('Line before cleanup ^^^')
        response_content = response.content.decode('utf-8')
        cleaned_content = clean_xml_content(response_content)
        print(response.content.decode('utf-8').splitlines()[4])
        #print('Line after cleanup ^^^')

        # Step 2: Parse the XML file
        individuals = []
        tree = ET.ElementTree(ET.fromstring(cleaned_content))
        root = tree.getroot()

        for individual in root.findall('.//INDIVIDUAL'):
            alias_names = [alias.text.strip() for alias in individual.findall('.//ALIAS_NAME') if alias.text]
            #print(alias_name)
            #last_name = individual.find('LastName').text
            if alias_names:  
                individuals.append({'alias_names': alias_names})
                
        
        if not individuals:
            return {"status": "error", "message": "No individuals found with ALIAS_NAME in XML."}


        # Step 3: Return the parsed data
        return {
            "status": "success",
            "individuals": individuals
        }
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": f"Failed to fetch XML: {str(e)}"}
    except ET.ParseError as e:
        return {"status": "error", "message": f"Failed to parse XML: {str(e)}"}
