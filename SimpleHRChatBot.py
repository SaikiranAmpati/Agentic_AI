import streamlit as st

st.set_page_config(page_title="Simple HR Chatbot", page_icon="💼")
st.title("Simple HR Chatbot")
st.caption("Ask common HR questions like leave, payroll, or benefits.")

HR_ANSWERS = {
    "leave": "You can request leave in the HR portal under Time Off. Annual leave is 20 days, sick leave is 12 days, and casual leave is 6 days per year.",
    "pto": "Paid time off is requested in the HR portal. Managers usually approve requests within 2 business days.",
    "payroll": "Payroll runs on the last working day of each month. For pay-slip questions, email payroll@company.com.",
    "salary": "Salary is credited on the last working day of each month. Use the payroll portal to download payslips.",
    "benefits": "Benefits include health insurance, wellness allowance, and a retirement plan. Details are in the Benefits handbook on the intranet.",
    "insurance": "Health insurance covers employees and dependents. Raise a ticket with HR Benefits to add or remove a dependent.",
    "onboarding": "New hires complete paperwork on day 1, laptop setup with IT, and a 30-day onboarding plan with their manager.",
    "policy": "Company policies are on the intranet under HR > Policies. Contact hr@company.com if you cannot find a document.",
    "wfh": "Work from home is allowed up to 2 days per week with manager approval. Mark WFH in the attendance system.",
    "remote": "Remote or hybrid work follows your team's policy. Ask your manager, then update your work location in the HR portal.",
}


def answer_hr_question(question: str) -> str:
    text = question.lower()
    for keyword, reply in HR_ANSWERS.items():
        if keyword in text:
            return reply
    return (
        "I can help with leave, payroll, salary, benefits, insurance, "
        "onboarding, policy, and work-from-home. Try asking one of those."
    )


if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I am the HR assistant. How can I help you today?"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Ask an HR question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    reply = answer_hr_question(prompt)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
