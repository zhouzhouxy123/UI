import flet

def create_16_layout(page: flet.Page):
   # 创建一个1:6比例的布局
   layout = flet.Column(
       [
           # 第一列，占1/6的宽度
           flet.Row(
               [
                   # 第一行，占1/6的高度
                   flet.Text("第一列第一行"),
               ],
               alignment=flet.MainAxisAlignment.SPACE_AROUND,
               horizontal_alignment=flet.CrossAxisAlignment.START,
               width="100px",
               height="100px",
               border=flet.border.all(1, "black"),
               border_radius=5,
           ),

           # 第二列，占5/6的宽度
           flet.Row(
               [
                   # 第一行，占1/6的高度
                   flet.Text("第一列第二行"),
               ],
               alignment=flet.MainAxisAlignment.SPACE_AROUND,
               horizontal_alignment=flet.CrossAxisAlignment.START,
               width="500px",
               height="100px",
               border=flet.border.all(1, "black"),
               border_radius=5,
           ),
       ],
       alignment=flet.MainAxisAlignment.SPACE_AROUND,
       horizontal_alignment=flet.CrossAxisAlignment.START,
       height=page.window_height,
       width="600px",
       border=flet.border.all(1, "black"),
       border_radius=5,
   )

   # 将布局添加到页面
   page.add(layout)