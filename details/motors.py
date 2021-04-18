from details import Details, DetailType


class Motors(Details):
    def __init__(self, ser_num: int = 0, products: str = '', material: str = '') -> None:
        super().__init__(DetailType.NoChassis, ser_num, products, material)
