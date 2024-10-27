from PIL import Image
import os

class ImageHeightVsWidth:   
    input_dir = '/Users/tapansidhwani/Downloads/PythonDigHist'
    categories = ['double', 'RepresentativeImages']

    @staticmethod
    def checkOrientation(input_dir):
        orientations = {}

        for category_idx, category in enumerate(ImageHeightVsWidth.categories):
            print(category_idx, category)
            category_path = os.path.join(input_dir, category)
            for file in os.listdir(category_path):
                # Skip hidden files and .DS_Store
                if file.startswith('.') or file == '.DS_Store':
                    continue

                img_path = os.path.join(category_path, file)
                if os.path.isfile(img_path):  # Check if it's a file, not a directory
                    try:
                        with Image.open(img_path) as img:
                            width, height = img.size

                        if height > width:
                            orientation = 'Portrait'
                        elif width > height:
                            orientation = 'Landscape'
                        else:
                            orientation = 'Square'

                        # Store the details in the orientations dictionary
                        orientations[file] = {'width': width, 'height': height, 'orientation': orientation}

                        print(f'{file}: {width}x{height} - {orientation}')
                    except Exception as e:
                        print(f"Could not process {file}: {e}")

        return orientations

# Run the checkOrientation method
image_orientations = ImageHeightVsWidth.checkOrientation(ImageHeightVsWidth.input_dir)
