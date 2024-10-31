# add progress bar
# add parallel processing

import os
import pandas as pd
import easyocr

# Initialize the EasyOCR reader
reader = easyocr.Reader(['en'])  # You can specify other languages if needed

# Specify the folder containing images
image_folder = 'Hiring'  # Update this path

# Initialize a list to store results
data = []

# Loop through all files in the folder
for filename in os.listdir(image_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg')):  # Add other formats if needed
        image_path = os.path.join(image_folder, filename)
        # Read text from the image
        results = reader.readtext(image_path)

        # Combine extracted text into a single string
        extracted_text = ' '.join([result[1] for result in results])

        # Append to data list
        data.append({'image_name': filename, 'extracted_text': extracted_text})

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a excel file
df.to_excel('extracted_text.xlsx', index=False)
print('Extraction completed and saved to extracted_text.xlsx')
