from model import Record, State
from view import render
from backend import to_screen

DATA: list[Record] = [
    Record(
        title=f"标题{i}",
        intro=f"第{i}个简介",
        link=f"https://www.baidu.com/s?wd={i}")
    for i in range(20)
]

STATE = State(data=DATA)

vdom = render(STATE)
# from pprint import pprint
# pprint(vdom)
to_screen(vdom)
