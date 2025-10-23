modul - plik z rozszerzeniem .py
paczka - folder (ktory zawiera modul __init__.py)


import modul
import paczka
import paczka.modul

modul.funkcja()
paczka.funkcja()
paczka.modul.funkcja()


from modul import funkcja, inna_funkcja

from modul import *

from modul import funkcja as alias

importy wzgledne (relatywne) i absolutne

from . import modul
from .. import modul

te relatywne dzialaja tylko traktujemy kod jako paczke

    myapp/
    ├── __init__.py
    ├── core/
    │   ├── __init__.py
    │   └── models.py
    └── utils/
        ├── __init__.py
        └── formatter.py
    
    # utils/formatter.py
    from ..core import models

    python -m myapp.utils.formatter


    jesli zrobisz tak:
    python myapp/utils/formatter.py
    
    ImportError: attempted relative import with no known parent package
