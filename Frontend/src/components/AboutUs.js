import React from 'react';
import MovingText from 'react-moving-text'

class AboutUs extends React.Component {
  render() {
    return (
        <div>
            <h1 style={{paddingBottom:'10px', textAlign:'center'}}>
                <MovingText type="fadeInFromBottom" duration="1900ms" delay="1s" 
                direction="normal" timing="ease" iteration="1" fillMode="none">
                    About Us
                </MovingText>
            </h1>
            <h2 style={{textAlign:'center'}}>
                <MovingText type="fadeInFromBottom" duration="1900ms" delay="1s" 
                direction="normal" timing="ease" iteration="1" fillMode="none">
                    We help you in buying at best price by comparing over various online platform
                </MovingText>
            </h2>
        </div>
    );
  }
}

export default AboutUs;