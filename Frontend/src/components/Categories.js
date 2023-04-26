import './Categories.css';
import React from 'react';
import { Card, Row} from 'react-bootstrap';
import Image1 from '../Images/Card-1.jpg';
import Image2 from '../Images/Card-2.jpg';
import Image3 from '../Images/Card-3.jpg';
import Image4 from '../Images/Card-4.jpg';

class Categories extends React.Component {
    
  render() {
    const imgStyle = {
        width:"auto",
        height:"50%",
        padding:"4%",
        paddingBottom: "0"
    }


    return (
        <div className="card-main">
            <Row md="5">
                <Card className="card-body">
                <Card.Img variant="top" src={Image1} style={imgStyle}/>
                    <Card.Body>
                        <Card.Title>Fashion</Card.Title>
                        <hr/>
                        <Card.Text>
                            Men's Clothing, Women's Clothing, Shoes, etc.
                        </Card.Text>
                    </Card.Body>
                </Card >
                <Card className="card-body">
                    <Card.Img variant="top" src={Image2} style={imgStyle}/>
                    <Card.Body>
                        <Card.Title>Electronics</Card.Title>
                        <hr></hr>
                        <Card.Text>
                            Mobiles, Laptops, TVs, etc.
                        </Card.Text>
                    </Card.Body>
                </Card>
                <Card className="card-body">
                <Card.Img variant="top" src={Image3} style={imgStyle}/>
                    <Card.Body>
                        <Card.Title>Food</Card.Title>
                        <hr></hr>
                        <Card.Text>
                            Compare between varous food delivery apps
                        </Card.Text>
                    </Card.Body>
                    </Card>
                <Card className="card-body">
                    <Card.Img variant="top" src={Image4} style={imgStyle}/>
                    <Card.Body>
                        <Card.Title>Cab Booking</Card.Title>
                        <hr></hr>
                        <Card.Text>
                            Compare cab fares over different platforms
                        </Card.Text>
                    </Card.Body>
                </Card>
            </Row>
        </div>
    );
  }
}

export default Categories;