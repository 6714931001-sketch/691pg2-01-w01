class Program:
    def __init__(self, short_name, name_th, name_en):
        self.short_name = short_name
        self.name_th = name_th
        self.name_en = name_en

    def __str__(self):
        return f"สาขา {self.name_th} ({self.short_name})"