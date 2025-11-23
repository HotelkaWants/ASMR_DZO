from database import Database
from theme import colors
import flet as ft
import pandas as pd

class ImportDataScreen(ft.Page):
    def __init__(self, page):
        self.page = page
        self.db = Database()
        self.db.connect()
        self.file_picker = ft.FilePicker(on_result=self.on_file_picker_result)
        self.page.overlay.append(self.file_picker)
        self.page.update()

    def build(self):
        self.preview_container = ft.Column()

        upload_csv_button = ft.ElevatedButton(
            text="Загрузить CSV",
            on_click = lambda e: self.file_picker.pick_files(
                allow_multiple=False,            
                file_type=ft.FilePickerFileType.CUSTOM,
                allowed_extensions=['csv']
            ),
            bgcolor=colors.dark_blue,
            style=ft.ButtonStyle(color=colors.background_blue)
        )
        send_button = ft.ElevatedButton(
            text="Отправить CSV",
            bgcolor=colors.dark_blue,
            style=ft.ButtonStyle(color=colors.background_blue)
        )
        return ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        self.preview_container,  
                    ],
                    scroll=ft.ScrollMode.AUTO,
                    expand=True,
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    controls=[
                        upload_csv_button,
                        send_button
                    ],
                    alignment=ft.MainAxisAlignment.END,
                    expand=True
                ),
            ]
        )
    def _create_preview_table(self, df: pd.DataFrame, max_rows: int = 10, max_cols: int = 10) -> ft.DataTable:
        df_preview = df.iloc[:max_rows, :max_cols].fillna('').astype(str)
        cols = list(df_preview.columns)
        if df.shape[1] > max_cols:
            cols = cols[:max_cols]
        data_columns = [ft.DataColumn(ft.Text(col)) for col in cols]
        data_rows = []
        for _, row in df_preview.iterrows():
            cells = [ft.DataCell(ft.Text(row[col])) for col in cols]
            data_rows.append(ft.DataRow(cells=cells))
        return ft.DataTable(columns=data_columns, rows=data_rows, border=ft.border.all(1, colors.grey))    


    def on_file_picker_result(self, e: ft.FilePickerResultEvent):
        if e.files:
            for file in e.files:
                if file.name.endswith('.csv'):
                    try:
                        # self.db.load_from_csv(file.path, "Показатели")
                        try:
                            df = pd.read_csv(file.path)
                            table = self._create_preview_table(df, max_rows=10, max_cols=10)
                            self.preview_container.controls = [
                                ft.Text(f"Превью файла: {file.name}", weight="bold"),
                                table
                            ]
                        except Exception as ex2:
                            print(f"Ошибка при создании превью: {ex2}")
                            self.preview_container.controls = [ft.Text("Не удалось сформировать превью.")]
                    except Exception as ex:
                        print(f"Ошибка при загрузке CSV: {ex}")
                        self.preview_container.controls = [ft.Text("Ошибка загрузки файла в базу.")]
                
        self.page.update()