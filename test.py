import json

from zbMcLib.mccn.version import *
print(json.dumps(getVersions(), ensure_ascii=False, indent=4))