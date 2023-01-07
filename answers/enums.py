from enum import Enum


class BaseChoiceMixin(Enum):
    @classmethod
    def choices(cls):
        return ((i.name, i.value) for i in cls)


class AnswerType(BaseChoiceMixin):
    d = "bajarildi"
    r = "rad etildi"


class AnswerAddress(BaseChoiceMixin):
    s = "Sayt"
    e = "Email"
    se = "Sayt va Email"
