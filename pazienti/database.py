from connectors import connessione_db

cursor = connessione_db.cursor(dictionary=True)







def salva_paziente(codice_fiscale, nome_pazienti_completo, data_di_nascita_formatata, genere, indirizzo, numero_di_telefono, email, password):
    query = "INSERT INTO pazienti (codice_fiscale, nome_pazienti_completo, data_di_nascita, genere, indirizzo, numero_di_telefono, email, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (codice_fiscale, nome_pazienti_completo, data_di_nascita_formatata, genere, indirizzo, numero_di_telefono, email, password))
    connessione_db.commit()






def cerca_by_codice_fiscale_paziente(codice_fiscale):
    
    query = "SELECT * FROM pazienti WHERE codice_fiscale = (%s)"
    cursor.execute(query,[codice_fiscale])
    return cursor.fetchone()









def visualizza_paziente(codice_fiscale):
    query = "SELECT * FROM pazienti WHERE codice_fiscale = (%s)"
    cursor.execute(query,[codice_fiscale])
    return cursor.fetchone()


    
    
    
    
    
    
def cerca_paziente_da_eliminare(codice_fiscale,password):
    
    query = "SELECT * FROM pazienti WHERE codice_fiscale = (%s) AND password = (%s)"  
    cursor.execute(query,[codice_fiscale,password])
    return cursor.fetchone()
    
    

def elimina_paziente(codice_fiscale,password):
    
    query = "DELETE FROM pazienti WHERE codice_fiscale= (%s) AND password = (%s)"
    cursor.execute(query,[codice_fiscale, password])
    
    connessione_db.commit()
    
    
    
    
    
    
    
    


def aggiorna_nome_paziente(nome_paziente_nuovo,nome_vecchio_paziente):
    
    query = "UPDATE pazienti SET nome_pazienti_completo = (%s) WHERE nome_pazienti_completo = (%s)"
    cursor.execute(query,[nome_paziente_nuovo,nome_vecchio_paziente])

    connessione_db.commit()
    
    

def aggiorna_indirizzo(indirizzo_nuovo,indirizzo_vecchio):
    
    query = "UPDATE pazienti SET indirizzo = (%s) WHERE indirizzo = (%s)"
    cursor.execute(query,[indirizzo_nuovo,indirizzo_vecchio])

    connessione_db.commit()
    
    
    
def aggiora_numero(numero_telefono_nuovo,numero_telefono_vecchio):
    
    query = "UPDATE pazienti SET numero_di_telefono = (%s) WHERE numero_di_telefono = (%s)"
    cursor.execute(query,[numero_telefono_nuovo,numero_telefono_vecchio])
    
    connessione_db.commit()
    
    
def aggiorna_email(email_nuovo,email_vecchio):
    
    query = "UPDATE pazienti SET email = (%s) WHERE email = (%s)"
    cursor.execute(query,[email_nuovo,email_vecchio])
    
       
    connessione_db.commit()
    
    

    
def aggiorna_password(password_nuovo,password_vecchio):
    
    query = "UPDATE pazienti SET email = (%s) WHERE email = (%s)"
    cursor.execute(query,[password_nuovo,password_vecchio])
    
       
    connessione_db.commit()