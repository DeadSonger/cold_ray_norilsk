from functools import partial

from cold_ray_norilsk.src.game_model.utils.callback_object import callback_object


@callback_object
class Cls:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def sum(self) -> float:
        return self.a + self.b


def test_get_var_callback():
    test_obj = Cls(1, 1)
    num_calls = [0]

    def callback(arr):
        arr[0] += 1

    test_obj.add_get_callback('a', partial(callback, arr=num_calls))

    _ = test_obj.a

    assert num_calls[0] == 1


def test_set_var_callback():
    test_obj = Cls(1, 1)
    num_calls = [0]

    def callback(value, arr):
        arr[0] = value

    test_obj.add_set_callback('a', partial(callback, arr=num_calls))

    test_obj.a = 'str'

    assert num_calls[0] == 'str'


def test_get_pre_call_callback():
    test_obj = Cls(1, 1)
    num_calls = [0]

    def callback(*args, arr, **kwargs):
        arr[0] += 1

    test_obj.add_pre_call_callback('sum', partial(callback, arr=num_calls))

    test_obj.sum()

    assert num_calls[0] == 1


def test_get_post_call_callback():
    test_obj = Cls(1, 1)
    num_calls = [0]

    def callback(*args, arr, **kwargs):
        arr[0] += 1

    test_obj.add_post_call_callback('sum', partial(callback, arr=num_calls))

    test_obj.sum()

    assert num_calls[0] == 1


def test_get_post_and_pre_call_callback():
    test_obj = Cls(1, 1)
    num_calls = [0]

    def callback(*args, arr, **kwargs):
        arr[0] += 1

    test_obj.add_pre_call_callback('sum', partial(callback, arr=num_calls))
    test_obj.add_post_call_callback('sum', partial(callback, arr=num_calls))

    test_obj.sum()

    assert num_calls[0] == 2
