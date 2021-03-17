import sphobjinv as soi


def get_inventory(autorefs, project="project", version="0.0.0"):
    inv = soi.Inventory()
    inv.project = project
    inv.version = version

    for anchor, url in autorefs._url_map.items():
        url = url.replace(anchor, "$")
        o = soi.DataObjStr(name=anchor, domain="py", uri=url, role="obj", priority="1", dispname="-")
        inv.objects.append(o)

    df = inv.data_file()
    return df
    #return soi.compress(df)
    #soi.writebytes("objects_attrs_new.inv", dfc) 