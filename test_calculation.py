import pytest
import calculation

# def test_add_num_and_double():
#     cal = calculation.Cal()
#     assert cal.add_num_and_double(1, 1) == 4

class TestCal(object):

    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = calculation.Cal()

    def test_add_num_and_double(self, tmpdir):
        print(tmpdir)
        assert self.cal.add_num_and_double(1, 1) == 4




    # @classmethod
    # def teardown_class(cls):
    #     print('end')
    #     del cls.cal
    #
    # def setup_method(self, method):
    #     print('method={}'.format(method.__name__))
    #     # self.cal = calculation.Cal()
    #
    # def teardown_method(self, method):
    #     print('method={}'.format(method.__name__))
    #     # del self.cal
    #
    # def test_add_num_and_double(self):
    #     assert self.cal.add_num_and_double(1, 1) == 4
    #
    # @pytest.mark.skip(reason='skip!')
    # def test_add_num_and_double_raise(self):
    #     with pytest.raises(ValueError):
    #         self.cal.add_num_and_double('1', '1')

#     def setUp(self):
#         print('setup')
#         self.cal = calculation.Cal()
#
#     def tearDown(self):
#         print('clean up')
#         del self.cal
#
#     def test_add_num_and_double(self):
#         self.assertEqual(self.cal.add_num_and_double(1, 1),
#                          4)
#     def test_add_num_and_double_raise(self):
#         with self.assertRaises(ValueError):
#             self.cal.add_num_and_double('1', '1')



# if __name__ == '__main__':
#     unittest.main()
