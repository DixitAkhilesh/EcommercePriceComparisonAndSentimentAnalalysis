import logo from "./logo.svg";
import "./App.css";
import Main from "./components/Main.js";
import Post from "./components/Post.js";
import StringInputForm from "./components/API2";
import ProductList from "./components/JSONFile";
// import MyComponent from "./components/abc.js";
// import {BrowseRouter, Route} from "react-router-dom"

function App() {
    return (
        <div>
            {/* <Post/> */}
            <StringInputForm/>
            {/* <MyComponent/> */}
            {/* <ProductList/> */}
        </div>
        // <div className="App">
        //     <Main/>
        // </div>
    );
}

export default App;
