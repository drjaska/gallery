from Imagegallery.image import Image

class Collection:

    images: list[Image] = []

    def __init__(self, name, hash):
        self.name = name
        self.hash = hash
        self.images: list[Image] = []

    @classmethod
    def create_empty(cls):
        instance = cls("", "")
        return instance

    def is_empty(self):
        return len(self.images) == 0

    def add_images(self, images: list[Image]):
        self.images.extend(images)

    def add_image(self, image: Image):
        self.images.append(image)

    def size(self):
        return len(self.images)
