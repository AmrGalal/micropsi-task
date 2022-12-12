from minimum_binary_search.minimum_binary_search import BinarySearchMinimum

class TestMinimumBS:

    def test_valid_array_with_odd_size(self):
        array = [10,8,7,4,5,6,9]
        handler = BinarySearchMinimum(array)
        minimum = handler.get_minimum()
        assert minimum == 4
    
    def test_valid_array_with_even_size(self):
        array = [10,8,7,4,5,6]
        handler = BinarySearchMinimum(array)
        minimum = handler.get_minimum()
        assert minimum == 4

    def test_valid_array_with_negatives(self):
        array = [-1,-2,-3,-4,1,2,5]
        handler = BinarySearchMinimum(array)
        minimum = handler.get_minimum()
        assert minimum == -4

    def test_with_alphabets(self):
        array = ['g', 'e', 'z']
        handler = BinarySearchMinimum(array)
        minimum = handler.get_minimum()
        assert minimum == 'e'