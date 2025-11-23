import psycopg2
from psycopg2.extras import RealDictCursor
import config
from data_classes import Analytic, Indicator, AnalyticType, ValueIndicator
import pandas as pd

class Database:
    def __init__(self):
        self.connection = None
    
    def connect(self):
        try:
            self.connection = psycopg2.connect(**config.DB_CONFIG)
            return True
        except Exception as e:
            print(f"Ошибка подключения к БД: {e}")
            return False
        
    def execute_query(self, query, params=None):
        try:
            with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(query, params)
                if query.strip().upper().startswith('SELECT') or ('RETURNING' in query.upper()):
                    return cursor.fetchall()
                else:
                    self.connection.commit()
                    return cursor.rowcount
        except Exception as e:
            print(f"Ошибка выполнения запроса: {e}")
            return None
    
    def get_values_indicators(self):
        query = """
        SELECT * FROM public."Значения показателей ДЗО"
        ORDER BY "Код показателя" ASC
        """
        result = self.execute_query(query)
        return [ValueIndicator(row) for row in result] if result else []
    
    def get_analytics_types(self):
        query = """
        SELECT * FROM public."Виды аналитики"
        ORDER BY "Код вида аналитики" ASC
        """
        result = self.execute_query(query)
        return [AnalyticType(row) for row in result] if result else []
        
    def get_analytics(self):
        query = """
        SELECT * FROM public."Аналитики"
        ORDER BY "Код вида аналитики" ASC, "Код аналитики" ASC
        """
        result = self.execute_query(query)
        return [Analytic(row) for row in result] if result else []
    def get_indicators(self):
        query = """
        SELECT * FROM public."Показатели"
        ORDER BY "Код показателя" ASC
        """
        result = self.execute_query(query)
        return [Indicator(row) for row in result] if result else []
    
    def create_value_indicator(self, value_indicator: ValueIndicator):
        try:
            query = """
            INSERT INTO public."Значения показателей ДЗО" (
                "Код показателя",
                "Код аналитики 1",
                "Код аналитики 2",
                "Код аналитики 3",
                "Сумма",
                "Дата начала периода",
                "Дата окончания периода",
                "ДЗО"
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING *
            """
            params = (
                value_indicator.indicator_id,
                value_indicator.id_analytic_type_1,
                value_indicator.id_analytic_type_2,
                value_indicator.id_analytic_type_3,
                value_indicator.sum_value,
                value_indicator.period_start,
                value_indicator.period_end,
                value_indicator.dzo
            )
            result = self.execute_query(query, params)
            return ValueIndicator(result[0]) if result else None
        except Exception as e:
            print(f"Ошибка при создании значения показателя: {e}")
            raise
        
# db = Database()
# if db.connect():
#     result = db.get_values_indicators()
#     for i in result:
#         print(i.to_dict())   