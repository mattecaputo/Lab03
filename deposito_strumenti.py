import csv
from operator import attrgetter
from strumento import Strumento
from prestito import Prestito



class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self._responsabile = responsabile
        self.strumenti = {}     # dizionario dove vengono memorizzati gli oggetti della classe strumento  ( es: S1 ---> Strumento )
        self.prestiti = {}      #  dizionario dove vengono memorizzati gli oggetti della classe prestito  ( es: P1 ---> Prestito )

        # contatori per generare i codici  di strumenti/ prestiti
        self._counter_strumenti = 0
        self._counter_prestiti = 0


    @property
    def responsabile(self):
        #metodo getter per accedere al responsabile
        return self._responsabile

    @responsabile.setter
    def responsabile(self, nuovo_responsabile):
        #metodo setter per modificare il responsabile
        self._responsabile = nuovo_responsabile




    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        try:
            with open(file_path, mode='r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for riga in reader:
                    #estraiamo i dati ripulendoli dal superflio
                    id_str, tipo, marca, anno, valore = [campo.strip() for campo in riga]

                    # Crea e memorizza l'oggetto Strumento nel dizionario
                    self.strumenti[id_str] = Strumento(id_str, tipo, marca, int(anno), float(valore))

                    # aggiornamento del contatore
                    if id_str.startswith('S') and id_str[1:].isdigit():
                        self._counter_strumenti = max(self._counter_strumenti, int((id_str[1:])))


        #eccezione se non trova il file
        except FileNotFoundError:
            raise FileNotFoundError(f" Il file '{file_path}' non è stato trovato.")

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # incrementa il contatore
        self._counter_strumenti += 1
        id_nuovo = f'S{self._counter_strumenti}'

        # creazione dell'oggetto che viene inserito nel dizionario
        nuovo_strumento = Strumento(id_nuovo, tipo, marca, anno_acquisto, valore)
        self.strumenti[id_nuovo] = nuovo_strumento
        return nuovo_strumento

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        return sorted(self.strumenti.values(), key=attrgetter('marca'))


    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # Verifica se lo strumento è nel deposito
        if id_strumento not in self.strumenti:
            raise Exception(f" Lo strumento '{id_strumento}' non è stato trovato nel deposito")

        # scorrimento dei prestiti per controllare se lo strumento è già occupato
        for prestito in self.prestiti.values():
            if prestito.id_strumento == id_strumento:
                raise Exception(f" Lo strumento '{id_strumento}' è già attualmente in prestito")

        # incremento contatore dei prestiti
        self._counter_prestiti += 1
        id_prestito = f'P{self._counter_prestiti}'

        # Crea e registra il nuovo prestito nel dizionario
        prestito = Prestito(id_prestito, data, id_strumento, cognome_allievo)
        self.prestiti[id_prestito] = prestito
        return prestito


    def termina_prestito(self, id_prestito):
        if id_prestito not in self.prestiti:
            raise Exception(f" Il prestito con codice '{id_prestito}' non esiste")

        # Rimozione del prestito dal dizionario
        self.prestiti.pop(id_prestito)