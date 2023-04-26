import React, { useState, useEffect } from 'react';
import Amazonproducts from './..\\json_files\\amazon_product.json';
import Flipkartproducts from './..\\json_files\\flipkart_product.json';

function AmazonDetails() {
    // const [data, setData] = useState([]);

    // useEffect(() => {
    //     const fetchData = async () => {
    //     const response = await fetch('./..\\json_files\\amazon_product.json');
    //     const json = await response.json();
    //     setData(json);
    //     };
    //     fetchData();
    // }, []);

    // Extract the last 5 elements from the data array using slice()
    const lastFiveData = Amazonproducts.slice(-5);

    return (
        <div>
            {lastFiveData.map((product) => (
            <div key={product.product_url}>
                <img src={product.product_image} alt={product.product_name} />
                <h3>{product.product_name}</h3>
                <p>{product.product_price}</p>
                <p>{product.product_review}</p>
                <p>{product.total_review} reviews</p>
                <a href={product.product_url}>View on Amazon</a>
            </div>
            ))}
        </div>
    );
}


function FlipkartDetails()
{
    const lastFiveFlipkartData = Flipkartproducts.slice(-5);

    return (
        <div>
            <h1>FLIPKART DATA</h1>
            {lastFiveFlipkartData.map((product) => (
            <div key={product.product_url}>
                <img src={product.product_image} alt={product.product_name} />
                <h3>{product.product_name}</h3>
                <p>{product.product_price}</p>
                <p>{product.product_review}</p>
                <p>{product.total_review} reviews</p>
                <a href={product.product_url}>View on Flipkart</a>
            </div>
            ))}
        </div>
    );
}

export {AmazonDetails, FlipkartDetails}