import streamlit as st

st.set_page_config(
    page_title="DisasterSafe AI",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ DisasterSafe AI")
st.subheader("Natural Disaster Risk Awareness")
st.warning(
    "Student prototype only. This version uses simple example rules, not a trained AI model "
    "or live official disaster data. Do not use it for real emergency decisions."
)

st.write(
    "Enter a location and some conditions to see an example risk assessment and safety guidance."
)

location = st.text_input("Your location (district, sector, or village)", placeholder="e.g. Nyabihu District")

hazard = st.selectbox(
    "Which hazard do you want to check?",
    ["Flood", "Landslide", "Drought", "Strong storm"]
)

st.markdown("### Conditions")
if hazard == "Flood":
    rainfall = st.slider("Recent or forecast rainfall (example scale, mm)", 0, 200, 40)
    near_water = st.selectbox("Is the area near a river or flood-prone lowland?", ["Not sure", "No", "Yes"])
    recent_flood = st.selectbox("Has flooding been reported nearby?", ["Not sure", "No", "Yes"])

    score = 0
    if rainfall >= 100:
        score += 2
    elif rainfall >= 50:
        score += 1
    if near_water == "Yes":
        score += 1
    if recent_flood == "Yes":
        score += 2

    if score >= 4:
        risk = "High (example rule-based result)"
        advice = [
            "Check official alerts and follow local authorities' instructions.",
            "Stay away from floodwater and flooded roads.",
            "If authorities advise evacuation, use their verified route and destination."
        ]
    elif score >= 2:
        risk = "Moderate (example rule-based result)"
        advice = [
            "Monitor official weather and disaster updates.",
            "Avoid riverbanks and low-lying areas if water levels are rising.",
            "Prepare essential items in case authorities advise moving."
        ]
    else:
        risk = "Lower based on entered answers (not a safety guarantee)"
        advice = [
            "Continue monitoring official alerts.",
            "Remember that local flooding can occur even when rainfall seems limited."
        ]

elif hazard == "Landslide":
    rainfall = st.slider("Recent or forecast rainfall (example scale, mm)", 0, 200, 40)
    steep_slope = st.selectbox("Is the area on or below a steep slope?", ["Not sure", "No", "Yes"])
    ground_signs = st.selectbox("Are there official reports or visible warning signs of slope movement?", ["Not sure", "No", "Yes"])

    score = 0
    if rainfall >= 100:
        score += 2
    elif rainfall >= 50:
        score += 1
    if steep_slope == "Yes":
        score += 1
    if ground_signs == "Yes":
        score += 2

    if score >= 4:
        risk = "High concern (example rule-based result)"
        advice = [
            "Move away from the affected slope if it is safe to do so.",
            "Follow official evacuation instructions immediately.",
            "Report warning signs to local authorities; do not approach an unstable slope."
        ]
    elif score >= 2:
        risk = "Moderate concern (example rule-based result)"
        advice = [
            "Monitor official warnings and local conditions.",
            "Take reports of cracks, leaning trees, or unusual ground movement seriously.",
            "Follow local authority guidance about moving to a safer place."
        ]
    else:
        risk = "Lower based on entered answers (not a safety guarantee)"
        advice = [
            "Keep following official alerts, especially during heavy rain.",
            "This simple form cannot determine whether a slope is stable."
        ]

elif hazard == "Drought":
    dry_period = st.selectbox("Has the area had a prolonged dry period?", ["Not sure", "No", "Yes"])
    water_shortage = st.selectbox("Are water sources or crops showing signs of shortage?", ["Not sure", "No", "Yes"])

    score = (2 if dry_period == "Yes" else 0) + (2 if water_shortage == "Yes" else 0)
    if score >= 3:
        risk = "High concern (example rule-based result)"
        advice = [
            "Check official drought and water-supply updates.",
            "Use water carefully and follow local public-health advice.",
            "Seek guidance from local authorities or agricultural services."
        ]
    elif score >= 2:
        risk = "Moderate concern (example rule-based result)"
        advice = [
            "Monitor water availability and official updates.",
            "Follow locally recommended water-conservation guidance."
        ]
    else:
        risk = "Insufficient evidence for a higher concern from these answers"
        advice = [
            "Continue monitoring rainfall, water availability, and official updates."
        ]

else:
    severe_weather = st.selectbox("Is an official severe-weather warning active?", ["Not sure", "No", "Yes"])
    strong_winds = st.selectbox("Are strong winds or damaging storm conditions being reported?", ["Not sure", "No", "Yes"])

    score = (3 if severe_weather == "Yes" else 0) + (1 if strong_winds == "Yes" else 0)
    if score >= 3:
        risk = "High concern (example rule-based result)"
        advice = [
            "Follow official weather warnings and emergency instructions.",
            "Stay indoors away from windows if advised and avoid exposed areas.",
            "Do not approach fallen power lines or damaged structures."
        ]
    elif score >= 1:
        risk = "Moderate concern (example rule-based result)"
        advice = [
            "Monitor official weather updates.",
            "Secure loose outdoor items only if it is safe to do so.",
            "Follow local authorities' advice."
        ]
    else:
        risk = "No strong warning indicated by these answers (not a safety guarantee)"
        advice = [
            "Keep monitoring official forecasts and alerts."
        ]

if st.button("Assess example risk", type="primary"):
    if not location.strip():
        st.error("Please enter your location first.")
    else:
        st.markdown("---")
        st.markdown("### Example assessment")
        st.write(f"**Location entered:** {location}")
        st.write(f"**Hazard selected:** {hazard}")
        st.info(risk)
        st.markdown("### Suggested safety steps")
        for item in advice:
            st.write(f"- {item}")
        st.caption(
            "This result is generated from simple demonstration rules and user-entered answers. "
            "It is not a forecast, verified risk score, or official warning."
        )

st.markdown("---")
st.markdown("### Emergency reminder")
st.write(
    "If you believe you are in immediate danger, contact local emergency services and follow "
    "official instructions. Do not rely on this student prototype to choose an evacuation route."
)
