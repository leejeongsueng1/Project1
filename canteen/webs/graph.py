
import pandas as pd
from .loadingContext import *
from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.io as po



def load_graph_data():
    conn = load_db_connection()
    df = pd.read_sql(text('select * from canteenu'), conn)
    df_statis = df.copy()
    df_statis = df_statis[['소재지도로명주소']]
    df_statis = pd.concat([df_statis, df_statis['소재지도로명주소'].str.split(' ', expand=True)], axis=1 )
    df_statis_cnt = df_statis[['소재지도로명주소',0,1,2]]
    df_statis_cnt.columns = ['주소', '지방', '시군구', '읍면리']
    return df_statis_cnt


def draw_graph(loc_name):
    loc_name = loc_name.split()[0]
    print(loc_name)
    data = load_graph_data()
    df_draw = data[data['지방'] == loc_name]
    print(df_draw)
    df_draw[f'{loc_name}_개수'] = 1
    fig = px.bar(df_draw, x='시군구', y=f'{loc_name}_개수')
    return po.write_html(fig, file=f'webs/templates/webs/graph.html', auto_open=True)
    
    
    



