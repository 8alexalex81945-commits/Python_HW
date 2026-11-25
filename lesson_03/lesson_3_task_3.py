from address import Address
from mailing import Mailing

to_address = Address("142900", "Кашира", "Ленина", "5", "8")
from_address = Address("307100", "Курск", "Соловьиная роща", "7", "5")
mailing = Mailing(to_address, from_address, 550, "TRACK12345RU")

print(
    f"Отправление {mailing.track} из {mailing.from_address.postal_code}, "
    f"г.{mailing.from_address.city}, ул.{mailing.from_address.street}, "
    f"д.{mailing.from_address.house}, кв.{mailing.from_address.flat}. "
    f"в {mailing.to_address.postal_code}, г.{mailing.to_address.city}, "
    f"ул.{mailing.to_address.street}, д.{mailing.to_address.house}, кв."
    f"{mailing.to_address.flat}. Стоимость {mailing.cost} рублей."
)
