
import pandas as pd
from .loadingContext import *


from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px


def load_graph_data():
    conn = load_db_connection()
    df = pd.read_sql('select * from canteenu', conn)
    df_statis = df.copy()
    df_statis = df_statis[['소재지도로명주소']]
    df_statis = pd.concat([df_statis, df_statis['소재지도로명주소'].str.split(' ', expand=True)], axis=1 )

    df_statis_cnt = df_statis[['소재지도로명주소',0,1,2]]
    df_statis_cnt.columns = ['주소', '지방', '시군구', '읍면리']



    return 



def draw_grph():
    conn = load_db_connection()
    






