import streamlit as st
import pandas as pd
import preprocessor as p, helper as h
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.figure_factory as ff

# Load dataset

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

st.sidebar.title("Olympics Analysis")
st.sidebar.image("data:image/jpeg;base64,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")

df = p.preprocess(df, region_df)

select = st.sidebar.radio(
    'Select an option',
    ('Medal Tally', 'Overall Analysis', 'Country-wise Analysis', 'Athlete-wise Analysis')
)

if select == 'Medal Tally':
    st.header("Medal Tally")
    years, country = h.country_year_list(df)

    selsected_year = st.sidebar.selectbox("Select Year", years)
    selsected_country = st.sidebar.selectbox("Select Country", country)
    


    medal_tally = h.fetch_medal_tally(df, selsected_year, selsected_country)

    if selsected_year == 'Overall' and selsected_country == 'Overall':
        st.title("Overall tally")
    elif selsected_year != 'Overall' and selsected_country == 'Overall':
        st.title("Medel Tally in " + str(selsected_year)+ " Olympics")
    elif selsected_year == 'Overall' and selsected_country != 'Overall':
        st.title("Medel Tally in "+ selsected_country + " overall all Olympics")
    elif selsected_year != 'Overall' and selsected_country != 'Overall':
        st.title(selsected_country+" Medel Tally in"+ str(selsected_year) + " Olympics")

    st.dataframe(medal_tally)



if select == 'Overall Analysis':
    st.title("Top Statistic")
    edition = df['Year'].unique().shape[0] -1
    cities = df['City'].unique().shape[0] - 1
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nation = df['region'].unique().shape[0]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Editions")
        st.title(edition)
    with col2:
        st.header("City")
        st.title(cities)
    with col3:
        st.header("sports")
        st.title(sports)


    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("events")
        st.title(events)
    with col2:
        st.header("athletes")
        st.title(athletes)
    with col3:
        st.header("nation")
        st.title(nation)


    nation_over_time = h.date_over_time(df, 'region')
    fig = px.line(nation_over_time, x="Edition", y="region")
    st.title("Participating Nation Over the Year")
    st.plotly_chart(fig)


    events_over_time = h.date_over_time(df, 'Event')
    fig = px.line(events_over_time, x="Edition", y="Event")
    st.title("Event Over the Year")
    st.plotly_chart(fig)


    Name_over_time = h.date_over_time(df, 'Name')
    fig = px.line(Name_over_time, x="Edition", y="Name")
    st.title("Name Over the Year")
    st.plotly_chart(fig)

    st.title("No. of Events over time (Every Sport)")

    fig, ax = plt.subplots(figsize=(20, 20))

    x = df.drop_duplicates(['Year', 'Sport', 'Event'])

    heatmap_data = x.pivot_table(
    index='Sport',
    columns='Year',
    values='Event',
    aggfunc='count').fillna(0).astype(int)
    sb.heatmap(heatmap_data, annot=True, ax=ax)
    st.pyplot(fig)



    st.title("Most successful Athletes")
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')
    selected_sport = st.selectbox('Select a sport', sport_list)

    x = h.most_successful(df, selected_sport)
    st.table(x)



if select == 'Country-wise Analysis':

    st.sidebar.title("Country-wise Analysis")
    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()

    selected_country = st.sidebar.selectbox("Select a country", country_list)


    df_final = h.yearwise_medal_tally(df, selected_country)

    st.title(selected_country + "country win Medal Tally Over the Years" )

    fig = px.line(df_final, x="Year", y="Medal")
    st.plotly_chart(fig)




    pivote_Table = h.country_event_heatmap(df, selected_country)
    fig, ax = plt.subplots(figsize=(20, 20))
    if pivote_Table.empty:
        st.warning("No athlete data found for " + selected_country)
    else:
        ax = sb.heatmap(pivote_Table, annot=True)
        st.pyplot(fig)



    st.title("Top 10 athletes of "+ selected_country)
    top_atletes_df = h.most_successful_athetes_Country(df, selected_country)
    if top_atletes_df.empty:
        st.warning("No athlete data found for " + selected_country)
    else:
        st.table(top_atletes_df)


if select == 'Athlete-wise Analysis':
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])
    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()

    fig = ff.create_distplot([x1, x2, x3, x4],["Age Distribution", "Gold Medalist", "Silver Medalist", "Bronze Medalist"], show_hist=False, show_rug=False)
    fig.update_layout(autosize = False, width = 1000, height = 600)
    st.title("Distribution of Age")
    st.plotly_chart(fig)



    sports = df['Sport'].value_counts().index.tolist()
    x = []
    name = []

    for sport in sports:
        temp_df = athlete_df[(athlete_df['Sport'] == sport) & (athlete_df['Medal'] == 'Gold')]
        ages = temp_df['Age'].dropna().tolist()
        
        if len(ages) > 1 and len(set(ages)) > 1:  # কমপক্ষে ২টি ভিন্ন value থাকা দরকার
            x.append(ages)
            name.append(sport)
    if len(x) > 0:
        fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
        fig.update_layout(autosize = False, width = 1000, height = 600)
        st.title("Distribution of Age vs sport  (Gold medalist)")
        st.plotly_chart(fig)
    else:
        print("No sport has enough Gold medalists with variable ages for KDE plot.")


    st.title("height vs weight")
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')
    selected_sport = st.selectbox('Select a sport', sport_list)

    temp_df = h.weight_vs_height(df, selected_sport)
    fig, ax = plt.subplots(figsize=(20, 20))
    ax = sb.scatterplot(data=temp_df, x='Weight', y='Height', hue='Medal',style=temp_df['Sex'], s = 50)
    st.pyplot(fig)

    st.title("Men vs women participation over the years")
    final = h.men_vs_women(df)
    fig = px.line(final, x = 'Year', y = ['Male', 'Female'])
    fig.update_layout(autosize = False, width = 1000, height = 600)
    st.plotly_chart(fig)





