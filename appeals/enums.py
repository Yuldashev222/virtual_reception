from enum import Enum


class BaseChoiceMixin(Enum):
    @classmethod
    def choices(cls):
        return ((i.name, i.value) for i in cls)

    @classmethod
    def get_values(cls):
        return [_.value for _ in cls]


class Provinces(BaseChoiceMixin):
    tas = "Toshkent"
    sam = "Samarqand"
    an = "Andijon"
    far = "Fargona"
    nam = "Namangan"
    qash = "Qashqadaryo"
    sur = "Surxondaryo"
    bux = "Buxoro"
    nav = "Navoiy"
    xor = "Xorazm"
    sir = "Sirdaryo"
    jiz = "Jizzax"
    qor = "Qoraqalpog\'iston Respublikasi"


class AppealType(BaseChoiceMixin):
    a = "Ariza"
    s = "Shikoyat"
    t = "Taklif"
    b = "boshqa"


class AppealStatus(BaseChoiceMixin):
    n = "Yangi"
    p = "Ko\'rib chiqilmoqda"
    r = "Rad etilgan"
    d = "Bajarilgan"


class ApplicantPosition(BaseChoiceMixin):
    tal = "Talaba"
    oon = "Ota ona"
    oqi = "O'qituvchi"
    uni = "Universitet xodimi"
    tas = "Tashkilot"
    bos = "Boshqa"


class ApplicantType(BaseChoiceMixin):
    y = "Yuridik shaxs"
    j = "Jismoniy shaxs"
