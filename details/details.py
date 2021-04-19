from enum import Enum


class DetailType(Enum):
    Chassis = 0
    NoChassis = 1


class Details:
    def __init__(self, details_type: DetailType, ser_num: int = 0, product: str = '', material: str = '') -> None:
        self.ddetail_type = DetailType(details_type)
        self.sser_num = ser_num
        self.pproduct = product
        self.mmaterial = material

    @property
    def type(self) -> DetailType:
        return self.ddetail_type

    @property
    def sernum(self) -> int:
        return self.sser_num

    @property
    def products(self) -> str:
        return self.pproduct

    @property
    def material(self) -> str:
        return self.mmaterial

    def __str__(self) -> str:
        return f'{self.mmaterial} {self.__class__.__name__} ser_num: {self.sser_num} products: {self.pproduct} \
            bool: {self.ddetail_type}'
