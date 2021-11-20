import pandas as pd
import plotly.graph_objs as go
from track_focus import loadFocus
from datetime import datetime


def create_focus_df():
    today = datetime.strftime(datetime.today(),format="%Y-%m-%d")
    timeStartsStamp,dateStartsStamp,durations=loadFocus()
    df = pd.DataFrame(dict(dates=dateStartsStamp, focus=durations))
    return df


def plotFocus(df):
    df_focus_daily = pd.DataFrame(df.groupby("dates")["focus"].sum())
    mean_focus_time = round(df_focus_daily["focus"].mean(),2)
    focusBar = go.Bar(x=df_focus_daily.index,y=df_focus_daily["focus"],
                      name="Focus",marker_color="green")
    focusTrend = go.Scatter(x=df_focus_daily.index,y=df_focus_daily["focus"],    
                    name="Focus",marker_color="red")
    fig = go.Figure(data=[focusTrend,focusBar])
    fig.update_layout(title=f"Overview, Average Focus Time: {mean_focus_time} hours")
    fig.update_yaxes(title="Focus (h)")
    
    return fig
    
    
df = create_focus_df()
fig = plotFocus(df)
fig.show()