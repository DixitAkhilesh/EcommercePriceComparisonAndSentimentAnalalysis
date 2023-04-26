import React, { useState, useEffect } from 'react';
import ProductList from './ProductDetails';

function MyComponent() {
    const [flipkart_data, setFlipkartData] = useState([]);
    const [amazon_data, setAmazonData] = useState([]);
  
    useEffect(() => {
      const fetchData = async () => {
        const response = await fetch('http://localhost:8080/flipkart_product.json');
        const jsonData = await response.json();
        setFlipkartData(jsonData);
      };
      fetchData();
    }, []);
    
    useEffect(() => {
        const fetchData = async () => {
          const response = await fetch('http://localhost:8080/amazon_product.json');
          const jsonData = await response.json();
          setAmazonData(jsonData);
        };
        fetchData();
    }, []);
    // fetch('..\\..\\..\\Backend\\json_files\\flipkart_product.json')
    // .then(response =>
    //     response.json())
    // .then(data =>
    //     console.log(data));



return (
    <div>
        {flipkart_data.map(item => (
            <li key={item.product_url}>
                <img src={item.product_image} alt={item.product_name} />
                <a href= {item.product_url}>{item.product_name}</a>
                <td>{item.product_price}</td>
                <td>{item.product_review}</td>
                <td>{item.total_review}</td>
            </li>
        ))}

        <br />
        <br />
        <br />
        <br />
        <h1>AMAZON DATA</h1>
        <br />
        <br />
        {amazon_data.map(item => (
            <li key={item.product_url}>
                <img src={item.product_image} alt={item.product_name} />
                <a href= {item.product_url}>{item.product_name}</a>
                <td>{item.product_price}</td>
                <td>{item.product_review}</td>
                <td>{item.total_review}</td>
            </li>
        ))}

    </div>
);
}

export default MyComponent;