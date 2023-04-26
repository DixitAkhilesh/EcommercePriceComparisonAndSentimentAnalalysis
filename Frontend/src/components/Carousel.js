import React from 'react';
import { Carousel } from 'react-bootstrap';
import Image1 from '../Images/C-1.jpg';
import Image2 from '../Images/C-2.jpg';
import Image3 from '../Images/C-3.jpg';

class CarouselBody extends React.Component 
{
    render() {

        const carouselStyle = {
            width: "100%",
            padding: "0%"
        };

        const imgStyle = {
        height: "500px",
        width: "100%",
        
        };

        return (
            <div>
                <Carousel style={carouselStyle}>
                    <Carousel.Item>
                        <img
                            className="d-block w-100"   
                            src= {Image1}
                            style={imgStyle}
                            alt="First slide"
                        />
                    </Carousel.Item>
                    <Carousel.Item>
                        <img
                            className="d-block w-100"
                            src= {Image2}
                            style={imgStyle}
                            alt="Second slide"
                        />
                    </Carousel.Item>
                    <Carousel.Item>
                        <img
                            className="d-block w-100"
                            src= {Image3}
                            style={imgStyle}
                            alt="Third slide"
                        />
                    </Carousel.Item>
                </Carousel>
            </div>
      );
    }
}  

export default CarouselBody;
