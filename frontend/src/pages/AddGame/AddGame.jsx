import axios from 'axios';
import { useState, useEffect, version } from "react";
import { useParams } from 'react-router-dom';
import useAuth from "../../hooks/useAuth";



const AddGame= ( props ) => {

    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const [cost, setCost] = useState('');
    const [year, setYear] = useState('');
    const [console, setConsole] = useState('');
    const [version, setversion] = useState('');
    const [image, setImage] = useState('');

    if (!open) return null;

    async function handleSubmit(event) {
        event.preventDefault();
        const newGame = {
            title: title,
            description: description,
            cost: cost,
            year: year,
            console: console,
            version: version,
            image: image,

        };
        if (title===''|| description==='' || cost==='' ||year===''||console===''||version==='')
        {
            alert('Please be sure all fields are filled out!')
        }
        else 
        {

            console.log({newGame});
            axios.put(`http://127.0.0.1:8000/api/games/`, newGame)
            setTitle("")
            setDescription("")
            setCost("")
            setYear("")
            setConsole('')
            setVersion('')
            setImage('')

        }
    }
    

    return (
        <form onSubmit={handleSubmit} className="form-grid">
        <div className='overlay'>
            <div className='modalContainer'>
                <div className="modalRight">
                    <button className='closeBtn' onClick={onClose}>x</button>
                    <div className="grid-container">
                    <div classname="grid-item">
                    <input type="text" placeholder="Title" value={title} onChange={(event) => setTitle(event.target.value)}/>
                    </div>

                    <div classname="grid-item">
                    <input type="text" placeholder="Description" value={description} onChange={(event) => setDescription(event.target.value)}/>
                    </div>

                    <div classname="grid-item">
                    <input type="text" placeholder="Cost" value={cost} onChange={(event) => setCost(event.target.value)}/>
                    </div>

                    <div classname="grid-item">
                    <input type="text" placeholder="Year" value={year} onChange={(event) => setYear(event.target.value)}/>
                    </div>

                    <div classname="grid-item">
                    <input type="text" placeholder="Console" value={console} onChange={(event) => setConsole(event.target.value)}/>
                    </div>

                    <div classname="grid-item">
                        <input type="text" placeholder="Version" value={version} onChange={(event) => setVersion(event.target.value)}/>
                    </div>

                    <div classname="grid-item">
                        <input type="text" placeholder="Image" value={image} onChange={(event) => setImage(event.target.value)}/>
                    </div>
                <br/>
                </div>
                    <button type="submit" className="btn btn-primary" style={{"margin-right": "1em"}}>Update</button>

                </div>
            </div>
        </div>
        </form>
    )
}
}

export default GamePage;