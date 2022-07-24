from enum import Enum

class OrderStatus(Enum):
    AWAITING_DELIVERY = "Ожидает доставку"
    ON_THE_WAY = "Товар в пути к выручении"
    DELIVERED = "Товар выручен"