import flet as ft
import theme.colors as colors
from data_classes import User, ValueIndicator
from dialog_manager import DialogManager
from database import Database

class CreateValuesIndicatorReportScreen:
    def __init__(self, page: ft.Page, user: User):
        self.page = page
        self.user = user
        self.db = Database()
        self.db.connect()

    def build(self):
        container = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(f"Создание отчета для ДЗО"),
                    self.build_content()
                ]
            )
        )
        return container

    def build_content(self):
        tf_indicator_id = ft.TextField(label="Код показателя", expand=True, text_style=ft.TextStyle(size=14))
        tf_id_analytic_type_1 = ft.TextField(label="Код аналитики 1", expand=True, text_style=ft.TextStyle(size=14))
        tf_id_analytic_type_2 = ft.TextField(label="Код аналитики 2", expand=True, text_style=ft.TextStyle(size=14))
        tf_id_analytic_type_3 = ft.TextField(label="Код аналитики 3", expand=True, text_style=ft.TextStyle(size=14))
        tf_sum_value = ft.TextField(label="Сумма", expand=True, text_style=ft.TextStyle(size=14))
        tf_period_start = ft.TextField(label="Дата начаоа периода", expand=True, text_style=ft.TextStyle(size=14))
        tf_period_end = ft.TextField(label="Дата окончания периода", expand=True, text_style=ft.TextStyle(size=14))

        def on_create_report_click(e):
            try:
                value_indicator_report = ValueIndicator(
                    indicator_id=tf_indicator_id.value,
                    id_analytic_type_1=tf_id_analytic_type_1.value,
                    id_analytic_type_2=tf_id_analytic_type_2.value,
                    id_analytic_type_3=tf_id_analytic_type_3.value,
                    sum_value=float(tf_sum_value.value),
                    period_start=tf_period_start.value,
                    period_end=tf_period_end.value,
                    dzo = self.user.dzo,
                )
                self.db.create_value_indicator(value_indicator_report)
                self.dialog_manager.show_success_dialog("Отчет создан успешно!")   
            except Exception as ex:
                self.dialog_manager.show_error_dialog(f"Ошибка при создании отчета: {str(ex)}")
        
        self.page.floating_action_button = ft.ElevatedButton(
                    "Создать отчет",
                    on_click=lambda e: on_create_report_click,
                    bgcolor=colors.accent_blue, style=ft.ButtonStyle(color=colors.background_blue)
                )
        content = ft.Column(
            controls=[
                tf_indicator_id,
                tf_id_analytic_type_1,
                tf_id_analytic_type_2,
                tf_id_analytic_type_3,
                tf_sum_value,
                tf_period_start,
                tf_period_end,
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.START,
        )
        return content