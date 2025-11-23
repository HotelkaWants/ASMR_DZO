from data_classes import Indicator
import theme.colors as colors
import flet as ft
from database import Database
class IndicatorsScreen:
    def __init__(self, page):
        self.page = page
        self.db = Database()
        self.db.connect()
        self.indicators = self.db.get_indicators()

    def build(self):
        table_header = ft.Row(
            controls=[
                ft.Text("Код показателя", color=colors.dark_blue, weight=ft.FontWeight.BOLD, expand=True, text_align=ft.TextAlign.CENTER),
                ft.Text("Показатель", color=colors.dark_blue, weight=ft.FontWeight.BOLD, expand=True, text_align=ft.TextAlign.CENTER),
                ft.Text("Вид аналитики 1", color=colors.dark_blue, weight=ft.FontWeight.BOLD, expand=True, text_align=ft.TextAlign.CENTER),   
                ft.Text("Вид аналитики 2", color=colors.dark_blue, weight=ft.FontWeight.BOLD, expand=True, text_align=ft.TextAlign.CENTER),
                ft.Text("Вид аналитики 3", color=colors.dark_blue, weight=ft.FontWeight.BOLD, expand=True, text_align=ft.TextAlign.CENTER),
            ]
        )
        return ft.Column(
            controls=[
                table_header,
                ft.Divider(color=colors.grey),
                *[self.display_content(indicator) for indicator in self.indicators]
            ]
        )


    def display_content(self, indicator, ):

        return ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(indicator.id, color=colors.dark_blue, expand=True, text_align=ft.TextAlign.CENTER),
                        ft.Text(indicator.indicator_name, color=colors.dark_blue, expand=True, text_align=ft.TextAlign.CENTER),
                        ft.Text(indicator.id_analytic_type_1, color=colors.dark_blue, expand=True, text_align=ft.TextAlign.CENTER),   
                        ft.Text(indicator.id_analytic_type_2, color=colors.dark_blue, expand=True, text_align=ft.TextAlign.CENTER),
                        ft.Text(indicator.id_analytic_type_3, color=colors.dark_blue, expand=True, text_align=ft.TextAlign.CENTER),
                    ]
                ),
                ft.Divider(color=colors.grey),
            ]
        )