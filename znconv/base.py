import abc


class Converter(abc.ABC):

    instance = abc.abstractmethod

    @abc.abstractmethod
    def encode(self, obj):
        raise NotImplementedError

    @abc.abstractmethod
    def decode(self, obj):
        raise NotImplementedError
