import os
from google_images_download import google_images_download
from PIL import Image

class imageGetter:
    def __init__(self, project_directory):
        self.download_directory = project_directory + "/images"

    def get_image(self, keyword):
        arguments = {"keywords": keyword, "limit": 1, "print_urls": True,
                     "no_directory": True, "size": "medium", "type": "clipart",
                     "output_directory": self.download_directory}
        # search and download image from Google images
        path, errors = google_images_download.googleimagesdownload().download(arguments)
        # open and display the image file on screen
        im = Image.open(path[keyword][0])
        im.show()
        # rename image file
        new_path = self.download_directory + "/" + keyword + ".jpg"
        os.rename(path[keyword][0], new_path)
        return new_path


if __name__ == "__main__":
    project_directory = os.path.abspath(os.getcwd())
    getter = imageGetter(project_directory)
    keyword = input("Enter a word: ")
    getter.get_image(keyword)

