import os
from uuid import uuid4

def uuid_upload_to(instance, filename):
    uuid_name = uuid4().hex
    ext =  os.path.splitext(filename)[-1].lower()
    uuid_name[:2]
    return '/'.join([
        uuid_name[:2],
        uuid_name[4:] + ext,
        ])