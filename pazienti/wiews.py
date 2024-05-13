# -Registrazione di nuovi pazienti.
# -Visualizzazione delle informazioni dei pazienti esistenti.
# -Aggiornamento dei dati dei pazienti.
# -Cancellazione di record dei pazienti (se necessario).




from pazienti.database import salva_paziente,cerca_by_codice_fiscale_paziente,visualizza_paziente,elimina_paziente,cerca_paziente_da_eliminare,aggiorna_nome_paziente,aggiorna_indirizzo,aggiora_numero,aggiorna_email,aggiorna_password


from datetime import datetime


def registra_paziente():
    codice_fiscale = input("Inserisci codice fiscale:\n").upper()
    nome_pazienti_completo = input("Inserisci nome completo (Nome e Cognome):\n") 
    data_di_nascita = input("Inserisci data di nascita (formato: YYYY-MM-DD):\n")
    data_di_nascita_formatata = datetime.strptime(data_di_nascita, '%Y-%m-%d')
    genere = input("Inserisci genere (Maschio - Femmina):\n").upper()
    indirizzo = input("Inserisci indirizzo (Via xxxx, civico):\n")
    numero_di_telefono = int(input("Inserisci numero di telefono (+** 1234567891):\n"))
    email = input("Inserisci email (********04@*****.***):\n")
    password = input("Inserisci password:\n")

    salva_paziente(codice_fiscale, nome_pazienti_completo, data_di_nascita_formatata, genere, indirizzo, numero_di_telefono, email, password)
    print("Registrazione eseguita")
    

    
    
    
    
    
    
def login_paziente():
    while True:
        codice_fiscale = input("Inserisci codice fiscale:\n")
        user = cerca_by_codice_fiscale_paziente(codice_fiscale)
        if user is None:
            print("Codice fiscale errato")
        else:
            print("Perfetto")
            break

    while True: 
        password = input("Inserisci password:\n")
        if user is not None and password == user["password"]:
            print("Perfetto")
            break
        else:
            print("Password errata")
    
 
 
 
 
 
def azioni_by_tipo_utente_paziente():
    while True:
        OPERAZIONI_PAZIENTE_1 = ("registra" ,"login",)
        print(OPERAZIONI_PAZIENTE_1)
        azione1 = input("Cosa vuoi fare?\n").lower()
        
        if azione1 == OPERAZIONI_PAZIENTE_1[0]:
                registra_paziente()
                print("Registrazione eseguita con successo!!")
                break
        elif azione1 == OPERAZIONI_PAZIENTE_1[1]:
                login_paziente()
                break
                
          
       
       
       
       
       
       
       
            
def visualizza():
    while True:
        codice_fiscale1 = input("Inserisci codice fiscale:\n")
        user = cerca_by_codice_fiscale_paziente(codice_fiscale1)
        if user is None:
            print("Codice fiscale errato")
        else:
            print("Perfetto")
            break

    while True: 
        password = input("Inserisci password:\n")
        if user is not None and password == user["password"]:
            print("Perfetto")
            codice_fiscale = codice_fiscale1
            print(visualizza_paziente(codice_fiscale))
            break
        else:
            print("Password errata")
            
    
            
    



def elimina_paziente_w():
    DOMANDA_SICUREZZA = input("Sei sicuro di voler continuare?\n").lower()
    
    if DOMANDA_SICUREZZA == "si":
          
        codice_fiscale = input("Inserisci codice fiscale:\n")
        password = input("Inserisci password \n")
        
        user_da_eliminare = cerca_paziente_da_eliminare(codice_fiscale,password)
        print(user_da_eliminare)
        
        DOMANDA_SICUREZZA_2 = input("Sei ancora sicuro di voler continuare?\n").lower()
        
        if DOMANDA_SICUREZZA_2 == "si":
            elimina_paziente(codice_fiscale,password)
        else:
             print("Grazie e arrivederci.")





