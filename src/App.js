import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';
import List, { Item } from "semantic-ui-react"

export default function App() {

  const [data0, setData0] = useState([]);
  const [data1, setData1] = useState([]);
  const [data2, setData2] = useState([]);
  const [data3, setData3] = useState([]);
  const [data4, setData4] = useState([]);

  const [film0, setFilm0] = useState([]);
  const [film1, setFilm1] = useState([]);
  const [film2, setFilm2] = useState([]);
  const [film3, setFilm3] = useState([]);
  const [film4, setFilm4] = useState([]);

  const [list0, setList0] = useState([]);
  const [list1, setList1] = useState([]);
  const [list2, setList2] = useState([]);
  const [list3, setList3] = useState([]);
  const [list4, setList4] = useState([]);



  useEffect(() => {
    fetch('/liste_1_short')
    .then(res => res.json())          // convert to plain text
    .then(text => {

    setData0(text.film0);
    setData1(text.film1);
    setData2(text.film2);
    setData3(text.film3);
    setData4(text.film4);

  });
}, []);

useEffect(() => {
  fetch('/liste_2_short')
  .then(res => res.json())          // convert to plain text
  .then(liste => {

  setList0(liste.film0);
  setList1(liste.film1);
  setList2(liste.film2);
  setList3(liste.film3);
  setList4(liste.film4);

});
}, []);

useEffect(() => {
  fetch('/liste_3_short')
  .then(res => res.json())          // convert to plain text
  .then(film => {

  setFilm0(film.realisateurs0);
  setFilm1(film.realisateurs1);
  setFilm2(film.realisateurs2);
  setFilm3(film.realisateurs3);
  setFilm4(film.realisateurs4);

});
}, []);


  return (
      <div>
        <head>
          <title>
            Quel film ?
          </title>
          <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css" rel="stylesheet"></link>
          <meta charset='utf-8'></meta>
        </head>
        <body>
          <header>
            <div class="bouton_principal">
              <a><img src="/static/logo.png" className="logo" srcset="" /></a>
            </div>
            
          </header>
          <main>
            <div class='menu'>
              Type Film
              <form method="post" action="/date">
                <select name = "type_film" id="tf">
                  <option value="Rien">Veuillez sélectionner</option>
                </select>
                <button type="submit"><i class="fa fa-search" aria-hidden="true"></i></button>
              </form>
            </div>
            <div class="contenu">
              <div class="film_alea">
                <div class="poster_film">
                  <a><img src={data0.image} className="Film-Poster" alt="Poster" /></a>
                </div>
                <div class="details_film">
                  <h3>{data0.nom_film} </h3>
                  <h3>{data0.theme_production}</h3>
                  <h3>{data0.duree_film} </h3>
                  <h3>{data0.note_moyenne}/10</h3>

                </div>
              </div>
            </div>
            <br></br>
            <br></br>
            <br></br>
            <div class="liste_1">
              <a><h2>PLUS GROS SUCCES AU BOX OFFICE</h2> </a>
              <table>
                <tr>
                  <td>
                    <div class="liste_poster">
                      <a><img src={data0.image} className="Film-Poster" alt="Poster" /><h5>{data0.nom_film}</h5></a>
                      <a><img src={data1.image} className="Film-Poster" alt="Poster" /><h5>{data1.nom_film}</h5></a>
                      <a><img src={data2.image} className="Film-Poster" alt="Poster" /><h5>{data2.nom_film}</h5></a>
                      <a><img src={data3.image} className="Film-Poster" alt="Poster" /><h5>{data3.nom_film}</h5></a>
                      <a><img src={data4.image} className="Film-Poster" alt="Poster" /><h5>{data4.nom_film}</h5></a>
                    </div>
                  </td>
                </tr>
              </table>
            </div>

            <div class="liste_2">
              <a><h2>TOP 50 Meilleurs Films entre 2013 et 2019</h2> </a>
              <table>
                <tr>
                  <td>
                    <div class="poster">
                      <a><img src={list0.image} className="Film-Poster" alt="Poster" /><h5>{list0.nom_film}</h5></a>
                      <a><img src={list1.image} className="Film-Poster" alt="Poster" /><h5>{list1.nom_film}</h5></a>
                      <a><img src={list2.image} className="Film-Poster" alt="Poster" /><h5>{list2.nom_film}</h5></a>
                      <a><img src={list3.image} className="Film-Poster" alt="Poster" /><h5>{list3.nom_film}</h5></a>
                      <a><img src={list4.image} className="Film-Poster" alt="Poster" /><h5>{list4.nom_film}</h5></a>
                    </div>
                  </td>
                </tr>
              </table>
            </div>

            <div class="liste_1">
              <a><h2>MEILLEURS REALISATEURS DE 2013 à 2019</h2> </a>
              <table>
                <tr>
                  <td>
                    <div class="poster">
                      <a><h2>{film0.Realisateur}</h2></a>
                      <a><h2>{film1.Realisateur}</h2></a>
                      <a><h2>{film2.Realisateur}</h2></a>
                      <a><h2>{film3.Realisateur}</h2></a>
                      <a><h2>{film4.Realisateur}</h2></a>
                    </div>
                  </td>
                </tr>
              </table>
            </div>


          </main>
          <footer>
            Copyright Ashkar et Nadjime 2021
          </footer>
        </body>

      </div>
        );
      }
