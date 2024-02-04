import os
import requests

# Setting up Output directory
workingDirectory = os.getcwd()
results_dir = 'Output_Images'
path = os.path.join(workingDirectory, results_dir)

# Creating output directory
try:
    if not os.path.exists(path):
        os.makedirs(path)
except:
    print(f"\nError in Creating Output directory\n")
    exit(0)


image_url = "https://epaper.munsifdaily.com/wp-content/uploads/2024/02/02/02_02_2024_m2_04.jpg"
output_filename = "Output_Images\downloaded_image.jpg"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

response = requests.get(image_url, headers=headers)

if response.status_code == 200:
    with open(output_filename, 'wb') as file:
        file.write(response.content)
    print(f"Image downloaded successfully as {output_filename}")
else:
    print(f"Failed to download image. Status code: {response.status_code}")
