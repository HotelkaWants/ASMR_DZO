from data_classes import AnalyticType
import flet as ft
import theme.colors as colors
from database import Database

class AnalyticsTypesScreen(ft.Page):
    def __init__(self, page):
        self.page = page
        self.db = Database()
        self.db.connect()
        self.analytics_types = self.db.get_analytics_types()

    def build(self):
        table_header = ft.Row(
            controls=[
                ft.Text("Код вида аналитики", color=colors.dark_blue, weight=ft.FontWeight.BOLD, expand=True, text_align=ft.TextAlign.CENTER),
                ft.Text("Вид аналитики", color=colors.dark_blue, weight=ft.FontWeight.BOLD, expand=True, text_align=ft.TextAlign.CENTER),   
            ]
        )
        return ft.Column(
            controls=[
                table_header,
                ft.Divider(color=colors.grey),
                *[self.display_content(analytic_type) for analytic_type in self.analytics_types]
            ]
        )

    def display_content(self, analytic_type: AnalyticType):
        return ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(analytic_type.id, color=colors.dark_blue, expand=True, text_align=ft.TextAlign.CENTER),
                        ft.Text(analytic_type.analytic_type_name, color=colors.dark_blue, expand=True, text_align=ft.TextAlign.CENTER),
                    ]
                ),
                ft.Divider(color=colors.grey),
            ]
        )