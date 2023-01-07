from enum import Enum


class BaseChoiceMixin(Enum):
    @classmethod
    def choices(cls):
        return ((i.name, i.value) for i in cls)


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


class AppealDirection(BaseChoiceMixin):
    dip = "Diplom olish masalalari"
    ish = "Ishga joylash, ishdagi tortishuv, oylik maoshi"
    kon = "Kontrakt to'lovi to'g'risida"
    mag = "Magistratura masalalari"
    fuq = "Fuqarolar murojaatlari to'g'risida"
    mol = "Moliyaviy masalalar"
    tal = "Talaba ustidan shikoyat"
    rah = "Rahbar faoliyatidan norozilik arizasi"
    sti = "Stipendiya masalalari"
    oqk = "O'qishga kirish to'g'risida"
    oqc = "O'qishni ko'chirish to'g'risida"
    oqt = "O'qishni tiklash to'g'risida"
    ijo = "Ijodiy imtihondan norozilik to'g'risida"
    dix = "Diplom xaqqoniyligini tasdiqlab berish to'g'risida"
    naf = "Nafaqa masalalari"
    arx = "Arxiv ma'lumotlarini olish to'grisida"
    ikk = "Ikkinchi mutaxasislik"
    kit = "Kitob nashr qilish"
    ixt = "Ixtiro qilish taklifi"
    tak = "Taklif va minnatdorchilik"
    sir = "Sirtqi o'qish masalalari"
    yot = "Yotoqxona masalalari bo'yicha"
    oli = "Olimpiada masalasi bo'yicha"
    bos = "Boshqa yo'nalishlar"


class AppealStatus(BaseChoiceMixin):
    n = "Yangi"
    p = "Ko\'rib chiqilmoqda"
    r = "Rad etilgan"
    d = "Bajarilgan"
