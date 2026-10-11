import csv
from operator import attrgetter
from strumento import Strumento
from prestito import Prestito



class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self._responsabile = responsabile
        self.strumenti = {}
        self.prestiti = {}
        self._counter_strumenti = 0
        self._counter_prestiti = 0


    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, nuovo_responsabile):
        self._responsabile = nuovo_responsabile




    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        try:
            with open(file_path, mode='r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for riga in reader:
                    id_str, tipo, marca, anno, valore = [campo.strip() for campo in riga]

                    self.strumenti[id_str] = Strumento(id_str, tipo, marca, int(anno), float(valore))

                    if id_str.startswith('S') and id_str[1:].isdigit():
                        self._counter_strumenti = max(self._counter_strumenti, int((id_str[1:])))


        except FileNotFoundError:
            raise FileNotFoundError(f" Il file '{file_path}' non è stato trovato.")

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""

    def termina_prestito(self, id_prestito):
