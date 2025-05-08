import streamlit as st

st.header("🏥 Hospital Triage Expert System")

def triage_system_streamlit():
    st.subheader("Enter Patient Information")

    name = st.text_input("Patient Name")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)

    st.subheader("Select Symptoms (Check all that apply):")
    chest_pain = st.checkbox("Chest Pain")
    short_breath = st.checkbox("Shortness of Breath")
    bleeding = st.checkbox("Heavy Bleeding")
    high_fever = st.checkbox("High Fever")
    injury = st.checkbox("Recent Injury")
    dizziness = st.checkbox("Dizziness or Fainting")
    stomach_pain = st.checkbox("Severe Stomach Pain")

    ask = st.button("Get Triage Result")
    quit = st.button("Quit")

    if ask:
        st.info("🔍 Analyzing symptoms...")

        if bleeding or injury:
            department = "Emergency Room (ER)"
            advice = "🚨 Immediate attention required. Proceed to the ER."
        elif chest_pain or short_breath:
            department = "Cardiology"
            advice = "❤️ Cardiac symptoms detected. Visit Cardiology immediately."
        elif high_fever and age < 12:
            department = "Pediatrics"
            advice = "👶 High fever in child. Visit Pediatrics urgently."
        elif high_fever:
            department = "General Medicine"
            advice = "🩺 Consult a general physician for evaluation."
        elif dizziness:
            department = "Neurology"
            advice = "🧠 Neurological symptoms present. Visit Neurology."
        elif stomach_pain:
            department = "Gastroenterology"
            advice = "🍽️ Visit a gastroenterologist for further diagnosis."
        else:
            department = "Outpatient (OPD)"
            advice = "✅ No critical symptoms. You may proceed to OPD."

        st.subheader("📋 Patient Report")
        st.write(f"**Name:** {name}")
        st.write(f"**Recommended Department:** {department}")
        st.write(f"**Advice:** {advice}")

    if quit:
        st.write("👋 Thank you for using the Hospital Triage Expert System!")

if __name__ == "__main__":
    triage_system_streamlit()
