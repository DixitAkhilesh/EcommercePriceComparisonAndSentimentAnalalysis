import FlipkartSentiments from "./FlipkartSentiments";
import Flipkart from "./Flipkart";
import { useLocation } from 'react-router-dom';
import Footer from "./Footer";

function FlipkartDetails(){
    const location = useLocation();
    const productUrl = location.state.url;
    console.log(productUrl);
    return(
        <div>
            <div>
                <div>
                    <Flipkart />
                </div>
                <div>
                    <FlipkartSentiments />
                </div>
            </div>
            {/* <Footer/> */}
        </div>
    )
}

export default FlipkartDetails;