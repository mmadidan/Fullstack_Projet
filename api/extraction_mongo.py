# -*- coding: utf-8 -*-

import pymongo
from pymongo import MongoClient
import pandas as pd
varProject = {"_id":0}
import insertion_mongo as i_mongo
import fonctions_utiles as f


client = MongoClient('localhost', 27017)
database = client['local']

i_mongo.base_de_donnee_insertion_ou_pas()

collection = database['projet_Application_Full_Stack']


def liste_theme():
    l = collection.aggregate([
        {"$group" : {"_id": "$theme_production", "nombre de films" : {"$sum" : 1}}},
        {"$sort" : {"nombre de films": -1}}
        ])

    l = list(l)
    liste_theme = []
    for i in range(len(l)):
        if l[i]['_id'] == 'Non':
            liste_theme.append("Documentaire")
        else:
            liste_theme.append(l[i]['_id'])
    return liste_theme

def liste_realisateur():
    l= ['Alfonso Cuarón', 'Damien Chazelle', 'Pete Docter', 'Claude Barras', 'Lenny Abrahamson', 'Isao Takahata', 'Park Chan-wook', 'Bob Persichetti', 'George Miller', 'Quentin Tarantino']
    return l

def liste_film():
    l = collection.distinct("nom_film")
    return l
    
def TOP_par_theme(theme):
    varProject = {"_id":0}
    dico ={
        "TOP_Drame" : collection.find({"theme_production":"Drame","charts.nombre_critiques":{"$gte":5000}},varProject).sort([("charts.note_moyenne", -1)]).limit(50),
        "TOP_Action" : collection.find({"theme_production":"Action","charts.nombre_critiques":{"$gte":5000}},varProject).sort([("charts.note_moyenne", -1)]).limit(50),
        "TOP_Comédie" : collection.find({"theme_production":"Comédie","charts.nombre_critiques":{"$gte":5000}},varProject).sort([("charts.note_moyenne", -1)]).limit(50),
        "TOP_Animation" : collection.find({"theme_production":"Animation","charts.nombre_critiques":{"$gte":5000}},varProject).sort([("charts.note_moyenne", -1)]),
        "TOP_Biopic" : collection.find({"theme_production":"Biopic","charts.nombre_critiques":{"$gte":5000}},varProject).sort([("charts.note_moyenne", -1)]),
        "TOP_Comédie_dramatique" : collection.find({"theme_production":"Comédie dramatique","charts.nombre_critiques":{"$gte":5000}},varProject).sort([("charts.note_moyenne", -1)]),
        "TOP_Aventure" : collection.find({"theme_production":"Aventure","charts.nombre_critiques":{"$gte":5000}},varProject).sort([("charts.note_moyenne", -1)]),
        "TOP_Policier" : collection.find({"theme_production":"Policier","charts.nombre_critiques":{"$gte":5000}},varProject).sort([("charts.note_moyenne", -1)]),
        "TOP_Thriller" : collection.find({"theme_production":"Thriller","charts.nombre_critiques":{"$gte":5000}},varProject).sort([("charts.note_moyenne", -1)]),
        "TOP_Documentaire" : collection.find({"theme_production":"Non","charts.nombre_critiques":{"$gte":5000}},varProject).sort([("charts.note_moyenne", -1)]),
        "TOP_Épouvante-Horreur" : collection.find({"theme_production":"Épouvante-Horreur","charts.nombre_critiques":{"$gte":500}},varProject).sort([("charts.note_moyenne", -1)]),
        "TOP_Science_fiction" : collection.find({"theme_production":"Science-fiction","charts.nombre_critiques":{"$gte":500}},varProject).sort([("charts.note_moyenne", -1)]),
        "TOP_Fantastique" : collection.find({"theme_production":"Fantastique","charts.nombre_critiques":{"$gte":500}},varProject).sort([("charts.note_moyenne", -1)]),
        "TOP_Western" : collection.find({"theme_production":"Western","charts.nombre_critiques":{"$gte":500}},varProject).sort([("charts.note_moyenne", -1)]),
        "TOP_Comédie_musicale" : collection.find({"theme_production":"Comédie musicale","charts.nombre_critiques":{"$gte":500}},varProject).sort([("charts.note_moyenne", -1)]),
        "TOP_Romance" : collection.find({"theme_production":"Romance","charts.nombre_critiques":{"$gte":500}},varProject).sort([("charts.note_moyenne", -1)]),
        "TOP_Historique" : collection.find({"theme_production":"Historique","charts.nombre_critiques":{"$gte":500}},varProject).sort([("charts.note_moyenne", -1)]),
        "TOP_Comédie_romantique" : collection.find({"theme_production":"Comédie romantique","charts.nombre_critiques":{"$gte":500}},varProject).sort([("charts.note_moyenne", -1)]),
        "TOP_Gangster" : collection.find({"theme_production":"Gangster","charts.nombre_critiques":{"$gte":500}},varProject).sort([("charts.note_moyenne", -1)]),
        "TOP_Expérimental" : collection.find({"theme_production":"Expérimental","charts.nombre_critiques":{"$gte":500}},varProject).sort([("charts.note_moyenne", -1)]),
        "TOP_Arts_martiaux" : collection.find({"theme_production":"Arts martiaux","charts.nombre_critiques":{"$gte":500}},varProject).sort([("charts.note_moyenne", -1)]),
        "TOP_Musique" : collection.find({"theme_production":"Musique","charts.nombre_critiques":{"$gte":500}},varProject).sort([("charts.note_moyenne", -1)]),
        "TOP_Film_noir" : collection.find({"theme_production":"Film noir","charts.nombre_critiques":{"$gte":500}},varProject).sort([("charts.note_moyenne", -1)]) 
    }
    return list(dico['TOP_'+f.c_film(theme)])

def TOP_meilleurs_realisateurs():
    varProject = {"_id":0}
    l = []
    dico ={
        "Alfonso Cuarón" : collection.find({"Realisateur" : 'Alfonso Cuarón'},varProject),
        "Damien Chazelle" : collection.find({"Realisateur" : 'Damien Chazelle'},varProject),
        "Pete Docter" : collection.find({"Realisateur" : 'Pete Docter'},varProject),
        "Claude Barras" : collection.find({"Realisateur" : 'Claude Barras'},varProject),
        "Lenny Abrahamson" : collection.find({"Realisateur" : 'Lenny Abrahamson'},varProject),
        "Isao Takahata" : collection.find({"Realisateur" : 'Isao Takahata'},varProject),
        "Park Chan-wook" : collection.find({"Realisateur" : 'Park Chan-wook'},varProject),
        "Bob Persichetti" : collection.find({"Realisateur" : 'Bob Persichetti'},varProject),
        "George Miller" : collection.find({"Realisateur" : 'George Miller'},varProject),
        "Quentin Tarantino" : collection.find({"Realisateur" : 'Quentin Tarantino'},varProject)
    }

    for realisateur in liste_realisateur():
        l = l + list(dico[realisateur])
    return l



def TOP_Box_Office():
    Best_Box_Office = collection.find({"other_details.budget":{"$gte":100000000}},varProject).sort([("other_details.Cumulative_WW_Gross", -1),("charts.note_moyenne", -1)]).limit(50)
    return list(Best_Box_Office)

def Top_50():
    TOP_FILMS_50 = collection.find({"charts.nombre_critiques":{"$gte":5000}},varProject).sort([("charts.note_moyenne", -1)]).limit(50)
    return list(TOP_FILMS_50)


def recherche_film(nom_film):
    return list(collection.find({'nom_film_attache': nom_film}))[0]
