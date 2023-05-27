import "./Home.css"
import NavBar from "./NavBar"
import Body from "./Body"
import Footer from "./Footer"

function Home()
{
    return(
        <div className="home">
            <NavBar/>
            <Body/>
            <Footer/>
        </div>
    )
}

export default Home;