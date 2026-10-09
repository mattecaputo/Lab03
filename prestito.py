class prestito:
    def __init__(self,id_prestito,data_prestito,id_strumento,cognome):
        self.id_prestito = id_prestito
        self.data_prestito = data_prestito
        self.id_strumento = id_strumento
        self.cognome = cognome


    def __str__(self):
        return f"[{self.id_prestito}] Data: {self.data_prestito} | Strumento : {self.id_strumento} | Allievo: {self.cognome}"


    def __repr__(self):
        return self.__str__