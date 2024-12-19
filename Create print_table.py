def print_table(self): #Таким образом, метод обеспечивает удобный способ визуализации табличных данных в текстовом формате.
    try:
        print(" | ".join(self.header))
        for row in self.data:
            print(" | ".join(map(str, row))) 
    except Exception as e:
        raise Exception(f"Error in print_table: {e}")
