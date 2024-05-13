
from medici.database import salva_medico,cerca_by_id_medico,visualizza,aggiorna_nome_medico,aggiorna_numero_medico,aggiorna_specializzazione_medico,aggiorna_email_medico,aggiorna_password_medico,aggiorna_indirizzo_medico,elimina_medico




from datetime import datetime


from prenotazioni.database import prenotazione


from pazienti.wiews import cerca_by_codice_fiscale_paziente








def registra_medico():
    
    id_medico = int(input("Inserisci ID medico:\n"))
    nome_medico_completo = input("Inserisci nome completo (Nome e Cognome):\n") 
    data_di_nascita = input("Inserisci data di nascita (formato: YYYY-MM-DD):\n")
    data_di_nascita_formattata = datetime.strptime(data_di_nascita, '%Y-%m-%d')
    genere = input("Inserisci genere (Maschio - Femmina):\n").upper()
    indirizzo = input("Inserisci indirizzo (Via xxxx, civico):\n")
    numero_di_telefono = input("Inserisci numero di telefono (+** 1234567891):\n")
    specializzazione = input("Inserisci specializzazione:\n")
    email = input("Inserisci email (********04@*****.***):\n")
    password = input("Inserisci password:\n")
    
    salva_medico(id_medico, nome_medico_completo, numero_di_telefono, specializzazione, email, password, data_di_nascita_formattata, genere, indirizzo)
    print("Registrazione eseguita")
    
    

def login_medico():
    while True: 
        id_medico = input("Inserisci ID medico:\n")
        user = cerca_by_id_medico(id_medico)
        if user is None:
            print("ID medico errato")
        else:
            print("ID medico trovato")
            break
        
    while True:
        id_medico = id_medico
        password = input("Inserisci password \n")
        user = cerca_by_id_medico(id_medico)
        if password == user["password"]:
            print("Perfetto")
            break
        else:
            print("Password errata") 
                
                    
def azioni_by_tipo_utente_medico():
    
    OPERAZIONI_UTENTE = ("registra" ,"login")
    print(OPERAZIONI_UTENTE)
    
    while True:
        azione1 = input("Cosa vuoi fare?\n").lower()
        if azione1 == OPERAZIONI_UTENTE[0]:
                    registra_medico()
                    break 
        elif azione1 == OPERAZIONI_UTENTE[1]:
                    login_medico() 
                    break
            

    
         
                
            


def visualizza_medico():
    id_medico = input("Inserisci id medico:\n")
    password = input("Inserisci password \n")
    
    medico_visualizzato = visualizza(id_medico,password)
    
    if password == medico_visualizzato["password"]:
            print(medico_visualizzato)
    else:
            print("Password errata") 
            
            

