import streamlit.components.v1 as components
import streamlit as st

st.set_page_config(layout="wide")

def embed_dashboard(dashboard_link):
    tableau_embed_code = f"""
    <div style="overflow: hidden; padding-bottom: 56.25%; position: relative; height: 0;">
        <iframe src="{dashboard_link}?:embed=y&:showVizHome=no&:embed=true" width="100%" height="100%" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;"></iframe>
    </div>
    """

    components.html(tableau_embed_code, height=2500, width=1400)

def main():
    # st.markdown('### Dashboards')
    st.markdown("<h1 style='text-align: center;'>All Dashboards</h1>", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Dashboard 1", "Dashboard 2", "Dashboard 3", "Dashboard 4", "Dashboard 5", "Dashboard 6"])

    with tab1:
        st.header("New Vs Returning")
        embed_dashboard("https://us-west-2b.online.tableau.com/t/spotiidmcc/views/new_and_returning_live_conn/new_vs_returning_dash?:origin=card_share_link&:showVizHome=no&:embed=true")

    with tab2:
        st.header("Miss Rates")
        embed_dashboard("https://us-west-2b.online.tableau.com/t/spotiidmcc/views/miss_dash_live_connection/monthly_miss_rates?:origin=card_share_link&:embed=n")

    with tab3:
        st.header("Shared Things")
        embed_dashboard("https://us-west-2b.online.tableau.com/t/spotiidmcc/views/shared_dash_live_connection/shared_dash?:origin=card_share_link&:embed=n")

    with tab4:
        st.header("Average Order Value")
        embed_dashboard("https://us-west-2b.online.tableau.com/t/spotiidmcc/views/aov_dash_v2_live_conn/aov_dash?:origin=card_share_link&:embed=n")
    
    with tab5:
        st.header("Purchase Frequency")
        embed_dashboard("https://us-west-2b.online.tableau.com/t/spotiidmcc/views/pf_dash_v2_live_connection/pf_dash?:origin=card_share_link&:embed=n")
    
    with tab6:
        st.header("Exception Merchants")
        embed_dashboard("https://us-west-2b.online.tableau.com/t/spotiidmcc/views/exception_merchants/exception_dash?:origin=card_share_link&:embed=n")

    # st.markdown('### Dashboards')

    # tableau_dashboard_link = "https://us-west-2b.online.tableau.com/t/spotiidmcc/views/new_and_returning_live_conn/new_vs_returning_dash?:origin=card_share_link&:showVizHome=no&:embed=true"
    # tableau_embed_code = f"""
    # <iframe src="{tableau_dashboard_link}" width="100%" height="800"></iframe>
    # """
    # components.html(tableau_embed_code, height=800)

if __name__ == "__main__":
    main()
