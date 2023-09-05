import requests
import os
import re
from urllib.parse import urlparse



def save_file_from_url(url, save_dir):
    try:
        response = requests.get(url)
        original_filename = False

        if response.status_code == 200:
            # Try to get the original filename and extension from the Content-Disposition header
            content_disposition = response.headers.get('Content-Disposition')
            if content_disposition:
                # Extract the filename from the header using a regular expression
                filename_match = re.search(r'filename="(.+)"', content_disposition)
                if filename_match:
                    original_filename = filename_match.group(1)
                else:
                    # If the header doesn't provide a filename, parse it from the URL
                    parsed_url = urlparse(url)
                    original_filename = os.path.basename(parsed_url.path)
            else:
                # If the Content-Disposition header is not present, parse the filename from the URL
                parsed_url = urlparse(url)
                original_filename = os.path.basename(parsed_url.path)

            # Combine the original filename with the save directory
            save_path = os.path.join(save_dir, original_filename)

            # Save the file to the specified location
            with open(save_path, 'wb') as file:
                file.write(response.content)

            print(f"File saved as {save_path}")

            return original_filename

        else:
            print(f"Failed to download file. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return False
