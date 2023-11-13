from dataclasses import dataclass
import typing

# @dataclass 装饰器用于装饰类，省去了手动编写 __init__、__repr__ 等方法的步骤。同时，通过类型注解来指定每个属性的类型。

class UI:
    pass

@dataclass
class HFrame(UI): #继承UI类
    children: list[UI]

@dataclass
class VFrame(UI):
    children: list[UI]

@dataclass
class Label(UI):
    text: str

@dataclass
class Align(UI):
    child: UI
    align: str

@dataclass
class Click(UI):
    child: UI
    onClick: typing.Callable[[], None]

@dataclass
class Sizer(UI):
    child: UI
    width: float
    height: float
    alignment: str