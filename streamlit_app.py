import streamlit as st
import requests
import time

API_URL = "http://13.62.100.182:8000/resolve"

st.set_page_config(page_title="Agentic IT Support", layout="wide")

# ---------- HEADER ----------
st.markdown("""
# 🧠 Agentic IT Support Automation
AI system that classifies → retrieves → decides → resolves IT issues autonomously.
""")

# ---------- INPUT ----------
ticket = st.text_input("💬 Enter your IT issue", placeholder="e.g. VPN not working")

if st.button("🚀 Resolve Issue"):

    if not ticket:
        st.warning("Please enter a ticket")
        st.stop()

    # ---------- PIPELINE UI ----------
    status_box = st.empty()

    status_box.info("🧠 Classifying issue...")
    time.sleep(0.6)

    status_box.info("🔎 Retrieving policies...")
    time.sleep(0.6)

    status_box.info("⚖️ Making decision...")
    time.sleep(0.6)

    status_box.info("⚙️ Executing resolution...")
    time.sleep(0.6)

    # ---------- API CALL ----------
    try:
        response = requests.post(API_URL, json={"ticket": ticket})
        result = response.json().get("data", {})

    except Exception as e:
        st.error(f"API Error: {e}")
        st.stop()

    status_box.success("✅ Analysis Complete")

    # ---------- LAYOUT ----------
    col1, col2 = st.columns(2)

    # ---------- LEFT PANEL ----------
    with col1:
        st.subheader("🧠 AI Reasoning")

        st.markdown(f"**Category:** {result.get('category')}")
        st.markdown(f"**Confidence:** {result.get('confidence')}")
        st.markdown(f"**Decision:** {result.get('decision')}")

        # Reason
        if result.get("decision") == "resolve":
            st.success("Reason: High confidence + valid policy match")
        else:
            st.error("Reason: High-risk or insufficient context")

        st.divider()

        st.subheader("🔎 Retrieved Knowledge")
        st.code(result.get("context", ""), language="markdown")

    # ---------- RIGHT PANEL ----------
    with col2:
        st.subheader("⚙️ Execution Engine")

        if result.get("decision") == "resolve":
            st.info("🔧 Tool Selected")

            time.sleep(0.5)
            st.warning("⏳ Running automation...")

            time.sleep(1)
            st.success("✅ Tool Execution Completed")

        else:
            st.error("🚨 Escalated to human agent")

        st.divider()

        st.subheader("📤 Final Response")

        response_text = result.get("response")

        if isinstance(response_text, dict):
            st.json(response_text)
        else:
            st.success(response_text)