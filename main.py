#PYTHON OSPEDALE

from pazienti.wiews import azioni_by_tipo_utente_paziente,visualizza,elimina_paziente_w,aggiorna_paziente





from medici.wiews import azioni_by_tipo_utente_medico,visualizza_medico,aggiorna_datimedico,elimina_medico_w,prenota_paziente






while True:
    tipo_utente = input("Salve sei un medico o un paziente?\n")
    
    
    
    
    if tipo_utente == "paziente":
        azioni_by_tipo_utente_paziente()
        
    
        OPERAZIONI_PAZIENTE = ("visualizza","aggiorna","elimina")
        print(OPERAZIONI_PAZIENTE)
        
        
        domanda_operazione_paziente = input("Quale operazione vuoi eseguire?\n").lower()
            
        
        
    
        if domanda_operazione_paziente == OPERAZIONI_PAZIENTE[0]:
                visualizza()
                
                
                
                
                
        elif domanda_operazione_paziente == OPERAZIONI_PAZIENTE[1]:
                visualizza()
                aggiorna_paziente()
                
                
                
                
                
        elif domanda_operazione_paziente == OPERAZIONI_PAZIENTE[2]:
                elimina_paziente_w()
                print("Perfetto operazione eseguita!!")
                
                
                    
        else:
                print("Operazione non valida.")  
        
        
        
        
        
        
        
        
        
        
    elif tipo_utente == "medico":
        azioni_by_tipo_utente_medico()




        OPERAZIONI_MEDICO = ("visualizza","aggiorna","elimina","prenota","ricetta")
        print(OPERAZIONI_MEDICO)
    
    
    
    
        domanda_operazione_medico = input("Quale operazione vuoi eseguire?\n").lower()
        
        
        
        if domanda_operazione_medico == OPERAZIONI_MEDICO[0]:
                visualizza_medico()
        
        elif domanda_operazione_medico == OPERAZIONI_MEDICO[1]:
                aggiorna_datimedico()
                
        
        elif domanda_operazione_medico == OPERAZIONI_MEDICO[2]:
                elimina_medico_w()
                

        elif domanda_operazione_medico == OPERAZIONI_MEDICO[3]:
                prenota_paziente()
   


         
        
    