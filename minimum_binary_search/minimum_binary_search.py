from typing import List

class BinarySearchMinimum:
    """
        Class to find minimum element in array when it's strictly decreasing
        then strictly increasing

        example:
        10 8 7 4 5 6 8 11

        answer here is 4
    """
    def __init__(self, elementsArray: List) -> None:
        self.elementsArray = elementsArray
        self.arraySize = len(self.elementsArray)
        self.isOddSize = self.arraySize % 2

    def __is_element_the_minimum__(self, index) -> bool:
        """
            Check if the element at an index is truly the minimum element in the array
            Simply if the element has neighbors and smaller than both neighbors
        """
        return index > 0 and index < (self.arraySize-1) and\
             self.elementsArray[index] < self.elementsArray[index+1] and\
                 self.elementsArray[index] < self.elementsArray[index-1]

    def __is_element_before_minimum__(self, index) -> bool:
        """
            Check the element at a specific index and check its right neighbor to see
            if the minimum element is at its right

            The element is before the minimum element if we have elements at its right and
            right neighbor is less than it
        """
        return index <= (self.arraySize-2) and self.elementsArray[index] > self.elementsArray[index+1]

    def get_minimum(self) -> int:
        startIndex, endIndex = 0, self.arraySize - 1
        increment = 1 if not self.isOddSize else 0

        while startIndex < endIndex:
            mid = int((endIndex - startIndex + increment)/2)
            if self.__is_element_the_minimum__(mid):
                return self.elementsArray[mid]
            elif self.__is_element_before_minimum__(mid):
                startIndex = mid
            else:
                endIndex = mid - 1
