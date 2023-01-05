import React, {useRef} from "react";
import { useEffect, useState } from "react";
import useAuth from "../../hooks/useAuth";
import {Link} from 'react-router-dom'

import axios from "axios";

const HomePage = ( props ) => {
  // The "user" value from this Hook contains the decoded logged in user information (username, first name, id)
  // The "token" value is the JWT token that you will send in the header of any request requiring authentication
  //TODO: Add an AddCars Page to add a car for a logged in user's garage
  const [user, token] = useAuth();
  const [cars, setCars] = useState([]);
  const [games, setGames] = useState([]);

  useEffect(() => {
    const fetchGames = async () => {
      try {
        let response = await axios.get("http://127.0.0.1:8000/api/games/all/", {
          headers: {
            Authorization: "Bearer " + token,
          },
        });
        setGames(response.data);
      } catch (error) {
        console.log(error.response.data);
      }
    };
    fetchGames();


  }, [token]);

  const handleButtonClick = (games) =>{
    props.setCurrentGame(games)
  }


  return (
    <div className="container">
      <h1>Home Page for {user.username}!</h1>
      {games &&
        games.map((games) => (
          <p key={games.id}>
            <Link to={`games/${games.id}`}>
              <button type="button" onClick={() => handleButtonClick(games)}>
            {games.id} {games.title} <img src={`http://127.0.0.1:8000${games.image1}`} />  
            </button>
            </Link>
            </p>
        ))}
    </div>
  );
};

export default HomePage;
