import React, { useState } from 'react';
import axios from 'axios';
import Data from './Electronics';
import Navbar from './NavBar';
import "./Search.css"
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSearch } from '@fortawesome/free-solid-svg-icons';
import load from "../Images/Loading3.gif";

function SearchElectronics() {
    const [inputString, setInputString] = useState('');
    const [count, setCount] = useState(0);
    const [isLoading, setIsLoading] = useState(false);

    const handleSubmit = async (event) => {
        event.preventDefault();
        setIsLoading(true); // Set loading state to true

        try {
            const response = await axios.post('http://localhost:5000/receive-string', { inputString });
            const { data } = response;
            console.log(`String sent to backend: ${inputString}`);
            console.log(`String received from backend: ${data}`);
            setCount(count + 1);
        } catch (error) {
            console.error(error);
        }

        setIsLoading(false); // Set loading state to false
    };

    return (
        <div>
            <Navbar/>
            <div className="Form">
                <form onSubmit={handleSubmit}>
                    <input type="text" value={inputString} onChange={(event) => setInputString(event.target.value)} placeholder='Enter Product Name' />
                    <button type="submit" className="search-button" style={{ margin: '20px', padding: '0.5%' }}>
                        <FontAwesomeIcon icon={faSearch} />
                    </button>
                </form>
            </div>
            {isLoading ? (
                <div className="loading-container">
                    <div className="loading-spinner" />
                    <div className="loading-text"><h4>Loading...</h4></div>
                </div>
            ) : (
                count > 0 && <Data />
            )}
        </div>
    );
}

export default SearchElectronics;
