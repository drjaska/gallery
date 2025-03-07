from copy import deepcopy

import pytest

from Imagegallery import Filetree, Imagegallery

from ..data.example_gallery import example_gallery


@pytest.fixture
def test_library_toml():
    return deepcopy(example_gallery)

@pytest.fixture
def filetree():
    tree = Filetree()
    tree.add_dir("path").add_dir("to").add_image("image1.jpg", "jpg")
    return tree

@pytest.fixture()
def imagegallery(test_library_toml, filetree):
    return Imagegallery.from_vars(test_library_toml, filetree)

def test_with_empty_returns_empty():
    imagegallery = Imagegallery()
    imagegallery.flag_missing()
    assert imagegallery.metadata == {}

def test_with_empty_filetree_all_missing(test_library_toml):

    imagegallery = Imagegallery.from_vars(test_library_toml, Filetree())
    imagegallery.flag_missing()

    assert "missing" in imagegallery.metadata["path/to/image1.jpg"]

def test_not_all_missing(imagegallery):
    imagegallery.flag_missing()

    assert not "missing" in imagegallery.metadata["path/to/image1.jpg"]

def test_original_gallery_is_intact(imagegallery, test_library_toml):
    imagegallery.flag_missing()

    assert "missing" not in test_library_toml["path/to/image1.jpg"]

def test_original_metadata_is_intact(imagegallery):
    original_metadata = imagegallery.metadata
    imagegallery.flag_missing()

    assert "missing" not in original_metadata["path/to/image1.jpg"]
