from typing import List
from .. import Details, DetailType


class DetailsManager:
    def __init__(self) -> None:

        self.details = []

    def add_detail(self, detail: Details) -> None:
        self.details.append(detail)

    def add_details(self, details: List[Details]) -> None:
        self.details += details

    def sort_by_ser_num(self, details: list, order: DetailType):
        return sorted(details, key=lambda s: s.sser_num, reverse=order.value)

    def sort_by_product(self, details: list, order: DetailType):
        return sorted(details, key=lambda s: s.pproduct, reverse=order.value)
