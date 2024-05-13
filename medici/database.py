from connectors import connessione_db

cursor = connessione_db.cursor(dictionary=True)


def salva_medico(id_medico, nome_medico_completo, numero_di_telefono, specializzazione, email, password, data_di_nascita_formattata, genere, indirizzo):
    query = "INSERT INTO medici(id_medico, nome_medico_completo, numero_di_telefono, specializzazione, email, password, data_di_nascita, genere, indirizzo) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,[id_medico, nome_medico_completo, numero_di_telefono, specializzazione, email, password, data_di_nascita_formattata, genere, indirizzo])
    
    connessione_db.commit()
  
    
    
def cerca_by_id_medico(id_medico):
    
    query = "SELECT * FROM medici WHERE id_medico=(%s)"
    cursor.execute(query,[id_medico])
    return cursor.fetchone()


def visualizza(id_medico,password):
    
    query = "SELECT * FROM  medici WHERE id_medico = (%s) AND password = (%s)"
    cursor.execute(query,[id_medico,password])
    return cursor.fetchone()



def aggiorna_nome_medico(nuovo_nome_medico,nome_medico_vecchio):
    
    query = "UPDATE medici SET nome_medico_completo = (%s) WHERE nome_medico_completo = (%s)"
    cursor.execute(query,[nuovo_nome_medico,nome_medico_vecchio])
    
    connessione_db.commit()
    
    
def aggiorna_numero_medico(nuovo_numero_medico,numero_medico_vecchio):
    
    query = "UPDATE medici SET numero_di_telefono = (%s) WHERE numero_di_telefono = (%s)"
    cursor.execute(query,[nuovo_numero_medico,numero_medico_vecchio])
    
    connessione_db.commit()
    


def aggiorna_specializzazione_medico(nuova_specializzazione_medico, specializzazione_medico_vecchio):
    
    query = "UPDATE medici SET specializzazione = (%s) WHERE specializzazione = (%s)"
    cursor.execute(query,[nuova_specializzazione_medico, specializzazione_medico_vecchio])
    
    connessione_db.commit()
    
    
    
def aggiorna_email_medico(nuova_email_medico, email_medico_vecchio):
    
    query = "UPDATE medici SET email = (%s) WHERE email = (%s)"
    cursor.execute(query,[nuova_email_medico, email_medico_vecchio])
    
    connessione_db.commit()
    


    
def aggiorna_password_medico(nuova_password_medico, password_medico_vecchio):
    
    query = "UPDATE medici SET password = (%s) WHERE password = (%s)"
    cursor.execute(query,[nuova_password_medico, password_medico_vecchio])
    
    connessione_db.commit()   
    
    

def aggiorna_indirizzo_medico(nuovo_indirizzo_medico,indirizzo_medico_vecchio):
    
    query = "UPDATE medici SET indirizzo = (%s) WHERE indirizzo = (%s)"
    cursor.execute(query,[nuovo_indirizzo_medico,indirizzo_medico_vecchio])
    
    connessione_db.commit()   
    
    
    
    
def elimina_medico(id_medico,password):
    
    query = "DELETE FROM medici WHERE id_medico = (%s) AND password = (%s)"
    cursor.execute(query,[id_medico,password])
    
    connessione_db.commit()
    
    
