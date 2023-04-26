import "./NavBar.css"

function NavBar()
{
    return(
        <nav className="nav-container sticky-top navbar bg-dark">
            <ul className="right-side">
                <li><a href="#" className="link-light"><b>CompareKar</b></a></li>
            </ul>
            <ul className="left-side">
                <li>
                    <form class="d-flex" role="search">
                        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search"></input>
                        <button class="btn btn-outline-success" type="submit">Search</button>
                    </form>
                </li>
                <li><a href="#" className="link-light">SignUp</a></li>
                <li><a href="#" className="link-light">Login</a></li>
            </ul>
        </nav>
    )
}

export default NavBar;