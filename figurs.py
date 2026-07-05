import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import functionfile
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


def batsman_performance_visualization(selected_batsman): 
    # Fetch data (replace these with actual function calls)
    runs = functionfile.batsman_score(selected_batsman)
    sixes = functionfile.batsman_six(selected_batsman)
    fours = functionfile.batsman_four(selected_batsman)

    # Create DataFrame
    df = pd.DataFrame({'Metric': ['Runs', 'Sixes', 'Fours'], 'Value': [runs, sixes, fours]})

    # Create a Plotly bar chart
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=df['Metric'],
        y=df['Value'],
        name=selected_batsman,
        marker_color='royalblue'
    ))

    fig.update_layout(
        title=f'Performance of {selected_batsman}',
        xaxis_title='Performance Metrics',
        yaxis_title='Count',
        showlegend=False
    )

    return {'fig': fig, 'df': df}


def most_wins_per_season_visualization(data):
    fig = px.bar(
        data,
        x='season',
        y='wins',
        color='winner',
        title='Most Winning Team Per Season',
        labels={'season': 'Season', 'wins': 'Number of Wins'},
        barmode='group',
    )
    fig.update_layout(xaxis=dict(title='Season'), yaxis=dict(title='Wins'))
    return fig


def most_losses_per_season_visualization(data):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='loser', data=data)
    plt.title('Most Losing Team Per Season')
    plt.xlabel('Team')
    plt.ylabel('Number of Losses')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def toss_win_impact_visualization(data):
    plt.figure(figsize=(8, 6))
    sns.countplot(x='winner', hue='toss_winner', data=data)
    plt.title('Impact of Toss on Match Outcome')
    plt.xlabel('Match Winner')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend(title='Toss Winner', loc='upper right')
    plt.show()

def most_player_of_match_visualization(data):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='player_of_match', data=data, order=data['player_of_match'].value_counts().index)
    plt.title('Player with Most Player of the Match Awards')
    plt.xlabel('Player')
    plt.ylabel('Number of Awards')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def most_matches_hosted_visualization(data):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='city', data=data)
    plt.title('City Hosting Maximum IPL Matches')
    plt.xlabel('City')
    plt.ylabel('Number of Matches')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def most_winning_team_per_season_visualization(data):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='season', hue='winner', data=data)
    plt.title('Most Winning Team Per Season')
    plt.xlabel('Season')
    plt.ylabel('Number of Wins')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend(title='Team', loc='upper right')
    plt.show()

def most_matches_umpire_visualization(data):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='umpire1', data=data)
    plt.title('On-field Umpire with Most IPL Matches')
    plt.xlabel('Umpire')
    plt.ylabel('Number of Matches')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def biggest_victories_visualization(data):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='result_margin', y='winner', data=data, hue='win_by', orient='h')
    plt.title('Biggest Victories in IPL')
    plt.xlabel('Margin of Victory')
    plt.ylabel('Winner')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend(title='Winning Type', loc='lower right')
    plt.show()
