import flet as ft
import theme.colors as colors
from data_classes import ValueIndicator
from database import Database
class ValuesIndicatorsScreen(ft.Page):

    def __init__(self, page):
        self.page = page
        self.db = Database()
        self.db.connect()
        self.values_indicators = self.db.get_values_indicators()

    def build(self):
        table_header = ft.Row(
            controls=[
                ft.Text("Дата начала периода", color=colors.dark_blue, weight=ft.FontWeight.BOLD, expand=True, text_align=ft.TextAlign.CENTER),
                ft.Text("Дата окончания периода", color=colors.dark_blue, weight=ft.FontWeight.BOLD, expand=True, text_align=ft.TextAlign.CENTER),
                ft.Text("Код показателя", color=colors.dark_blue, weight=ft.FontWeight.BOLD, expand=True, text_align=ft.TextAlign.CENTER),
                ft.Text("Код аналитики 1", color=colors.dark_blue, weight=ft.FontWeight.BOLD, expand=True, text_align=ft.TextAlign.CENTER),   
                ft.Text("Код аналитики 2", color=colors.dark_blue, weight=ft.FontWeight.BOLD, expand=True, text_align=ft.TextAlign.CENTER),
                ft.Text("Код аналитики 3", color=colors.dark_blue, weight=ft.FontWeight.BOLD, expand=True, text_align=ft.TextAlign.CENTER),
                ft.Text("Сумма", color=colors.dark_blue, weight=ft.FontWeight.BOLD, expand=True, text_align=ft.TextAlign.CENTER),     
            ]
        )
        return ft.Column(
            controls=[
                table_header,
                ft.Divider(color=colors.grey),
                *[self.display_content(value_indicator) for value_indicator in self.values_indicators]
            ]
        )

    def display_content(self, value_indicator: ValueIndicator):
        return ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(value_indicator.date_period_start, color=colors.dark_blue, expand=True, text_align=ft.TextAlign.CENTER),
                        ft.Text(value_indicator.date_period_end, color=colors.dark_blue, expand=True, text_align=ft.TextAlign.CENTER),
                        ft.Text(value_indicator.id_indicator, color=colors.dark_blue, expand=True, text_align=ft.TextAlign.CENTER),
                        ft.Text(value_indicator.analytic_1, color=colors.dark_blue, expand=True, text_align=ft.TextAlign.CENTER),   
                        ft.Text(value_indicator.analytic_2, color=colors.dark_blue, expand=True, text_align=ft.TextAlign.CENTER),
                        ft.Text(value_indicator.analytic_3, color=colors.dark_blue, expand=True, text_align=ft.TextAlign.CENTER),
                        ft.Text(str(value_indicator.sum_value), color=colors.dark_blue, expand=True, text_align=ft.TextAlign.CENTER),
                    ]
                ),
                ft.Divider(color=colors.grey),
            ]
        )