from __future__ import annotations
import ui
import flet

def layout(view_object: ui.UI) -> flet.Control:
    if isinstance(view_object, ui.VFrame):
        c = flet.Container()
        c.border_radius = 5
        c.border = flet.border.all(1, "black")

        children_controls = [
            layout(child) for child in view_object.children
        ]

        total_weight = sum(child.weight for child in view_object.children) if view_object.children else 1

        c.content = flet.Column(
            children_controls,
            alignment=flet.MainAxisAlignment.SPACE_AROUND,
            horizontal_alignment=flet.CrossAxisAlignment.CENTER,
            weights=[child.weight / total_weight for child in view_object.children]
        )
        return c
    elif isinstance(view_object, ui.HFrame):
        c = flet.Container()
        c.border_radius = 5
        c.border = flet.border.all(1, "black")

        children_controls = [
            layout(child) for child in view_object.children
        ]

        total_weight = sum(child.weight for child in view_object.children) if view_object.children else 1

        c.content = flet.Row(
            children_controls,
            alignment=flet.MainAxisAlignment.SPACE_AROUND,
            vertical_alignment=flet.CrossAxisAlignment.CENTER,
            weights=[child.weight / total_weight for child in view_object.children]
        )
        return c
    elif isinstance(view_object, ui.Label):
        return flet.Text(view_object.text)
    elif isinstance(view_object, ui.Align):
        align_str = view_object.align
        child = view_object.child

        match align_str:
            case "left":
                return flet.Row(
                    [
                        layout(child)
                    ],
                    alignment=flet.MainAxisAlignment.START,
                    vertical_alignment=flet.CrossAxisAlignment.CENTER,
                )
            case "right":
                return flet.Row(
                    [
                        layout(child)
                    ],
                    alignment=flet.MainAxisAlignment.END,
                    vertical_alignment=flet.CrossAxisAlignment.CENTER,
                )
            case "center":
                return flet.Row(
                    [
                        layout(child)
                    ],
                    alignment=flet.MainAxisAlignment.CENTER,
                    vertical_alignment=flet.CrossAxisAlignment.CENTER,
                )
            case _:
                raise ValueError(f"Unknown align: {align_str}")
    else:
        raise ValueError(f"Unknown type: {type(view_object)}")