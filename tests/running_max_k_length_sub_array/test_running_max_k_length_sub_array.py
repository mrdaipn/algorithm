from problems.running_max_k_length_sub_array.running_max_k_length_sub_array import RuningMaxKLengthSubArray


class TestRunningMaxKLengthSubArray:

    def test_running_max_2_length_sub_array_10_8_5_returns_10_8(self):
        runing_max_sub_array = RuningMaxKLengthSubArray(array=[10, 8, 5], k=2)
        assert [10, 8] == runing_max_sub_array.get_running_max_array()

    def test_running_max_1_length_sub_array_10_8_5_return_10_8_5(self):
        runing_max_sub_array = RuningMaxKLengthSubArray(array=[10, 8, 5], k=1)
        assert [10, 8, 5] == runing_max_sub_array.get_running_max_array()

    def test_running_max_with_empty_array_should_return_empty_array(self):
        runing_max_sub_array = RuningMaxKLengthSubArray(array=[], k=2)
        assert [] ==  runing_max_sub_array.get_running_max_array()
        
