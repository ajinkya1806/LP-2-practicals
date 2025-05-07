import time
import random

# Function to get user symptoms
def get_symptoms():
    print("\nPlease answer the following questions (yes/no):\n")
    symptoms = []
    questions = {
        "fever": "Do you have a fever?",
        "cough": "Are you experiencing a cough?",
        "headache": "Do you have a headache?",
        "sore_throat": "Do you have a sore throat?",
        "runny_nose": "Do you have a runny nose?",
        "fatigue": "Are you feeling tired?",
    }
    for symptom, question in questions.items():
        ans = input(f"{question} ").strip().lower()
        if ans == "yes":
            symptoms.append(symptom)
    return symptoms

# Diagnosis using if-else
def diagnose(symptoms):
    s = set(symptoms)
    if "fever" in s and "cough" in s and "fatigue" in s:
        return "Flu", "Rest well, drink fluids, and consult a doctor if needed."
    elif "cough" in s and "sore_throat" in s and "runny_nose" in s:
        return "Common Cold", "Rest, stay warm, and drink plenty of fluids."
    elif "fever" in s and "headache" in s and "fatigue" in s:
        return "Dengue", "Consult a doctor immediately. Avoid painkillers like ibuprofen."
    else:
        return "Unknown", "Symptoms unclear. Please consult a healthcare professional."

# Main function
def main():
    print("=" * 50)
    print("\033[1;92m     Welcome to the Medical Expert System\033[0m")
    print("=" * 50)
    time.sleep(1)

    symptoms = get_symptoms()

    print("\nAnalyzing your symptoms...")
    time.sleep(2)

    disease, advice = diagnose(symptoms)

    print("\n" + "-" * 50)
    print(f"Diagnosis Result : {disease}")
    print(f"Recommendation   : {advice}")
    print("-" * 50)

    # Health tip
    tips = [
        "Tip: Stay hydrated and drink clean water.",
        "Tip: Wash your hands regularly.",
        "Tip: Get enough sleep every night.",
        "Tip: Avoid self-medication.",
    ]
    print(random.choice(tips))
    print("=" * 50)
    print("\033[1;91mNote: This system is not a substitute for professional medical advice.\033[0m")
    print("=" * 50)

if __name__ == "__main__":
    main()
