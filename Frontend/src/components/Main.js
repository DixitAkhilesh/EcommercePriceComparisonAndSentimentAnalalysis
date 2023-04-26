import "./Main.css"
import NavBar from "./NavBar"
import Body from "./Body"
import Footer from "./Footer"

function Main()
{
    return(
        <div className = "main">
            <NavBar/>
            <Body/>
            <Footer/>
        </div>
    )
}

export default Main;