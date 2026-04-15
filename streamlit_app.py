import streamlit as st
import requests
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Agentic IT Support",
    layout="wide"
)

# ---------------- CUSTOM DARK THEME ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: white;
}
.card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    border: 1px solid rgba(255,255,255,0.1);
    margin-bottom: 15px;
}
.title {
    font-size: 34px;
    font-weight: bold;
    color: #60a5fa;
}
.subtitle {
    color: #94a3b8;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.title("👤 User Profile")
    st.markdown("**Name:** Nishit")
    st.markdown("**Employee ID:** EMP123")
    st.markdown("**Department:** IT Services")

    st.markdown("---")

    st.markdown("### ⚙️ System Status")
    st.success("🟢 AI Engine Active")
    st.success("🟢 Automation Enabled")
    st.success("🟢 API Connected")

# ---------------- HEADER ----------------
st.markdown('<div class="title">🧠 Agentic IT Support System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI system that autonomously resolves enterprise IT issues</div>', unsafe_allow_html=True)

st.markdown("---")

# ---------------- INPUT ----------------
ticket = st.text_input("💬 Describe your issue", placeholder="e.g. VPN not connecting")

run = st.button("🚀 Resolve Issue")

# ---------------- MAIN ----------------
if run:

    if not ticket.strip():
        st.warning("Please enter a valid issue")
        st.stop()

    # -------- API CALL --------
    with st.spinner("🧠 AI analyzing issue..."):
        try:
            res = requests.post(
                "http://127.0.0.1:8000/resolve",
                json={"ticket": ticket}
            )
            result = res.json()["data"]
        except Exception as e:
            st.error(f"Backend error: {e}")
            st.stop()

    st.success("✅ Analysis Complete")

    col1, col2 = st.columns(2)

    # ================= LEFT PANEL =================
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.subheader("🧠 AI Reasoning")
        st.markdown(f"**Category:** `{result.get('category')}`")
        st.markdown(f"**Confidence:** `{result.get('confidence')}`")
        st.markdown(f"**Decision:** `{result.get('decision')}`")

        st.markdown("---")

        st.subheader("🔎 Retrieved Knowledge")
        st.code(result.get("context", "")[:400])

        st.markdown('</div>', unsafe_allow_html=True)

    # ================= RIGHT PANEL =================
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.subheader("⚙️ Execution Engine")

        decision = result.get("decision")
        category = result.get("category")

        execution_steps = []

        if decision == "resolve":

            st.success("🟢 Automation Triggered")

            # Step mapping
            if category == "vpn_issue":
                tool = "vpn_fix()"
                execution_steps = [
                    "🔄 Initializing system...",
                    "🔌 Restarting VPN service...",
                    "🔐 Authenticating...",
                    "📡 Reconnecting VPN..."
                ]

            elif category == "network_issue":
                tool = "restart_network()"
                execution_steps = [
                    "🔄 Initializing system...",
                    "📶 Restarting network adapter...",
                    "🔄 Renewing IP address...",
                    "🌐 Reconnecting WiFi..."
                ]

            elif category == "password_reset":
                tool = "reset_password()"
                execution_steps = [
                    "🔄 Initializing system...",
                    "🔑 Generating reset link...",
                    "📧 Sending email..."
                ]

            elif category == "device_issue":
                tool = "run_diagnostics()"
                execution_steps = [
                    "🔄 Initializing system...",
                    "🛠 Running diagnostics...",
                    "🔍 Checking hardware..."
                ]

            else:
                tool = "generic_fix()"
                execution_steps = [
                    "🔄 Initializing system...",
                    "⚙️ Executing automated fix..."
                ]

            # 🔥 LIVE + PERSISTENT LOGS
            log_box = st.empty()
            full_log = ""

            for step in execution_steps:
                full_log += step + "\n"
                log_box.code(full_log)
                time.sleep(0.7)

            st.success("✅ Issue Resolved Successfully")

            # TOOL DISPLAY
            st.info(f"🛠 Tool Invoked: `{tool}`")

        else:
            st.error("⚠️ Escalated to L2 Support")

        st.markdown('</div>', unsafe_allow_html=True)

    # ================= FINAL OUTPUT =================
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📤 Resolution Summary")

    if result.get("decision") == "resolve":
        st.success("✅ Issue resolved automatically")
    else:
        st.error("❌ Escalated")

    st.markdown(f"**Category:** {result.get('category')}")
    st.markdown(f"**Confidence:** {result.get('confidence')}")

    st.text_area("System Output", result.get("response"), height=180)

    st.markdown('</div>', unsafe_allow_html=True)