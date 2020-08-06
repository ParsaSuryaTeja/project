def lead_function(lead_list):
    lead_dict={}
    lead_count={}
    
    if(len(lead_list)>0):
        for lead in range (len(lead_list)):
            if( lead_list[lead].find('@')>-1):
                lead_domainname=lead_list[lead].split('@')[1]
                if(lead_dict.get(lead_domainname)):
                    lead_dict[lead_domainname].append(lead_list[lead]) 
                    
                
                else:
                    lead_dict[lead_domainname]=[lead_list[lead]]     
                
            else:
                print("invalid email id:");
            
            
        for lead_domainname,numberof in lead_dict.items():
            lead_count[lead_domainname]=len(numberof)
        
    print(lead_dict)
    print(lead_count)
    
leads_list= ['hello@dhruvsoft.com','john@dhruvsoft.com','bob@google.com', 'alice@amazon.com','william@salesforce.com', 'jhon@heroku.com','chiru@netsuite.com', 'venky@dhruvsoft.com', 'naveen@zoho.com', 'doe@zoho.com','aws@dhruvsoft.com','rgv@sivio.com','pawan@netsuite.com','welcome@dhruvsoft.com']
lead_function(leads_list)