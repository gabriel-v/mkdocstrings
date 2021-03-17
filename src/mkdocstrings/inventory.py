"""Module responsible for generating the objects inventory."""

# Credits to Brian Skinn
# and the sphobjinv project:
# https://github.com/bskinn/sphobjinv

import zlib

HEADER = """# Sphinx inventory version 2
# Project: {project}
# Version: {version}
# The remainder of this file is compressed using zlib.
"""


def get_inventory(anchors_urls, project="project", version="0.0.0", compress=True) -> bytes:
    """Generate an objects inventory.

    Arguments:
        anchors_urls: A dictionary with objects identifier as keys and their URLs as values.
        project: The project name.
        version: The project version.
        compress: Whether to compress the data using zlib.

    Returns:
        The inventory as bytes.
    """
    header = HEADER.format(project=project, version=version).encode("utf8")

    lines = []
    for anchor, url in anchors_urls.items():
        anchor_length = len(anchor)
        if url[-anchor_length - 1 :] == "#" + anchor:
            url = url[:-anchor_length] + "$"
        lines.append(f"{anchor} py:obj 1 {url} -".encode("utf8"))

    data = b"\n".join(lines)
    if compress:
        data = zlib.compress(data, 9)
    return header + data
