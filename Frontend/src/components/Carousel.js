import React from 'react';
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import './Carousel.css';
import Image1 from '../Images/C-1.jpg';
import Image2 from '../Images/C-2.jpg';
import Image3 from '../Images/C-3.jpg';
import prev from "../Images/prev.jpg";
import next from "../Images/next.jpg";

const PrevArrow = (props) => {
    const { className, style, onClick } = props;
    return (
      <div
        className={className}
        style={{ ...style, backgroundColor: 'white'}}
        onClick={onClick}
      >
        <img src={prev}alt="" style={{height: '30px'}}/>
      </div>
    );
  };
  
  const NextArrow = (props) => {
    const { className, style, onClick } = props;
    return (
      <div
        className={className}
        style={{ ...style, backgroundColor: 'white' }}
        onClick={onClick}
      >
        <img src={next}alt="" style={{height: '30px'}}/>
      </div>
    );
  };

function Carousel() {
    const settings = {
        dots: true,
        infinite: true,
        speed: 500,
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 2000, 
        prevArrow: <PrevArrow />,
        nextArrow: <NextArrow />
    };

    return (
        <div className="carousel-container">
            <Slider {...settings}>
                <div>
                <img src={Image1} alt="Slide 1" style={{height:'500px',width:'100%'}}/>
                </div>
                <div>
                <img src={Image2} alt="Slide 2" style={{height:'500px',width:'100%'}}/>
                </div>
                <div>
                <img src={Image3} alt="Slide 3" style={{height:'500px',width:'100%'}}/>
                </div>
            </Slider>
        </div>
    );
}

export default Carousel;
