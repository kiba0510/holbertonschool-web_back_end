#!/usr/bin/env python3
"""Create a class BasicCache that inherits from
BaseCaching and is a caching system
"""
from BaseCaching import BaseCaching


class BasicCache(BaseCaching):
    """Basics of caching"""

    def put(self, key, item):
        """Add chaching to caching system"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get cache from caching system"""
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
