from typing import Dict
from os.path import join, abspath, dirname, exists, expanduser
from credentials import get_credentials

FILENAME = join(abspath(expanduser("~")), ".ERS_credentials")

def get_ERS_credentials(filename: str = FILENAME) -> Dict[str, str]:
    if filename is None or not exists(filename):
        filename = FILENAME

    credentials = get_credentials(
        filename=filename,
        displayed=["username", "header"],
        hidden=["password"],
        prompt="credentials for EROS Registration System https://ers.cr.usgs.gov/register"
    )

    return credentials
