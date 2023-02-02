// General Imports
import { Routes, Route } from "react-router-dom";
import { useState } from "react";
import "./App.css";

// Pages Imports
import HomePage from "./pages/HomePage/HomePage";
import LoginPage from "./pages/LoginPage/LoginPage";
import RegisterPage from "./pages/RegisterPage/RegisterPage";
import GamePage from "./pages/GamePage/GamePage";

// Component Imports
import Navbar from "./components/NavBar/NavBar";
import Footer from "./components/Footer/Footer";

// Util Imports
import PrivateRoute from "./utils/PrivateRoute";

function App() {
const [currentGame, setCurrentGame] = useState([])

  return (
    <div>
      <Navbar />
      <Routes>
        <Route
          path="/"
          element={
            <PrivateRoute>
              <HomePage setCurrentGame={setCurrentGame} />
              <p>Current Game: {currentGame}</p>
            </PrivateRoute>
          }
        />
        <Route
        path="games/:gameId/" element={
          <PrivateRoute>
            <GamePage currentGame={currentGame} />
          </PrivateRoute>
        } />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/login" element={<LoginPage />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
