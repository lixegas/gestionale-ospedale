
from connectors import connessione_db

cursor = connessione_db.cursor(dictionary=True)


def prenotazione(medico_che_prenota, paziente_prenotato, data_prenotazione, data_visita_formattata, note_aggiuntive):
    query = "INSERT INTO prenotazioni (id_medico, codice_fiscale_paziente, data_prenotazione, data_visita, note_aggiuntive) VALUES (%s, %s, %s, %s, %s)"
    valori = (medico_che_prenota, paziente_prenotato, data_prenotazione, data_visita_formattata, note_aggiuntive)
    
    try:
        cursor.execute(query, valori)
        connessione_db.commit()
        print("Prenotazione inserita correttamente nel database.")
    except Exception as e:
        print("Si è verificato un errore durante l'inserimento della prenotazione nel database:", e)
        connessione_db.rollback()
    
