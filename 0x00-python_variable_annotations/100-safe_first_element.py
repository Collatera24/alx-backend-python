#!/usr/bin/env python3
'''100-safe_first_element.
'''
from typing import List, Optional, Any


def safe_first_element(lst: List[Any]) -> Optional[Any]:
    if lst:
        return lst[0]
    else:
        return None
