def triage_system():   #Defines a function named triage_system.
    print("=== Hospital Expert System: Patient Triage Assistant ===")  #Prints a heading for the expert system to the console.

    name = input("Enter Patient Name: ")  #Takes the patient’s name as input.
    age = int(input("Enter Age: "))  #Takes the patient's age and converts it to an integer.
    print("\nSelect Symptoms (Y/N):")  #Prompts the user to answer yes or no to a list of symptoms.
    
    chest_pain = input("Chest Pain? ").lower() == 'y'
    short_breath = input("Shortness of Breath? ").lower() == 'y'
    bleeding = input("Heavy Bleeding? ").lower() == 'y'
    high_fever = input("High Fever? ").lower() == 'y'
    injury = input("Recent Injury? ").lower() == 'y'
    dizziness = input("Dizziness or Fainting? ").lower() == 'y'
    stomach_pain = input("Severe Stomach Pain? ").lower() == 'y'

#Each line collects a 'Y' or 'N' response for a symptom.
#input(...).lower() == 'y' converts the input to lowercase and checks if it's 'y' (yes).

    print("\nAnalyzing symptoms...")

    if bleeding or injury:
        department = "Emergency Room (ER)"
        advice = "Immediate attention required. Proceed to the ER."
    elif chest_pain or short_breath:
        department = "Cardiology"
        advice = "Cardiac symptoms detected. Visit Cardiology immediately."
    elif high_fever and age < 12:
        department = "Pediatrics"
        advice = "High fever in child. Visit Pediatrics urgently."
    elif high_fever:
        department = "General Medicine"
        advice = "Consult a general physician for evaluation."
    elif dizziness:
        department = "Neurology"
        advice = "Neurological symptoms present. Visit Neurology."
    elif stomach_pain:
        department = "Gastroenterology"
        advice = "Visit a gastroenterologist for further diagnosis."
    else:
        department = "Outpatient (OPD)"
        advice = "No critical symptoms. You may proceed to OPD."

#If-elif blocks check the symptoms and assign a department and advice.
#Priority: Emergency > Cardiac > Pediatric > General > Neurology > Gastro > OPD.

    print(f"\n=== Patient Report ===")
    print(f"Name: {name}")
    print(f"Recommended Department: {department}")
    print(f"Advice: {advice}")

#Outputs the recommended department and advice for the user.

if __name__ == "__main__":
    triage_system()
#Ensures the function runs only when the script is directly executed.

# Sample Input:
# Enter Patient Name: Ramesh
# Enter Age: 45
# Select Symptoms (Y/N):
# Chest Pain? y
# Shortness of Breath? n
# Heavy Bleeding? n
# High Fever? n
# Recent Injury? n
# Dizziness or Fainting? n
# Severe Stomach Pain? n

# Sample Output:
# Analyzing symptoms...

# === Patient Report ===
# Name: Ramesh
# Recommended Department: Cardiology
# Advice: Cardiac symptoms detected. Visit Cardiology immediately.