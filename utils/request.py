import json
import urllib.request

from settings import environment

def download_mendeley_data():

  output_file = f'{environment.BASE_DIR}/data/public_data_en.csv'
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
  }

  request = urllib.request.Request(environment.URL_DATASET, headers=headers)
  try:
    with urllib.request.urlopen(request) as response, open(output_file, 'wb') as out_file:
      out_file.write(response.read())
    print(f"File successfully downloaded and saved as '{output_file}'.")
  except Exception as e:
    print(f"An error occurred: {e}")

def get_readability_metrics(text: str):
  url = 'http://localhost:8080/api/v1/metrix/_min/yyy?format=json'
  bytes_arr = bytearray(text, encoding='utf-8')
  req = urllib.request.Request(url, data=bytes_arr, headers={'content-type': 'text/plain'})
  try:
    response = urllib.request.urlopen(req)
    return json.loads(response.read().decode('utf8'))
  except Exception as e:
    print(e)
    return None