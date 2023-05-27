import AmazonSentiments from "./AmazonSentiment";
import Amazon from './Amazon';
import { useLocation } from 'react-router-dom';
import Footer from "./Footer";

function AmazonDetails()
{
    const location = useLocation();
    const productUrl = location.state.url;
    console.log(productUrl);
    return(
        <div>
            <div>
                <div>
                    {/* <Amazon /> */}
                </div>
                <div>
                    <AmazonSentiments />
                </div>
            </div>
            {/* <Footer/> */}
        </div>
    )
}

export default AmazonDetails;