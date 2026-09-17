# Veridian Corp — Internal IT Support Agent (Assignment 2)

An autonomous, audit-compliant internal IT support agent built for Veridian Corp to convert messy employee requests into accurate resolutions, structured tickets, and explicit policy citations.

---

## 🚀 Quick Start / Live Demo

You can interact with the live working prototype without running any code locally:

👉 **[Click Here to Open the Live Agent Prototype](https://8rc4bgacymdicgfaua2el5.streamlit.app/)
---

## 📌 Project Overview

This agent operates in the context of **Monday, 21 September 2026 – Friday, 25 September 2026** and handles incoming IT support requests strictly grounded in official Veridian Corp policies (KB-01 to KB-10 and the Asset Management Policy).

### Key Agent Capabilities:
- **Direct Resolution:** Resolves routine self-service queries immediately (e.g., Guest Wi-Fi kiosk instructions via KB-07).
- **Manual Action Queuing:** Recognizes locked-out accounts (>5 failed attempts) and queues manual unlock tickets for IT admins (KB-01).
- **Security Interception:** Instantly flags and halts the forwarding of suspicious or phishing emails, escalating directly to Security (KB-09).
- **Approval Routing:** Directs hardware, software, and WFH equipment requests through the necessary Finance, IT, or Security approval workflows (KB-03, KB-04, KB-10).
- **Ambiguity Handling:** Requests necessary follow-up details when an employee query is too vague (e.g., "it's not working").
- **Audit Logging:** Logs every interaction into a structured ticket schema (`Ticket ID`, `Timestamp`, `Action Taken`, `Citation Source`, `Status`).

---

## 🛠️ How to Run Locally

If you prefer to run this project on your local machine, follow these simple steps:

### Prerequisites
Make sure you have **Python 3.8+** installed on your system.

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/veridian-it-agent.git](https://github.com/your-username/veridian-it-agent.git)
cd veridian-it-agent
