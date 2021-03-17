"""Tests for the inventory module."""

from io import BytesIO
from os.path import join
from pathlib import Path

import pytest

from mkdocstrings.inventory import get_inventory

try:
    from sphinx.util.inventory import InventoryFile
except ImportError:
    InventoryFile = None  # type: ignore

MKDOCSTRINGS_OBJECTS_INV = Path("site/objects.inv")


# https://github.com/bskinn/sphobjinv/blob/260a96cd4eaa7d5cdd8e12f03ae7376243841fa6/conftest.py#L163-L177
@pytest.mark.skipif(InventoryFile is None, reason="Sphinx is not installed")
@pytest.mark.parametrize(
    "anchors_urls",
    [
        {},
        {"object_path": "page_url"},
        {"object_path": "page_url#object_path"},
        {"object_path": "page_url#other_anchor"},
    ],
)
def test_sphinx_load_inventory_file(anchors_urls):
    """Perform the 'live' inventory load test."""
    buffer = BytesIO(get_inventory(anchors_urls))
    InventoryFile.load(buffer, "", join)


@pytest.mark.skipif(not MKDOCSTRINGS_OBJECTS_INV.exists(), reason="site/objects.inv does not exist")
def test_sphinx_load_mkdocstrings_inventory_file():
    """Perform the 'live' inventory load test on mkdocstrings own inventory."""
    with MKDOCSTRINGS_OBJECTS_INV.open("rb") as fp:
        InventoryFile.load(fp, "", join)
