diseases={
    "flu":{"fever","cough","body_aches","weakness"},
    "cold":{"runny nose","headache","sore throat","cough","sneezing"},
    "covid19":{"loss of taste and smell","fever","shortness of breadth","sore throat"},
    "malaria":{"fever","chills","weakness","nausea"}
}

symptom_ques=["fever","sore_throat","cough","shortness of breadth","runny nose ","loss of taste and smell","headache","weakness","chills","nausea"]

def diagnose():
    print("\nWelcome to  Expert systme")
    print("\n answer foloowing questiosn for diagnose")
    user_symp=set()
    for symp in symptom_ques:
        ans=input(f"Do you have {symp} (yes/no)").lower()
        if ans=='yes':
            user_symp.add(symp)
    match_dis=[]
    for disease,symp in diseases.items():
            match_count=len(user_symp & symp)
            if match_count>=2:
                match_dis.append((disease,match_count))
    if match_dis:
            match_dis.sort(key=lambda x:x[1], reverse =True)
            print("\n Based on your sympotoms you may have ")
            for disease, _ in match_dis:
                print(f"{disease}")
    else:
            print("your symtoms not matched conault the doctor")
if __name__=="__main__":
    diagnose()



