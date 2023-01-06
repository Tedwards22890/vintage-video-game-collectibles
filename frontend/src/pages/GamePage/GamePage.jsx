import axios from 'axios';
import { useState, useEffect } from "react";
import { useParams } from 'react-router-dom';
import useAuth from "../../hooks/useAuth";



const GamePage = (props) => {

    const [currentGame, setCurrentGame] = useState(null)
    const [user, token] = useAuth();
    const {gameId} = useParams();

async function displayGame() {
    try {
        let response = await axios.get(
            `http://127.0.0.1:8000${gameId.image1}`
        );
        setCurrentGame(response.data.items);
        console.log(response.data.items);
    } catch (error) {
        console.log(error.message);
    }
}

    return (
        <div>
        <h1> Some Text!</h1>
        <p>
            Game Name: {currentGame.title}
        </p>
        </div>


    );
}

export default GamePage;