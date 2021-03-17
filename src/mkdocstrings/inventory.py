import zlib


HEADER = """# Sphinx inventory version 2
# Project: {project}
# Version: {version}
# The remainder of this file is compressed using zlib.
"""


def get_inventory(autorefs, project="project", version="0.0.0", compress=False):
    header = HEADER.format(project=project, version=version).encode("utf8")

    lines = []
    for anchor, url in autorefs._url_map.items():
        url = url.replace(anchor, "$")
        lines.append(f"{anchor} py:obj 1 {url} -".encode("utf8"))

    data = b"\n".join(lines)
    if compress:
        data = zlib.compress(data, 9)
    return header + data
