from ..manager import DetailsManager
from .. import DetailType, Doors, Wheels, Motors


class DetailsTest:
    def __init__(self) -> None:
        pass

    def main(self) -> None:
        fac = DetailsManager()
        fac.add_details([
            Doors(10232, 'German', 'Metal'),
            Wheels(20456, 'England', 'Metal'),
            Motors(20866, 'German', 'Metal'),
            Doors(10646, 'Spain', 'Metal'),
            Wheels(30564, 'England', 'Metal'),
            Motors(17777, 'Spain', 'Metal'),
        ])

        print('All:\n\t', '\n\t'.join([str(i) for i in fac.details]), '\n')
        print('Sorted by ser_num:\n\t',
              '\n\t'.join([str(i) for i in fac.sort_by_ser_num(True)]), '\n')
        print('Sorted by product:\n\t',
              '\n\t'.join([str(i) for i in fac.sort_by_product(fac.details, DetailType.Chassis)]), '\n')
