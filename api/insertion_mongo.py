# -*- coding: utf-8 -*-

import fonctions_utiles as f

import pandas as pd
import pymongo
from pymongo import MongoClient

def nettoyage_dataframe(dataframe):
            dataframe = dataframe.drop('Unnamed: 0',1)
            dataframe = dataframe.fillna('"Non"')
            b = []
            for i in range(len(dataframe['theme_production'])):
                    b.append(eval(dataframe['theme_production'][i]))

            dataframe = dataframe.drop('theme_production',1)
            dataframe.insert(2,'theme_production',b,True)
            b = []
            for i in range(len(dataframe['Realisateur'])):
                b.append(eval(dataframe['Realisateur'][i]))
            dataframe = dataframe.drop('Realisateur',1)
            dataframe.insert(4,'Realisateur',b,True)
            b = []
            for i in range(len(dataframe['acteurs_principaux'])):
                b.append(eval(dataframe['acteurs_principaux'][i]))
            dataframe = dataframe.drop('acteurs_principaux',1)
            dataframe.insert(7,'acteurs_principaux',b,True)
            b = []
            for i in range(len(dataframe['charts'])):
                b.append(eval(dataframe['charts'][i]))
            dataframe = dataframe.drop('charts',1)
            dataframe.insert(8,'charts',b,True)
            b = []
            for i in range(len(dataframe['charts_IMDB'])):
                b.append(eval(dataframe['charts_IMDB'][i]))
            dataframe = dataframe.drop('charts_IMDB',1)
            dataframe.insert(10,'charts_IMDB',b,True)
            b = []
            for i in range(len(dataframe['charts_IMDB'])):
                b.append(eval(dataframe['other_details'][i]))
            dataframe = dataframe.drop('other_details',1)
            dataframe.insert(12,'other_details',b,True)

            b = []
            for i in range(len(dataframe['theme_production'])):
                try:
                    b.append(eval(dataframe['theme_production'][i]))
                except TypeError : 
                    b.append(dataframe['theme_production'][i])
                except NameError : 
                    b.append(dataframe['theme_production'][i])
            for i in range(len(b)):
                if b[i]!='Non':
                    b[i] = b[i][0]
            dataframe = dataframe.drop('theme_production',1)
            dataframe.insert(2,'theme_production',b,True)
            b = []
            for i in range(len(dataframe['Realisateur'])):
                try:
                    b.append(eval(dataframe['Realisateur'][i]))
                except TypeError : 
                    b.append(dataframe['Realisateur'][i])
                except NameError : 
                    b.append(dataframe['Realisateur'][i])
            for i in range(len(b)):
                if b[i]!='Non':
                    b[i] = b[i][0]
            dataframe = dataframe.drop('Realisateur',1)
            dataframe.insert(4,'Realisateur',b,True)
            b = []
            for i in range(len(dataframe['other_details'])):
                try:
                    b.append(eval(dataframe['other_details'][i]))
                except TypeError : 
                    b.append(dataframe['other_details'][i])
                except NameError : 
                    b.append(dataframe['other_details'][i])
            for i in range(len(b)):
                try:
                    b[i]['budget'] = int(b[i]['budget'][1:].replace(',',''))
                    b[i]['Cumulative_WW_Gross'] = int(b[i]['Cumulative_WW_Gross'][1:].replace(',',''))
                except ValueError : 
                    pass
                except TypeError :
                    pass
            dataframe = dataframe.drop('other_details',1)
            dataframe.insert(12,'other_details',b,True)

            dataframe.drop_duplicates(subset ="nom_film", keep = 'first', inplace=True)
            return dataframe

client = MongoClient('localhost', 27017)
database = client['local']

def base_de_donnee_insertion_ou_pas():
    if 'projet_Application_Full_Stack' not in database.list_collection_names():
        collection = database['projet_Application_Full_Stack']

        df_films = pd.read_csv('FILMS.csv')

    

        df_films = nettoyage_dataframe(df_films)

        df_films['charts_METACRITIC'] = df_films['charts_METACRITIC'].apply(lambda x: 0 if x=='Reviews' else x )
        df_films['nom_film_attache'] = df_films['nom_film'].apply(lambda x: f.c_film(x))
        df_films['nom_fichier_image'] = df_films['nom_film'].apply(lambda x: "/static/poster/"+f.c_film(x)+"_poster")
        df_films['note_moyenne'] = round((df_films['charts'].apply(lambda x: x['note_moyenne']) + df_films['charts_IMDB'].apply(lambda x: float(".".join(x[0].split(',')))) + df_films['charts_METACRITIC'].apply(lambda x: int(x)/10))/3,1)
        df_films['etoiles'] = df_films['note_moyenne'].apply(lambda x: [list(range(int(x))), 1, list(range(9-int(x)))] if x - int(x)<=0.5 else [list(range(int(x))), 0, list(range(10-int(x)))])

        DOCUMENTS = df_films.to_dict('records')
        collection.insert_many(DOCUMENTS)
