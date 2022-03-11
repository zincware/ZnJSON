from __future__ import annotations

import abc


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

    instance: type = None
    representation: str = None
    level: int = 0

    @abc.abstractmethod
    def _encode(self, obj) -> str:
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
    def _decode(self, value: str):
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

    def encode(self, obj) -> dict:
        """Convert obj to a serializable dict

        Parameters
        ----------
        obj

        Returns
        -------
        dict:
            A dictionary {_type: self.representation, value: serialized_obj}

        """
        return {"_type": self.representation, "value": self._encode(obj)}

    def decode(self, obj: dict):
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
        return self._decode(obj["value"])

    def __eq__(self, other) -> bool:
        """Check if the other object is equal to self.instance

        Can be used for custom overwriting the __eq__ method
        """
        return isinstance(other, self.instance)

    def __lt__(self, other: ConverterBase):
        return self.level < other.level
