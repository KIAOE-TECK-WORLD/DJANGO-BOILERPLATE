from django.db.models import TextChoices


class UserType(TextChoices):
    HOST = "HOST", "Host"
    CLIENT = "CLIENT", "Client"

    @classmethod
    def default(cls):
        return cls.HOST

    @classmethod
    def host(cls):
        return cls.default()

    @classmethod
    def client(cls):
        return cls.CLIENT


class SexType(TextChoices):
    MALE = "MALE", "Male"
    FEMALE = "FEMALE", "Female"

    @classmethod
    def default(cls):
        return cls.MALE

    @classmethod
    def male(cls):
        return cls.default()

    @classmethod
    def female(cls):
        return cls.FEMALE


class StatusType(TextChoices):
    OPEN = "OPEN", "Open"
    CLOSE = "CLOSE", "Close"

    @classmethod
    def default(cls):
        return cls.OPEN

    @classmethod
    def open(cls):
        return cls.default()

    @classmethod
    def close(cls):
        return cls.CLOSE


class CurrencyType(TextChoices):
    XOF = "XOF", "Franc Afrique Ouest"
    XAF = "XAF", "Franc Afrique Central"
    USD = "USD", "Dollar Americain"
    EUR = "EUR", "Euro"

    @classmethod
    def default(cls):
        return cls.XOF

    @classmethod
    def xof(cls):
        return cls.default()

    @classmethod
    def xaf(cls):
        return cls.XAF

    @classmethod
    def usd(cls):
        return cls.USD

    @classmethod
    def eur(cls):
        return cls.EUR


class EventType(TextChoices):
    GASTRONOMIC = "GASTRONOMIC", "GASTRONOMIC"
    CONCERT = "CONCERT", "CONCERT"
    ARTISANAL = "ARTISANAL", "ARTISANAL"

    @classmethod
    def default(cls):
        return cls.GASTRONOMIC

    @classmethod
    def gastronomic(cls):
        return cls.default()


class TicketType(TextChoices):
    VIP = "VIP", "VIP"
    SIMPLE = "SIMPLE", "SIMPLE"
    CLASSIC = "CLASSIC", "CLASSIC"

    @classmethod
    def default(cls):
        return cls.VIP

    @classmethod
    def vip(cls):
        return cls.default()

    @classmethod
    def simple(cls):
        return cls.SIMPLE

    @classmethod
    def classic(cls):
        return cls.CLASSIC
