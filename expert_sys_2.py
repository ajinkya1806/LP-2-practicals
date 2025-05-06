def ask_questions(question:str)->bool:
    response=input(question+"(yes/no):").lower().strip()
    return response.startswith("y")

def diagnose_allergies()->bool:
    return ask_questions("Are you having red, watery eyes?") or ask_questions("Do you have itching/swelling?")

def diagnose_fever()->bool:
    return ask_questions("Are you having temperature 37.5C?") or ask_questions("Are you having chills?")

def diagnose_cold()->bool:
    return ask_questions("Do you have runny nose?") or ask_questions("Are you sneezing frequently?")

def diagnose_flu()->bool:
    return ask_questions("Are you having temperature above 38C?") and ask_questions("Are you feeling tired?") and ask_questions("Do you have body aches?")

def diagnose_foodpoisoning()->bool:
    return ask_questions("Do you have diarrhea?") and ask_questions("Are you vomiting?") and ask_questions("Do you feel nauseous?")

def diagnose_strepthroat()->bool:
    return ask_questions("Do you have swollen tonsils?") and ask_questions("Do you have a sore throat?")

def diagnose_appendictis()->bool:
    return ask_questions("Do you have severe stomach pain?") and ask_questions("Are you having loss of appetite?")

print("===Expert System for Diagnosing Ailments===")

diagnoses=[]

if diagnose_allergies():
    diagnoses.append("Allergies")

if diagnose_fever():
    diagnoses.append("Fever")

if diagnose_cold():
    diagnoses.append("Cold")

if diagnose_flu():
    diagnoses.append("Flu")

if diagnose_strepthroat():
    diagnoses.append("Strep Throat")

if diagnose_foodpoisoning():
    diagnoses.append("Food Poisoning")

if diagnose_appendictis():
    diagnoses.append("Appendictis")

print("===Diagnoses Summary====")

if diagnoses:
    for illness in diagnoses:
        print(f"You may have :{illness}")
else:
    print("No diagnoses found")