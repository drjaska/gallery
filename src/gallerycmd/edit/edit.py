from Imagegallery import Imagegallery
from filesystem_operations.librarysaver import save_library

from gallerycmd.parser import subparsers


def main(args):
    try:
        edit_image(args.filename,
                   args.title,
                   args.description,
                   args.tags)

    except(FileNotFoundError):
        print("No such image:", args.filename)
        exit(1)
    except(NeedsNamedArgument):
        print("You must provide either title, description or tags")
        exit(1)

def edit_image(filename, title=None, description=None, tags=None):
    gallery = Imagegallery.from_disk()

    if title == None and description == None and tags == None:
        raise NeedsNamedArgument

    gallery.edit(filename,
                 title=title,
                 description=description,
                 tags=tags)

    save_library(gallery.LibraryToml)

class NeedsNamedArgument(Exception):
    pass

parser = subparsers.add_parser('edit',
    description="Edit image metadata. Give field you want to modify as a parameter",
                               )
parser.add_argument("filename", help="Filename for image to be edited")
parser.add_argument("-t", "--title", help="Image title")
parser.add_argument("-d", "--description", help="Image description")
parser.add_argument("--tags", nargs="+", help="Tags describing this image, separated by space")
parser.set_defaults(func=main)
