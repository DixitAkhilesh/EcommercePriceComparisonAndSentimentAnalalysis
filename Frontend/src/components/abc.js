import React, { useState, useEffect } from 'react';

function MyComponent() {
    const [lists, setLists] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetch('/flipkart_list')
        .then(response => response.json())
        .then(data => setLists(data))
        .catch(error => setError(error));
    }, []);

    console.log(lists);
    return (
    <div>
        Hello
    </div>
    );
    
}

export default MyComponent;
