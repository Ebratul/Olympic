import numpy as np

def medal_tally(df):
    medal_df = df.drop_duplicates(
        subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal']
    )

    medal_tally = medal_df.groupby('region')[['Gold', 'Silver', 'Bronze']].sum().reset_index()
    medal_tally = medal_tally.sort_values('Gold', ascending=False)

    medal_tally['Total'] = medal_tally['Gold'] + medal_tally['Silver'] + medal_tally['Bronze']

    return medal_tally.astype({
        'Gold': 'int',
        'Silver': 'int',
        'Bronze': 'int',
        'Total': 'int'
    })


def country_year_list(df):
    years = sorted(df['Year'].unique().tolist())
    years.insert(0, 'Overall')

    countries = sorted(df['region'].dropna().unique().tolist())
    countries.insert(0, 'Overall')

    return years, countries


def fetch_medal_tally(df, year, country):
    medal_df = df.drop_duplicates(
        subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal']
    )

    flag = False

    if year == 'Overall' and country == 'Overall':
        temp_df = medal_df

    elif year == 'Overall' and country != 'Overall':
        flag = True
        temp_df = medal_df[medal_df['region'] == country]

    elif year != 'Overall' and country == 'Overall':
        temp_df = medal_df[medal_df['Year'] == year]

    else:
        temp_df = medal_df[(medal_df['Year'] == year) & (medal_df['region'] == country)]

    if flag:
        x = temp_df.groupby('Year')[['Gold', 'Silver', 'Bronze']].sum().reset_index()
    else:
        x = temp_df.groupby('region')[['Gold', 'Silver', 'Bronze']].sum().reset_index()

    x['Total'] = x['Gold'] + x['Silver'] + x['Bronze']

    x = x.astype({
        'Gold': 'int',
        'Silver': 'int',
        'Bronze': 'int',
        'Total': 'int'
    })

    return x


def date_over_time(df, col):
    nation_over_time = df.drop_duplicates(['Year', col])['Year'].value_counts().reset_index().sort_values('Year')
    nation_over_time.rename(columns={
    'Year': 'Edition',
    'count': col
    }, inplace=True)
    return nation_over_time


def most_successful(df, Sport):
    temp_df = df.dropna(subset=['Medal'])
    if Sport != 'Overall':
        temp_df = temp_df[temp_df['Sport'] == Sport]
    x = temp_df['Name'].value_counts().reset_index().head(10).merge(df, left_on = 'Name', right_on = 'Name', how = 'left')[['Name', 'count', 'Sport', 'region']].drop_duplicates('Name')
    x.rename(columns= {'count':'Medals'}, inplace= True)
    return x





def yearwise_medal_tally(df, country):

    temp_df = df.dropna(subset=['Medal'])
    temp_df.drop_duplicates(subset=['Team', 'NOC','Games', 'Year', 'City', 'Sport', 'Event', 'Medal'], inplace=True)

    new_df = df[df['region'] == country]
    final_df = new_df.groupby('Year').count()['Medal'].reset_index()
    return final_df






def country_event_heatmap(df, country):
    temp_df = df.dropna(subset=['Medal'])
    temp_df.drop_duplicates(subset=['Team', 'NOC','Games', 'Year', 'City', 'Sport', 'Event', 'Medal'], inplace=True)
    new_df = temp_df[temp_df['region'] == country]
    pivote_Table = new_df.pivot_table(index='Sport', columns='Year', values= 'Medal', aggfunc= 'count').fillna(0)
    return pivote_Table


def most_successful_athetes_Country(df, country):
  temp_df = df.dropna(subset=['Medal'])
  if country != 'Overall':
    temp_df = temp_df[temp_df['region'] == country]
  x = temp_df['Name'].value_counts().reset_index().head(10).merge(df, left_on = 'Name', right_on = 'Name', how = 'left')[['Name', 'count', 'Sport']].drop_duplicates('Name')
  x.rename(columns= {'count':'Medals'}, inplace= True)
  return x





def weight_vs_height(df, sport):
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])
    athlete_df['Medal'].fillna('No Medal', inplace=True)
    if sport != 'Overall':
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        return temp_df
    else:
        return athlete_df
    

def men_vs_women(df):
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])
    men = athlete_df[athlete_df['Sex'] == 'M'].groupby('Year').count()['Name'].reset_index()
    women = athlete_df[athlete_df['Sex'] == 'F'].groupby('Year').count()['Name'].reset_index()
    final = men.merge(women, on = 'Year', how= 'right')
    final.rename(
    columns = {
        'Name_x': 'Male',
        'Name_y': 'Female'
    },
    inplace = True
    )
    final.fillna(0, inplace=True)
    return final


