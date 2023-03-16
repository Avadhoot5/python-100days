import argparse
import requests

# Initializing the parser 
parser = argparse.ArgumentParser()

# Add command line arguments
parser.add_argument("URL", help = "URL of the file to download")
# parser.add_argument("Output", help = "by which name do you want to save your file")
parser.add_argument("-o", "--Output", help = "Name of the file", default = None)

# function to download a file using requests
def download_file(url, local_filename):
    if local_filename is None:
        local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename

# Parse the arguments
args = parser.parse_args()

# Using the arguments in your code
print(args.URL)
print(args.Output)
print(type(args.Output))
download_file(args.URL, args.Output)
