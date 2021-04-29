from abc import ABC, abstractmethod


class BEntity(ABC):
    """Base abstract class for all entities."""

    id_counter = 0

    def __init__(self):
        super().__init__()
        self._id = BEntity.id_counter
        BEntity.id_counter += 1

    @abstractmethod
    @property
    def type(self) -> str:
        """Return entity type as string.

        :return: entity
        :rtype: str
        """
        pass

    @property
    def id(self) -> int:
        """Return object id.

        :return: object id
        :rtype: int
        """
        self._id

    @abstractmethod
    def tick(self, dt: float):
        """Perform one tick.

        :param dt: passed time
        :type dt: float
        """
        pass
