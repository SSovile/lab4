from details import Details, DetailType


class Wheels(Details):
    def __init__(self, ser_num: int = 0, products: str = '', material: str = '') -> None:
        super().__init__(DetailType.Chassis, ser_num, products, material)
