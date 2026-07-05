import pandas as pd
import plotly.express as px

#load files
detail=pd.read_csv('deliveries.csv')
match=pd.read_csv('matches.csv')
match['season']=pd.DatetimeIndex(match['date']).year
new=detail.merge(match,left_on='id',right_on='id')


def most_wins_data():
    wins_per_season = new.groupby(['season', 'winner']).size().reset_index(name='wins')
    
    # Find the team with the maximum wins in each season
    idx = wins_per_season.groupby('season')['wins'].transform(max) == wins_per_season['wins']
    most_wins_per_season = wins_per_season[idx]
    return most_wins_per_season


def strike_rate(batsman):
    # Filter rows for the selected batsman
    batsman_detail = detail[detail['batter'] == batsman]
    # Calculate total runs scored by the batsman
    total_runs = batsman_detail['batsman_runs'].sum()    
    # Calculate total balls faced by the batsman
    total_balls = len(batsman_detail)    
    # Calculate strike rate
    strike_rate = (total_runs / total_balls) * 100 if total_balls > 0 else 0
    return strike_rate



def avg_of_batsman(batsman):
    filtered_data = detail[detail['batter'] == batsman]   
    # Calculate the number of innings (matches played)
    innings = filtered_data.shape[0]    
    # If the batsman has not played any innings, return 0
    if innings == 0:
        return 0    
    # Calculate the total runs scored by the batsman
    total_runs = filtered_data['batsman_runs'].sum()    
    # Calculate the average runs
    average_runs = total_runs / innings    
    return average_runs



def death_wickets(bowler):
    a=detail['over']>15
    b=detail['bowler']==bowler
    c=detail['is_wicket']==1
    return detail[a & b & c]['is_wicket'].count()


def batsman_score(batsman):
       return detail[detail['batter'] == batsman]['batsman_runs'].sum()


def death_strike_rate(batsman):
     # Filter the dataset for death overs (overs > 15)
    death_overs = detail[detail['over'] > 15]    
    # Filter the dataset for the selected batsman
    batsman_death_overs = death_overs[death_overs['batter'] == batsman]
        # Check if the selected batsman faced any balls during death overs
    if batsman_death_overs.empty:
        return "Selected batsman did not face any balls during death overs"    
    # Calculate strike rate
    runs_by_batsman = batsman_death_overs.groupby('batter')['batsman_runs'].sum()
    balls_faced_by_batsman = batsman_death_overs.groupby('batter')['ball'].count()
    strike_rate = (runs_by_batsman / balls_faced_by_batsman) * 100
    
    return strike_rate.values[0]  # Return the strike rate of the selected batsman


def batsman_six(batsman):
    q=detail['batter']==batsman
    w=detail['batsman_runs']==6
    return detail[q & w].shape[0]

def batsman_four(batsman):
    q=detail['batter']==batsman
    w=detail['batsman_runs']==4
    return detail[q & w].shape[0]

def bowler_wicket(bowler):
    q=detail['bowler']==bowler
    w=detail['is_wicket']==1
    return detail[q & w].shape[0]

def bowling_avg(bowler):
    a=detail['bowler']==bowler
    b=detail['is_wicket']==1
    runs=detail[a]['batsman_runs'].sum()
    wicket=detail[a & b]['is_wicket'].count()
    return runs/wicket

def batting_stats_in_venue(batsman, venue):
    # Filter data for the specified batsman and venue
    batsman_filter = new['batter'] == batsman
    venue_filter = new['venue'] == venue
    relevant_data = new[batsman_filter & venue_filter]
    
    # Calculate total runs scored and balls faced
    total_runs = relevant_data['batsman_runs'].sum()
    total_balls = relevant_data.shape[0]  # Total balls faced
    
    # Calculate strike rate
    strike_rate = (total_runs / total_balls) * 100
    
    return {
        'Total Runs': total_runs,
        'Total Balls': total_balls,
        'Strike Rate': strike_rate
    }

def winning_percentage(venue):
    matches_at_venue = new[new['venue'] == venue]
    total_matches = len(matches_at_venue)
    matches_won = matches_at_venue[matches_at_venue['winner'] == matches_at_venue['team1']]['winner'].count()
    winning_percentage = (matches_won / total_matches) * 100
    return winning_percentage

