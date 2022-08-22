from craiyon import Craiyon
from PIL import Image # pip install pillow
from io import BytesIO
import base64
import cv2
import numpy as np

class craiyon_image:
    """
    Class implements craiyon connected with an API to generate 9 images at a time.
    """
    def __init__(self, prompt, path):
        """
        Initializes the classes.
        :param prompt: text tokens to generate images. 
        :param path: the path to the repository that users what to save the image in.
        """
        self.prompt = prompt
        self.path = path


    def craiyon_API(self):
        """
        This function uses craiyon API to save and show images 
        return: void
        """
        # Instantiates the api wrapper
        generator = Craiyon() 
        # Generates 9 images by default and you cannot change that
        result = generator.generate(self.prompt) 
        # save image as in indicated path
        result.save_images(self.path) 
        images = result.images # A list containing image data as base64 encoded strings
        for i in images:
            # Use the PIL's Image object as per your needs
            image = Image.open(BytesIO(base64.decodebytes(i.encode("utf-8"))))
            # convert PIL format into numpy array
            image = np.array(image)
            print(type(image))
            cv2.imshow("image candidate", image)
            cv2.waitKey(0)                
            cv2.destroyAllWindows()

    def __call__(self):
        self.craiyon_API()

# Create a new object and execute.
new_task = craiyon_image(prompt = "a knight holding an apple", path = "/home/tianhao/CHI paper - survey engagement/craiyonAPITest")
new_task()
