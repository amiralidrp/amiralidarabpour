import requests
import re
import sys
from pathlib import Path


if __name__=='__main__':


    subject=sys.argv[1]
    s=requests.request('GET', 'https://en.wikipedia.org/wiki/' + subject)

    kn=re.findall('<p>(.*)</p>', str(s.text.encode()))
    print(kn)

    x=Path(subject+'html')
    x.write_text(str(s.text.encode()))

