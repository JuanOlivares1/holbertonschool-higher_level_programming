#!/usr/bin/python3
"""Module
"""


class MyInt(int):
    """class MyInt - """
    def __eq__(self, obj):
        """function - validates equality

        Args:
            obj (obj): object to compare

        Returns: True if obj and self are differents. False otherwise
        """
        return super().__ne__(obj)

    def __ne__(self, obj):
        """function - validates inequality

        Args:
            obj (obj): object to compare

        Returns: False if obj and self are equal. True otherwise
        """
        return super().__eq__(obj)
