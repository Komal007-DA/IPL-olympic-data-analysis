import streamlit as st
import app
import ipl_app


def main():
    st.sidebar.title('Analytical Dashboard')
    st.sidebar.title("Menu")
    options = st.sidebar.selectbox("Choose an option", ["Home", "IPL Data Analysis", "Olympic Data Analysis"])


    if options =="Home":
        st.header("Welcome to Analytical Dashboard")
        # Introduction
        st.write("This dashboard provides analysis and insights into IPL cricket matches and Olympic data.Explore detailed analysis for both IPL and Olympic events.")
        st.write("## IPL Analysis:")
        st.write("1. Provides insights into batsmen's performance, including runs scored, strike rate, boundaries hit, and batting averages.")
        st.write("2. Offers statistics on bowlers' performance, such as wickets taken, economy rates, bowling averages, and bowling variations")
        st.write("3.  Allows users to explore venue-specific statistics, including average scores, pitch conditions, winning trends, and player performances at different venues")
        st.image("https://th.bing.com/th/id/OIP.Ggk9PLPhN_dZ0NlNktQDMwAAAA?rs=1&pid=ImgDetMain",caption="IPL Analysis", use_column_width=True)

        st.write('## Olympic Analysis:')
        st.write("1.  Displays a comprehensive overview of medal standings for various countries across different Olympic events and editions. ")
        st.write("2. Provides insights into overall trends and patterns in Olympic data, including participation trends, medal distributions over time, and dominant countries or sports")
        st.write("3. Allows users to analyze Olympic performance by country, including medal counts, athlete participation, and performance trends over multiple Olympic editions.")
        st.write("4. Enables users to explore individual athlete performances in Olympic events, including medal wins, event participation, and performance statistics.")
        st.image("https://cdn1.neoskosmos.com/uploads/sites/2/2020/04/OLYMPICGAMES.jpg", caption='Olympic Analysis', use_column_width=True)

        st.write("### Note:")
        st.write("Data sorce for both the file are taken from kaggle.")
        st.write("files: - athlete_events.csv",
                        "- noc_regions.csv",
                        "- deliveries.csv",
                        "- matches.csv")


    elif options == "IPL Data Analysis":
        ipl_app.ipl()

    elif options == "Olympic Data Analysis":
        app.olym()


if __name__ == "__main__":
    main()