from __future__ import annotations
import ui
import flet

def to_screen(view_object: ui.UI): #页面呈现
    def main(page: flet.Page):
        m = _to_screen(view_object)
        if isinstance(m, flet.Container):
            m.width = page.window_width
            m.height = "600px",

        page.add(m)
    flet.app(target=main)

def _to_screen(view_object: ui.UI) -> flet.Control:#指定函数的参数类型和返回类型
    if isinstance(view_object, ui.VFrame):
        # 生成一个带圆框的容器，竖方向居中排列多个子元素

        c = flet.Container()
        c.border_radius = 5
        c.border = flet.border.all(1, "black")
        c.content = flet.Column(
            [
                _to_screen(child)
                for child in view_object.children
            ],
            alignment=flet.MainAxisAlignment.SPACE_AROUND,
            horizontal_alignment=flet.CrossAxisAlignment.CENTER,
            width="100px",
            height="100px",
        )
        return c
    elif isinstance(view_object, ui.HFrame):
        # 生成一个带圆框的容器，横向居中排列多个子元素

        c = flet.Container()
        c.border_radius = 5 
        c.border = flet.border.all(1, "black")
        c.content = flet.Row(
            [
                _to_screen(child)
                for child in view_object.children
            ],
            alignment=flet.MainAxisAlignment.SPACE_AROUND,
            vertical_alignment=flet.CrossAxisAlignment.CENTER,
            width="500px",
            height="100px",
        )
        return c
    elif isinstance(view_object, ui.Label):
        # 生成一个带圆框的容器，显示文本

        return flet.Text(view_object.text)

    elif isinstance(view_object, ui.Align):
        # 获取view_object的align属性
        align_str = view_object.align
        # 获取view_object的child属性
        child = view_object.child

        # 根据align_str的值，返回不同的布局
        match align_str:
            case "left":
                return flet.Row(
                    [
                        _to_screen(child)
                    ],
                    alignment=flet.MainAxisAlignment.START,
                    vertical_alignment=flet.CrossAxisAlignment.CENTER,
                )
            case "right":
                return flet.Row(
                    [
                        _to_screen(child)
                    ],
                    alignment=flet.MainAxisAlignment.END,
                    vertical_alignment=flet.CrossAxisAlignment.CENTER,
                )
            case "center":
                return flet.Row(
                    [
                        _to_screen(child)
                    ],
                    alignment=flet.MainAxisAlignment.CENTER,
                    vertical_alignment=flet.CrossAxisAlignment.CENTER,
                )
            case _:
                # 如果align_str的值不是left、right、center，抛出异常
                raise ValueError(f"Unknown align: {align_str}")
    else:
        # 如果view_object的类型不是ui.Align，抛出异常
        raise ValueError(f"Unknown type: {type(view_object)}")