def average_score(venue):
    venue_scores = new[new['venue'] == venue]
    average_score = venue_scores.groupby('id')['total_runs'].sum().mean()
    return average_score


def batsman_against_bowler(batsman,bowler):
    a=detail['batter']==batsman
    b=detail['bowler']==bowler
    c=detail['is_wicket']==1
    runs=detail[a & b]['batsman_runs'].sum()
    wicket=detail[a & b & c]['is_wicket'].count()
    return {
        'Runs':runs, 
        'Wicket': wicket,}

def bowling_performance(venue):
    venue_bowling = new[new['venue'] == venue]
    runs_conceded = venue_bowling['total_runs'].sum()
    balls_bowled = venue_bowling.shape[0]
    overs_bowled = balls_bowled / 6
    bowling_performance = runs_conceded / overs_bowled
    return bowling_performance

def toss_analysis(venue):
    toss_wins = new[new['venue'] == venue]
    total_tosses = len(toss_wins)
    team1_wins = toss_wins[toss_wins['toss_winner'] == toss_wins['team1']].shape[0]
    team2_wins = toss_wins[toss_wins['toss_winner'] == toss_wins['team2']].shape[0]
    team1_win_percentage = (team1_wins / total_tosses) * 100
    team2_win_percentage = (team2_wins / total_tosses) * 100
    return team1_win_percentage, team2_win_percentage

def matches_per_season_visualization():
    # Grouping the data
    data = new.groupby(['id','season']).count().index.droplevel(level=0).value_counts().sort_index()
    
    # Create Plotly bar chart
    fig = px.bar(
        data_frame=data.reset_index(),
        x=data.index,
        y=data.values,
        orientation='h',
        title='Matches Played per Season',
        labels={'x': 'Season', 'y': 'Matches Played'},
        color=data.index,
        color_continuous_scale='Viridis'
    )
    
    return fig
    
def plot_matches_per_team():
    # Getting data
    data = new['bowling_team'].value_counts().sort_values(ascending=False)
    
    # Create Plotly bar chart
    fig = px.bar(
        data_frame=data.reset_index(),
        x=data.index,
        y=data.values,
        orientation='h',
        title='Matches Played per Team',
        labels={'x': 'Team', 'y': 'Matches Played'},
        color=data.index,
        color_continuous_scale='Blues'
    )
    
    return fig

def most_runs_by_batsman():
    # Grouping the data
    data = new.groupby(['batter'])['batsman_runs'].sum().sort_values(ascending=False)[:10]
    
    # Create Plotly bar chart
    fig = px.bar(
        data_frame=data.reset_index(),
        x=data.index,
        y=data.values,
        title='Most IPL Runs by a Batsman',
        labels={'batter': 'Batsman', 'batsman_runs': 'Runs'},
        color=data.index,
        color_continuous_scale='Sunset'
    )
    
    return fig

def venue_with_max_matches():
    venue_ser = new['venue'].value_counts().reset_index()
    venue_ser.columns = ['venue', 'matches']
    
    fig = px.bar(
        venue_ser,
        x='matches',
        y='venue',
        orientation='h',
        title='IPL Venues with Maximum Matches',
        labels={'matches': 'Number of Matches', 'venue': 'Venue'},
         color_continuous_scale='Sunset'
    )
    fig.update_layout(yaxis=dict(categoryorder='total ascending'))
    return fig

def umpire_with_most_matches():
    # Concatenating both umpire columns and counting matches
    umpires = pd.concat([new['umpire1'], new['umpire2']])
    umpire_counts = umpires.value_counts().reset_index()
    umpire_counts.columns = ['umpire', 'matches']
    
    # Create Plotly bar chart for top 10 umpires
    fig = px.bar(
        umpire_counts.head(10),
        x='matches',
        y='umpire',
        orientation='h',
        title='Top 10 Umpires with Most IPL Matches',
        labels={'matches': 'Number of Matches', 'umpire': 'Umpire'},
        color='umpire',
        color_continuous_scale='Viridis'
    )
    
    return fig
     