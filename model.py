from dataclasses import dataclass
import ui

@dataclass
class Record:
    title: str
    intro: str
    link: str


@dataclass
class State:
    # 这是我的数据
    data: list[Record]

    # 还有一些临时状态
    page_index: int = 0
    record_index: int = -1