def aggiorna_paziente():
    DOMANDA_CONFERMA = input("Sono questi i dati che vuoi modificare?\n").lower()
        
    if DOMANDA_CONFERMA == "si":
        while True:
       
            LISTA_DATI = ("nome paziente" , "indirizzo", "numero di telefono", "email", "password","nessuno")
            print(LISTA_DATI)
            DATI_DA_MODIFICARE = input("Quale dato vuoi modificare modificare?\n").lower()
                            
            if DATI_DA_MODIFICARE == LISTA_DATI[0]:
                
                nome_paziente_nuovo = input("Inserisci nuovo nome completo (nome e cognome):\n")
                nome_vecchio_paziente = input("Inserisci vecchio nome completo (nome e cognome):\n")
                                    
                DOMANDA_SICUREZZA1 = input("Sei sicuro di voler continuare?\n").lower()
                                    
                if DOMANDA_SICUREZZA1 == "si":
                    aggiorna_nome_paziente(nome_paziente_nuovo,nome_vecchio_paziente)
                    print("Modifica effettuata!!")
                else:
                    print("Grazie e arrivederci.")
                
        
            elif DATI_DA_MODIFICARE == LISTA_DATI[1]:
                
                indirizzo_nuovo = input("Inserisci nuovo indirizzo (Via liberazione 24):\n")
                indirizzo_vecchio= input("Inserisci vecchio indirizzo (Via liberazione 24):\n")
                                
                DOMANDA_SICUREZZA2 = input("Sei sicuro di voler continuare?\n").lower()
                                
                if DOMANDA_SICUREZZA2 == "si":
                    aggiorna_indirizzo(indirizzo_nuovo,indirizzo_vecchio)
                    print("Modifica effettuata!!")
                    
                else:
                    print("Grazie e arrivederci.")
                                            
                                                                      
            elif DATI_DA_MODIFICARE == LISTA_DATI[2]:
                
                numero_telefono_nuovo = input("Inserisci nuovo numero di telefono (+391234567891):\n")
                numero_telefono_vecchio= input("Inserisci vecchio numero di telefono (+391234567891):\n")
                                    
                DOMANDA_SICUREZZA3 = input("Sei sicuro di voler continuare?\n").lower()
                                
                if DOMANDA_SICUREZZA3 == "si":
                    aggiora_numero(numero_telefono_nuovo,numero_telefono_vecchio)
                    print("Modifica effettuata!!")
                    
                else:
                    print("Grazie e arrivederci.")
                                
                            
                        
            elif DATI_DA_MODIFICARE == LISTA_DATI[3]:
                
                email_nuovo = input("Inserisci nuova email (xxxxxxx04@example.com):\n")
                email_vecchio= input("Inserisci vecchia email (xxxxxxx04@example.com):\n")
                                
                DOMANDA_SICUREZZA4 = input("Sei sicuro di voler continuare?\n").lower()
                                
                if DOMANDA_SICUREZZA4 == "si":
                    aggiorna_email(email_nuovo,email_vecchio)
                    print("Modifica effettuata!!")
                    
                else:
                    print("Grazie e arrivederci.")
                            
                        
                        
            elif DATI_DA_MODIFICARE == LISTA_DATI[4]:
                
                password_nuovo = input("Inserisci nuova password (jfskkji1234.) :\n")
                password_vecchio= input("Inserisci vecchia password (jfskkji1234.):\n")
                                
                DOMANDA_SICUREZZA4 = input("Sei sicuro di voler continuare?\n").lower()
                                
                if DOMANDA_SICUREZZA4 == "si":
                    aggiorna_password(password_nuovo,password_vecchio)
                    print("Modifica effettuata!!")
                   
                else:
                    print("Grazie e arrivederci.")
                
            elif DATI_DA_MODIFICARE == LISTA_DATI[5]:
                
                print("Grazie e arrivederci")
                break
                    
                
            
                                        
                                            
                    

            
            