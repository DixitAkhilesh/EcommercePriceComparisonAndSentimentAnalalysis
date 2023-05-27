import 'bootstrap/dist/css/bootstrap.min.css';  
import {Container ,Card,Row, Button} from 'react-bootstrap';  
import img2 from '../Images/Card-2.jpg';
import img1 from '../Images/Card-1.jpg';  
import { NavLink } from 'react-router-dom';


function App() {  
    return (  
        <div style={{display: 'flex', paddingLeft: '15%'}}>  
            <Container className='p-4' style={{flex: 1}}>  
                <Row>  
                    <Card  
                        text={'dark'}  
                        style={{width:"50%",height: "450px"}}  
                        className="m-2" 
                    >  
                    <Card.Img src={img2} style={{height: '250px', widht:'300px'}} />
                        <Card.Body style={{textAlign:'center'}}>  
                            <Card.Title style={{textAlign:'center'}}>Electronics</Card.Title>
                            <hr />
                            <Card.Text>  
                                Laptops, Smartphones, Refrigerators, etc...
                            </Card.Text>  
                            <NavLink to="/searchElectronics"><Button>Search</Button></NavLink>
                        </Card.Body>  
                    </Card>  
                </Row>  
            </Container>  
            
            <Container className='p-4' style={{flex: 1}}>  
                <Row>  
                    <Card  
                        text={'dark'}  
                        style={{width:"50%",height:'450px'}}  
                        className="m-2" 
                    >  
                    <Card.Img src={img1} style={{height: '250px', widht:'300px'}} />
                        <Card.Body style={{textAlign:'center',height:'40%'}}>  
                            <Card.Title style={{textAlign:'center'}}>Fashion</Card.Title>
                            <hr />
                            <Card.Text>  
                                Clothing, Shoes, Wearables...
                            </Card.Text>  
                            <NavLink to="/searchFashion"><Button>Search</Button></NavLink>
                        </Card.Body>  
                    </Card>  
                </Row>  
            </Container>  
        </div>  
    );  
}  
export default App;  