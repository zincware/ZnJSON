"""ZnJSON converter parent class"""

from __future__ import annotations

import abc
import base64
import functools
import io
import logging

log = logging.getLogger(__name__)


def _depreciate_decorator(func, old: str, new: str):
    """Wrap the function with a depreciation warning"""

    @functools.wraps(func)
    def log_warning(*args, **kwargs):
        log.warning(
            f"DEPRECATED: '{old}' is deprecated and will be removed in future releases."
            f" Use '{new}' instead."
        )
        return func(*args, **kwargs)

    return log_warning


class ConverterBase(abc.ABC):
    """Base class for all converters

    Attributes
    ----------
    instance: type
        the type of the object to convert, e.g. np.ndarray or pathlib.Path
    representation: str
        the name of the object to convert. should e.g. be `pathlib.Path`
    level: int
        The level in which the encoding should be applied. A higher number means it will
        try this first. E.g. test small numpy conversion before pickle
        first.
    """

    instance: type
    representation: str
    level: int = 10

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        if hasattr(cls, "_encode"):
            func = _depreciate_decorator(
                getattr(cls, "_encode"), old="_encode()", new="encode()"
            )
            setattr(cls, "encode", func)
        if hasattr(cls, "_decode"):
            func = _depreciate_decorator(
                getattr(cls, "_decode"), old="_decode()", new="decode()"
            )
            setattr(cls, "decode", func)
        return cls

    @abc.abstractmethod
    def encode(self, obj) -> str:
        """Convert obj to a serializable str

        Serialize the given object

        Parameters
        ----------
        obj: Any
            Object of type self.instance to serialize

        Returns
        -------
        str:
            a serialized string of the parsed obj

        """
        raise NotImplementedError

    @abc.abstractmethod
    def decode(self, value: str):
        """Convert dict to instance of self.instance

        Parameters
        ----------
        value: str
            output of self._encode to be decoded back to an instace

        Returns
        -------

        instance of self.instance based on the given value

        """
        raise NotImplementedError

    def encode_obj(self, obj) -> dict:
        """Convert obj to a serializable dict

        Parameters
        ----------
        obj

        Returns
        -------
        dict:
            A dictionary {_type: self.representation, value: serialized_obj}

        """
        return {"_type": self.representation, "value": self.encode(obj)}

    def decode_obj(self, obj: dict):
        """Convert parsed dict back to instance

        Parameters
        ----------
        obj: dict
            A dictionary {_type: self.representation, value: serialized_obj}

        Returns
        -------
        any:
            instance of self.instance

        """
        return self.decode(obj["value"])

    def __eq__(self, other) -> bool:
        """Check if the other object is equal to self.instance

        Can be used for custom overwriting the __eq__ method
        """
        return isinstance(other, self.instance)

    def __lt__(self, other: ConverterBase):
        return self.level < other.level

    @staticmethod
    def save_to_b64(method):
        """Use the method, e.g. np.save into memory and then return as ascii string"""
        with io.BytesIO() as file:
            method(file)
            file.seek(0)
            return base64.b64encode(file.read()).decode("ascii")

    @staticmethod
    def load_from_b64(value, method):
        """Convert a string from memory such that it can be read e.g. by np.load"""
        with io.BytesIO() as file:
            file.write(base64.b64decode(value))
            file.seek(0)
            return method(file)
