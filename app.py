import datetime
import streamlit as st

# Streamlit Interface Setup
st.set_page_config(page_title="Veridian Corp IT Agent", layout="wide")
st.title("Veridian Corp — Internal IT Support Agent")
st.caption("Operating Context: Sept 21–25, 2026 | Grounded on KB-01 to KB-10")

if "tickets" not in st.session_state:
    st.session_state.tickets = []

user_query = st.text_area(
    "How can IT help you today?",
    placeholder="e.g., I'm locked out of my account after 6 attempts...",
)
employee_email = st.text_input(
    "Employee Email:", "employee@veridian-corp.example"
)


def run_agent_logic(query, email):
    time_now = datetime.datetime.now().strftime("2026-09-21 %H:%M:%S")
    q = query.lower()

    # Policy Routing Engine
    if "phishing" in q or "forwarding" in q or "suspicious" in q:
        action = (
            "CRITICAL BLOCK: Stop forwarding email immediately. Alerting"
            " security@veridian-corp.example."
        )
        source = "KB-09: Security Incident Reporting"
        status = "Escalated to Security"
    elif "guest" in q and ("wifi" in q or "wi-fi" in q):
        action = (
            "RESOLVED: Generate 24-hour guest Wi-Fi credentials directly at the"
            " front-desk kiosk."
        )
        source = "KB-07: Guest Wi-Fi Access"
        status = "Resolved (Self-Service)"
    elif "locked out" in q or "password" in q or "attempts" in q:
        action = (
            "ACTION QUEUED: Account locked (>5 attempts). Manual unlock ticket"
            " created for IT."
        )
        source = "KB-01: Password Reset"
        status = "In Progress (Manual Unlock Needed)"
    elif "laptop" in q and ("dead" in q or "replace" in q or "broken" in q):
        action = (
            "ELIGIBLE: Laptop meets 3-year threshold (or verified hardware"
            " failure). Replacement ticket logged."
        )
        source = "KB-03 & Asset Management Policy"
        status = "Pending Fulfillment"
    elif len(query.strip().split()) < 4:
        action = (
            "CLARIFICATION NEEDED: Please provide specific details about the"
            " device, app, or error message."
        )
        source = "Agent Ambiguity Guardrail"
        status = "Waiting on Employee Response"
    else:
        action = (
            "LOGGED: Ticket received and routed to standard IT support queue."
        )
        source = "General IT Policy / Knowledge Base"
        status = "Open Ticket"

    ticket = {
        "Ticket ID": f"TK-{hash(time_now) % 10000}",
        "Date": time_now,
        "Employee": email,
        "Issue Summary": query,
        "Agent Decision & Next Steps": action,
        "Policy Source": source,
        "Status": status,
    }
    st.session_state.tickets.append(ticket)
    return ticket


if st.button("Submit Request"):
    if user_query:
        res = run_agent_logic(user_query, employee_email)
        st.success(f"Status: {res['Status']}")
        st.write(
            f"**Action/Resolution:** {res['Agent Decision & Next Steps']}"
        )
        st.info(f"**Source Cited:** {res['Policy Source']}")
    else:
        st.warning("Please enter a request.")

st.divider()
st.subheader("Audit Trail & Ticket Queue")
if st.session_state.tickets:
    st.table(st.session_state.tickets)
