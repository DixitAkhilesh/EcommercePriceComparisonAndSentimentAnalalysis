import './Data.css'
import Footer from './Footer';
import Amazonproducts from '../json_files/amazon_fashion_product.json';
import Flipkartproducts from '../json_files/flipkart_fashion_product.json';
import { FaStar, FaStarHalfAlt } from 'react-icons/fa';
import AmazonLogo from '../Images/Amazon.jpg'
import FlipkartLogo from '../Images/Flipkart.jpg'
import { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

function RatingStars({ rating }) {
    const fullStars = Math.floor(rating);
    const halfStar = rating - fullStars >= 0.5 ? true : false;
  
    const stars = [];
    for (let i = 0; i < fullStars; i++) {
        stars.push(<FaStar key={i} />);
    }
  
    if (halfStar) {
        stars.push(<FaStarHalfAlt key={fullStars} />);
    }
  
    if (fullStars < 5) {
        const emptyStars = 5 - fullStars - (halfStar ? 1 : 0);
        for (let i = 0; i < emptyStars; i++) {
            stars.push(<FaStar key={fullStars + i} className="empty-star" />);
        }
    }
  
    return stars;
}



function Fashion() {
    
    const navigate = useNavigate();
    const [clicked, setClicked] = useState(false);
    const [flag, setFlag] = useState(false);

    const handleAmazonSubmit = (productUrl) => {
        navigate('/Amazondetails', { state: { url: productUrl } });
        fetch('http://localhost:5000/amazon', {
            method: 'POST',
            body: JSON.stringify({ url: productUrl }),
            headers: {
            'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (!response.ok) {
            throw new Error('Network response was not ok');
            }
        })
        .catch(error => {
            console.error('There was an error sending the data to the server:', error);
        });
    };

    const handleFlipkartSubmit = (productUrl) => {
        navigate('/Flipkartdetails', { state: { url: productUrl } });
        fetch('http://localhost:5000/flipkart', {
            method: 'POST',
            body: JSON.stringify({ url: productUrl }),
            headers: {
            'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (!response.ok) {
            throw new Error('Network response was not ok');
            }
            
        })
        .catch(error => {
            console.error('There was an error sending the data to the server:', error);
        });
    };

    const lastFiveData = Amazonproducts.slice(-5);
    const lastFiveFlipkartData = Flipkartproducts.slice(-5);

    return (
        <div>
            <div class="products-container">
                <div class="amazon-products">
                    <img src={AmazonLogo} style={{maxWidth: '100%', maxHeight: '100px', marginLeft:'35%', display:'block', margin:'0 auto'}}/>
                    <div class="product-cards">
                        {lastFiveData.map((product) => (
                        <div class="product-card" key={product.product_url}>
                            <img src={product.product_image} alt={product.product_name} />
                            <div class="product-info" style={{textAlign:'left', marginLeft:'2%'}}>
                                <h3>
                                    <a href={product.product_url} target="_blank" rel="noreferrer">
                                        {product.product_name}
                                    </a>
                                </h3>
                                <br />
                                <h5>{product.product_price}</h5>
                                <div style={{ display: 'flex', alignItems: 'center' }}>
                                    {/* <RatingStars rating={product.product_review}/> */}
                                    <h5 style={{ marginLeft: '0.5rem' }}>{product.product_review} Stars</h5>
                                    <h6 style={{ marginLeft: '0.5rem' }}>{product.total_review} Reviews</h6>
                                </div>
                                <button onClick={() => handleAmazonSubmit(product.product_url)}>View Details</button>
                            </div>
                        </div>
                        ))}
                    </div>
                </div>
                <div class="flipkart-products" >
                    <img src={FlipkartLogo} style={{maxWidth: '100%', height: '100px' , display:'block', margin:'0 auto'}}/>
                    <div class="product-cards">
                    {lastFiveFlipkartData.map((product) => (
                    <div class="product-card" key={product.product_url}>
                        <img src={product.product_image} alt={product.product_name} />
                        <div class="product-info"  style={{textAlign:'left', marginLeft:'2%', padding:'2% '}}>
                            <h3>
                                <a href={product.product_url} target="_blank" rel="noreferrer">
                                    {product.product_name}
                                </a>
                            </h3>
                            <br />
                            <h5>{product.product_price}</h5>
                            <div style={{ display: 'flex', alignItems: 'center' }}>
                                {/* <RatingStars rating={product.product_review}/> */}
                                <h5 style={{ marginLeft: '0.5rem' }}>{product.product_review} Stars</h5>
                                <h6 style={{ marginLeft: '0.5rem' }}>{product.total_review} Reviews</h6>
                            </div>
                            <button onClick={() => handleFlipkartSubmit(product.product_url)}>View Details</button>
                        </div>
                    </div>
                    ))}
                    </div>
                </div>
            </div>
            <Footer/>
        </div>
    );
}

export default Fashion