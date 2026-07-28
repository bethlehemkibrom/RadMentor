
import streamlit as st

def metric_cards(total_cases, modalities, body_systems, pending):

    c1, c2, c3, c4 = st.columns(4)

    cards = [
        ("Cases", total_cases),
        ("Modalities", modalities),
        ("Body Systems", body_systems),
        ("Pending Review", pending),
    ]

    for col, (title, value) in zip([c1, c2, c3, c4], cards):

        with col:

            st.markdown(
                f"""
                <div style="
                    background:#ffffff;
                    border-radius:20px;
                    padding:24px;
                    border:1px solid #E5E7EB;
                    box-shadow:0 8px 24px rgba(0,0,0,.08);
                    text-align:center;
                    transition:0.3s;
                ">

                    <div style="
                        color:#64748B;
                        font-size:14px;
                        letter-spacing:.5px;
                        text-transform:uppercase;
                    ">
                        {title}
                    </div>

                    <div style="
                        margin-top:12px;
                        font-size:42px;
                        font-weight:700;
                        color:#1E3A8A;
                    ">
                        {value}
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )
