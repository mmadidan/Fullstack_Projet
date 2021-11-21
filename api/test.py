# -*- coding: utf-8 -*-

from flask import Flask
from flask import Flask, redirect, url_for, render_template, request, flash
import pandas as pd
import extraction_mongo as m
import fonctions_utiles as f
from flask import jsonify
import time
import json 

app = Flask(__name__)

film = m.liste_film()
lst_theme = m.liste_theme()
lst_TOP_realisateur = m.liste_realisateur()

titres_listes_top_film = [["Plus gros succès au BOX OFFICE", m.TOP_Box_Office()], ["TOP 50 Meilleurs films entre 2013 et 2019", m.Top_50()], ["Meilleurs réalisateurs de 2013 à 2019", m.TOP_meilleurs_realisateurs()]]

listes = []
for elm in titres_listes_top_film:
    listes.append([elm[0], f.c_film(elm[0]), elm[1]])


@app.route('/titre_film', methods = ['POST', 'GET'])
def liste_film():
    return jsonify(film)

@app.route('/liste_1_short', methods = ['POST', 'GET'])

def liste_1_short():
    liste_1_short = f.liste_alea(listes[0][2], 5)
    for i in range(len(liste_1_short)):
        liste_1_short[i]['image'] = liste_1_short[i]['nom_fichier_image']+'.jpg'
    dict = {}
    keys = []
    for i in range(5):
        keys.append('film'+str(i))
    a = 0
    for i in keys:
        dict[i] = liste_1_short[a]
        a += 1
    return dict



@app.route('/liste_2_short', methods = ['POST', 'GET'])
def liste_2_short():
    liste_2_short = f.liste_alea(listes[1][2], 5)
    for i in range(len(liste_2_short)):
        liste_2_short[i]['image'] = liste_2_short[i]['nom_fichier_image']+'.jpg'
    dict = {}
    keys = []
    for i in range(5):
        keys.append('film'+str(i))
    a = 0
    for i in keys:
        dict[i] = liste_2_short[a]
        a += 1
    return dict



@app.route('/liste_3_short', methods = ['POST', 'GET'])
def liste_3_short():
    liste_3_short = f.liste_alea(listes[2][2], 5)
    dict = {}
    keys = []
    for i in range(5):
        keys.append('realisateurs'+str(i))
    a = 0
    for i in keys:
        dict[i] = liste_3_short[a]
        a += 1
    return dict



@app.route('/film_alea', methods = ['POST', 'GET'])
def film_alea():
    film_alea = f.liste_alea(m.TOP_par_theme(f.c_film(lst_theme[f.r.randint(0, len(lst_theme)-1)])), 1)[0]
    film_alea['image'] = film_alea['nom_fichier_image']+'.jpg'
    return film_alea



@app.route('/liste_2', methods = ['POST', 'GET'])
def liste_2():
    liste_2 = listes[5]
    for i in range(len(liste_2)):
        liste_2[i]['image'] = listes[1][i]['nom_fichier_image']+'.jpg'
    return liste_2



@app.route('/liste_3', methods = ['POST', 'GET'])
def liste_3():
    liste_3 = listes[5]
    for i in range(len(liste_3)):
        liste_3[i]['image'] = listes[2][i]['nom_fichier_image']+'.jpg'
    return liste_3



@app.route('/rea', methods = ['POST', 'GET'])
def liste_rea():
    liste_rea = m.liste_realisateur()
    return liste_rea



@app.route('/theme', methods = ['POST', 'GET'])
def liste_theme():
    liste_theme = lst_theme
    return liste_theme



@app.route('/date', methods = ['POST','GET'])
def date():
    date = request.json['date']
    return jsonify({'the date is':date})



if __name__ == "__main__":
   app.run()