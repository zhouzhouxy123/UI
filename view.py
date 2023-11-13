from model import Record, State
import ui

COUBNT_PER_PAGE = 8

def render(state: State) -> ui.UI:
    # ui.VFrame/ui.HFrame
    preview_list = mk_preview_list(state)
    details = mk_details(state)

    return ui.HFrame(
        children = [
            preview_list,
            details
        ]
    )

def mk_details(state: State):
    if state.record_index >= 0:
        return ui.Label("没有选中任何记录")

    record = state.data[state.record_index]#第几页的第几个  
    return ui.VFrame(
        children = [
            ui.Label(record.title,),#标题
            ui.Label(2 * " " + record.intro),#信息
            ui.Align(ui.Label(record.link), 'left'),#链接，在左边
        ]
    )

def mk_preview_list(state: State): #当前的页面包括哪些
    start = COUBNT_PER_PAGE * state.page_index
    data_to_view = state.data[start:start+COUBNT_PER_PAGE]
    item_list = [       #列表推导式生成一个包含预览项的列表item_list，其中每个预览项由mk_preview_item函数生成。
            mk_preview_item(datum)
            for datum in
            data_to_view
    ]
    item_list: list[ui.UI] = item_list + [  
    #将item_list转换为list[ui.UI]类型，并添加一个包含当前页码和总记录数的ui.HFrame对象作为列表的最后一项。最后，将所有的组件列表传递给ui.VFrame，并返回该对象作为页面的预览。
        ui.HFrame(
            children=[
                ui.Label(f" 第{state.page_index}页 "),
                ui.Label(f"共{len(state.data)}条记录"),
            ]
        )
    ]
    return ui.VFrame(children=item_list)#页面预览

def mk_preview_item(record: Record):
    return ui.HFrame(children=[ui.Label(record.title)])
