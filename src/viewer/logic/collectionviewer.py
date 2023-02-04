import gi
from Imagegallery import Image

gi.require_version("Gtk", "3.0")
from gi.repository import GObject


class CollectionViewer(GObject.Object):

    images: [Image] = []
    current_index = 0

    def has_images(self):
        return len(self.images) > 0

    def add_images(self, images):
        self.images = images

    def empty(self):
        self.images = []

    def count(self):
        return len(self.images)

    def current_image(self):
        return self.images[self.current_index]

    @GObject.Property(type=str)
    def current_image_path(self):
        if self.has_images():
            return self.current_image().path_as_bytes()
        return ""

    def go_next(self):
        if self.current_index < len(self.images) - 1:
            self.current_index = self.current_index + 1
        return self

    def go_prev(self):
        if self.current_index > 0:
            self.current_index = self.current_index - 1
        return self

    def load_collection(self, collection):
        self.empty()
        self.add_images(collection.images)
