#!/usr/bin/env python3
'''Task 101-safely_get_value.
'''
from typing import Dict, TypeVar, Optional

T = TypeVar('T')
U = TypeVar('U')

def safely_get_value(dct: Dict[str, T], key: str, default: Optional[U] = None) -> Optional[T]:
    if key in dct:
        return dct[key]
    else:
        return default
