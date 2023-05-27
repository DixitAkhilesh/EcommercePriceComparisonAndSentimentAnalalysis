import React, { useState, useEffect } from 'react';
import Chart from 'react-google-charts';
import './Sentiment.css';

const FlipkartSentiments = () => {
    const [showData, setShowData] = useState(false);
    const [loading, setLoading] = useState(false);
    const [data, setData] = useState(null);
    const [countdown, setCountdown] = useState(10);

    useEffect(() => {
        let interval = null;
        if (countdown === 0) {
        setLoading(true);
        interval = setInterval(() => {
            fetch('http://localhost:5000/details/flipkart')
            .then((response) => response.json())
            .then((data) => {
                const lastTenData = data.slice(-100);
                const chartData = [
                    ['Sentiment', 'Count'],
                    ['Positive', lastTenData.filter((item) => item === 'Positive').length],
                    ['Negative', lastTenData.filter((item) => item === 'Negative').length],
                    ['Neutral', lastTenData.filter((item) => item === 'Neutral').length],
                ];
                setData(chartData);
                setLoading(false);
                setShowData(true);
                clearInterval(interval);
            })
            .catch((error) => {
                console.error(error);
                setLoading(false);
            });
        }, 1000);
        }
        return () => clearInterval(interval);
    }, [countdown]);

    useEffect(() => {
        if (!showData && countdown > 0) {
        const timer = setInterval(() => setCountdown(countdown - 1), 1000);
        return () => clearInterval(timer);
        }
    }, [countdown, showData]);

    const Poptions = {
            pieSliceText: "label",
            pieHole: 0.4,
            colors: ['#F8E831', '#047BD5', '#F7A200'],
            pieSliceBorderColor: 'black', // Set the border color
            pieSliceTextStyle: {
                color: 'black',
            },
            slices: {
                1: { offset: 0.2},
                2: { offset: 0.4},
            },
            chartArea: {width: 400, height: 300}    
    };
    
    return (
        <div className="flipkart-sentiments" style={{marginTop: '2%', marginBottom:'2%'}}>
        <div className="chart-container">
            {showData && (
            loading ? (
                <p>Loading...</p>
            ) : (
                <div className="chart-wrapper">
                    <div className="chart-title">
                        <h1>Sentiment Analysis</h1>
                    </div>
                    <div className="chart">
                        <Chart
                        chartType="PieChart"
                        data={data}
                        options={Poptions}
                        width={'100%'}
                        height={'400px'}
                        />
                    </div>
                </div>
            )
            )}
        </div>
        {!showData && (
            <div className="countdown">
                <div className="loading-container">
                    <div className="loading-spinner" />
                    <div className="loading-text"><h4>Loading...</h4></div>
                </div>
            </div>
        )}
        </div>
    );
};

export default FlipkartSentiments;
