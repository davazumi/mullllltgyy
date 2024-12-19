def get_value(self, column=0): #предназначена для извлечения значения из определенной строки и столбца объекта, который, предположительно, представляет собой таблицу данных или набор данных
    try:
        if len(self.data) != 1:
            raise ValueError("Таблица содержит более одной строки.")
        col_index = column if isinstance(column, int) else self.header.index(column)
        return self.data[0][col_index]
    except Exception as e:
        raise Exception(f"Ошибка в get_value: {e}")
