from typing import ClassVar, List, Callable, Any


def _function_callback(func: Callable,
                       pre_call: List[Callable],
                       post_call: List[Callable]):
    def wrapper(*args, **kwargs):
        for pc in pre_call:
            pc(*args, **kwargs)
        ret = func(*args, **kwargs)
        for pc in post_call:
            pc(*args, **kwargs)
        return ret

    return wrapper


def callback_object(pcls: ClassVar):
    class WrapperOne(pcls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self._callback_map = {}

        def __add_callback(self, key: str, callback: Callable):
            callback_map = super().__getattribute__('_callback_map')
            if key not in callback_map:
                callback_map[key] = []
            callback_map[key].append(callback)

        def add_get_callback(self, attr: str, callback: Callable[[], Any]):
            self.__add_callback(f'{attr}__get', callback)

        def add_set_callback(self, attr: str, callback: Callable[[Any], None]):
            self.__add_callback(f'{attr}__set', callback)

        def add_post_call_callback(self, attr: str, callback: Callable[..., None]):
            self.__add_callback(f'{attr}__post', callback)

        def add_pre_call_callback(self, attr: str, callback: Callable[..., None]):
            self.__add_callback(f'{attr}__pre', callback)

    class WrapperTwo(WrapperOne):

        def __setattr__(self, key: str, value):
            super().__setattr__(key, value)
            try:
                callback_map = super().__getattribute__('_callback_map')
            except AttributeError:
                return
            get_key = f'{key}__set'
            if get_key in callback_map:
                for cb in callback_map[get_key]:
                    cb(value)

        def __getattribute__(self, key: str):
            ret = super().__getattribute__(key)

            try:
                callback_map = super().__getattribute__('_callback_map')
            except AttributeError:
                return ret

            if callable(ret):
                pre_callbacks = []
                pre_key = f'{key}__pre'
                if pre_key in callback_map:
                    pre_callbacks = callback_map[pre_key]
                post_callbacks = []
                post_key = f'{key}__post'
                if post_key in callback_map:
                    post_callbacks = callback_map[post_key]

                ret = _function_callback(ret, pre_callbacks, post_callbacks)

            get_key = f'{key}__get'
            if get_key in callback_map:
                for cb in callback_map[get_key]:
                    cb(self)
            return ret

    return WrapperTwo
