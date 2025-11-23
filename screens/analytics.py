import flet as ft
import theme.colors as colors
from data_classes import Analytic
from database import Database
class AnalyticsPage(ft.Page):
    def __init__(self, page):
        self.page = page
        self.db = Database()
        self.db.connect()
        self.analytics = self.db.get_analytics()

    def build(self):
        table_header = ft.Row(
            controls=[
                ft.Text("Код аналитики", color=colors.dark_blue, weight=ft.FontWeight.BOLD, expand=True, text_align=ft.TextAlign.CENTER),
                ft.Text("Код вида аналитики", color=colors.dark_blue, weight=ft.FontWeight.BOLD, expand=True, text_align=ft.TextAlign.CENTER),
                ft.Text("Аналитика", color=colors.dark_blue, weight=ft.FontWeight.BOLD, expand=True, text_align=ft.TextAlign.CENTER),   
            ]
        )
        return ft.Column(
            controls=[
                table_header,
                ft.Divider(color=colors.grey),
                *[self.display_content(analytic) for analytic in self.analytics]
            ]
        )

    def display_content(self, analytic: Analytic):
        return ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(analytic.id, color=colors.dark_blue, expand=True, text_align=ft.TextAlign.CENTER),
                        ft.Text(analytic.id_analytic_type, color=colors.dark_blue, expand=True, text_align=ft.TextAlign.CENTER),
                        ft.Text(analytic.analytic_name, color=colors.dark_blue, expand=True, text_align=ft.TextAlign.CENTER),
                    ]
                ),
                ft.Divider(color=colors.grey),
            ]
        )

   