import React from 'react';
import Extract from '../json_files/FlipkartExtract.json';


const Flipkart = () => {
  return (
    <div>
        <div style={{ display: 'flex', paddingTop:'2%' }}>
            <div style={{ flex: 1 }}>
                <h1>Highlights:</h1>
                <ul style={{ listStyleType: 'disc', marginLeft: '1.5rem' }}>
                {Extract.highlights.map((highlight, index) => (
                    <li key={index} style={{ marginBottom: '0.5rem' }}>
                    {highlight}
                    </li>
                ))}
                </ul>
                
                <div>
                    <button href={Extract.url}>View Product</button>
                </div>
            </div>

            <div style={{ flex: 1 }}>
                <h1>Offers:</h1>
                {Extract.offers.length > 0 ? (
                <ul style={{ listStyleType: 'none', padding: 0 }}>
                    {Extract.offers.map((offer, index) => (
                    <li key={index} style={{ marginBottom: '1rem' }}>
                        <h2 style={{ fontSize: '1.2rem', marginBottom: '0.5rem' }}>{offer.title}</h2>
                        <p style={{ fontSize: '1rem', color: '#666' }}>{offer.description}</p>
                    </li>
                    ))}
                </ul>
                ) : (
                <p style={{ fontStyle: 'italic' }}>No offers available.</p>
                )}
            </div>
        </div>
        
    </div>
  );
};

export default Flipkart;