def aggiorna_datimedico():
    while True:
        DATI_MEDICO = ("nome medico", "numero di telefono", "specializzazione", "email", "password","indirizzo","nessuno")
        print(DATI_MEDICO)
    
 
        dato_da_aggiornare = input("Quale dato vuoi aggiornare?\n").lower()
        
        if dato_da_aggiornare == DATI_MEDICO[0]:
            
            nuovo_nome_medico = input("Inserisci nuovo nome medico (nome e cognome):\n")
            nome_medico_vecchio = input("Inserisci nome medico vecchio (nome e cognome):\n")
                
            DOMANDA_DI_SICUREZZA = input("Sei sicuro di voler proseguire?\n").lower()
            
            if DOMANDA_DI_SICUREZZA == "si":
                aggiorna_nome_medico(nuovo_nome_medico,nome_medico_vecchio)
                print("Modifica effettuata!!")
            else:
                 print("Grazie e arrivederci")
                
        
        elif  dato_da_aggiornare == DATI_MEDICO[1]:
            
            nuovo_numero_medico = input("Inserisci nuovo numero di telefono (+391234567891):\n")
            numero_medico_vecchio = input("Inserisci vecchio numero di telefono  (+391234567891):\n")
            
            DOMANDA_DI_SICUREZZA1 = input("Sei sicuro di voler proseguire?\n").lower()
            
            
            if DOMANDA_DI_SICUREZZA1 == "si":
            
                aggiorna_numero_medico(nuovo_numero_medico, numero_medico_vecchio)
                print("Modifica effettuata")
            else:
                 print("Grazie e arrivederci")
                    
                
            
        elif dato_da_aggiornare == DATI_MEDICO[2]:
            
            
            nuova_specializzazione_medico = input("Inserisci nuova specializzazione:\n")
            specializzazione_medico_vecchio = input("Inserisci vecchia specializzazione:\n")
            
            DOMANDA_DI_SICUREZZA2 = input("Sei sicuro di voler proseguire?\n").lower()
            
            
            if DOMANDA_DI_SICUREZZA2 == "si":
                
                aggiorna_specializzazione_medico(nuova_specializzazione_medico, specializzazione_medico_vecchio)
                print("Modifica effettuata")
            else:
                 print("Grazie e arrivederci")
                    
                    
                
        elif dato_da_aggiornare == DATI_MEDICO[3]:
            
            
            nuova_email_medico = input("Inserisci nuova email (xxxxxxx04@example.com):\n")
            email_medico_vecchio = input("Inserisci vecchia email (xxxxxxx04@example.com):\n")
            
            DOMANDA_DI_SICUREZZA3 = input("Sei sicuro di voler proseguire?\n").lower()
            
            
            if DOMANDA_DI_SICUREZZA3 == "si":
            
                aggiorna_email_medico(nuova_email_medico, email_medico_vecchio)
                print("Modifica effettuata")
            else:
                    print("Grazie e arrivederci")
                    
                
            
            
        elif dato_da_aggiornare == DATI_MEDICO[4]:
            
            
            nuova_password_medico = input("Inserisci nuova password:\n")
            password_medico_vecchio = input("Inserisci vecchia password:\n")
            
            DOMANDA_DI_SICUREZZA4 = input("Sei sicuro di voler proseguire?\n").lower()
            
            
            if DOMANDA_DI_SICUREZZA4 == "si":
            
                aggiorna_password_medico(nuova_password_medico, password_medico_vecchio)
                print("Modifica effettuata")
            else:
                    print("Grazie e arrivederci")
            
            
        elif dato_da_aggiornare == DATI_MEDICO[5]:
            
            nuovo_indirizzo_medico = input("Inserisci nuovo indirizzo:\n")
            indirizzo_medico_vecchio = input("Inserisci vecchio indirizzo:\n")
            
            DOMANDA_DI_SICUREZZA5 = input("Sei sicuro di voler proseguire?\n").lower()
            
            
            if DOMANDA_DI_SICUREZZA5 == "si":
            
                aggiorna_indirizzo_medico(nuovo_indirizzo_medico,indirizzo_medico_vecchio)
                print("Modifica effettuata")
            else:
                    print("Grazie e arrivederci")
                    
                    
        
        elif dato_da_aggiornare == DATI_MEDICO[6]:
            
            print("Grazie e arrivederci.")
            break
                
            
            
            
            
            
def elimina_medico_w():
    
 
        id_medico = input("Inserisci ID medico:\n")
        password = input("Inserisci password:\n")
        
        user_da_eliminare = cerca_by_id_medico(id_medico)
        print(user_da_eliminare)
        
        DOMANDA_SICUREZZA_2 = input("Sei sicuro di voler continuare?\n").lower()
        
        if DOMANDA_SICUREZZA_2 == "si":
            elimina_medico(id_medico,password)
            print("Eliminazione effettuata con successo")
        else:
             pass
         
         
        
                
                

def prenota():
    
    while True:
        medico_che_prenota = input("Inserisca il suo ID medico:\n")
        user = cerca_by_id_medico(medico_che_prenota)
        if user is None:
            print("ID medico errato")
        else:
            print("Perfetto")
            break
    
    
        
    while True:
        paziente_prenotato = input("Inserisci codice fiscale del paziente:\n")
        user1 = cerca_by_codice_fiscale_paziente(paziente_prenotato)
        if user1 is None:
            print("Codice fiscale errato")
        else:
            print("Perfetto")
            break
        
    
    data_prenotazione = datetime.now()
    data_visita = input("Inserisci data e ora della visita (formato: YYYY-MM-DD HH:MM):\n")
    data_visita_formattata = datetime.strptime(data_visita, "%Y-%m-%d %H:%M")
        
    domanda_note_aggiuntive = input("Vuoi aggiungere un commento?\n").lower()
            
    if domanda_note_aggiuntive == "si":
        note_aggiuntive = input("Scrivi il tuo commento:\n")
    else:
        note_aggiuntive = "Nessun commento"
            
    DOMANDA_CONFERMA1 = input("Vuoi confermare la prenotazione?\n").lower()
    if DOMANDA_CONFERMA1 == "si":
        prenotazione(medico_che_prenota, paziente_prenotato, data_prenotazione, data_visita_formattata, note_aggiuntive)
    else:
        print("Grazie e arrivederci")
            
        
        
    
