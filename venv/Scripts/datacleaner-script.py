#!"F:\4-2\Sessional\CSE 474 Pattern Recognition Sessional\Offline 1\1405119\venv\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'datacleaner==0.1.5','console_scripts','datacleaner'
__requires__ = 'datacleaner==0.1.5'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('datacleaner==0.1.5', 'console_scripts', 'datacleaner')()
    )
