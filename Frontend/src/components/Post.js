// import React, { useState } from 'react';
// import axios from 'axios';

// function Post() {
//   const [inputString, setInputString] = useState('');
//   const [outputString, setOutputString] = useState('');

//   const handleSubmit = async (event) => {
//     event.preventDefault();
//         try {
//             const response = await axios.post('http://localhost:5000/receive-string', { inputString });
//             const { data } = response;
//             console.log(`String sent to backend: ${inputString}`);
//             console.log(`String received from backend: ${data}`);
//             setOutputString(data);
//         } catch (error) {
//         console.error(error);
//         }
//   };

//   return (
//     <div>
//         <form onSubmit={handleSubmit}>
//             <input type="text" value={inputString} onChange={(event) => setInputString(event.target.value)} />
//             <button type="submit">Send string to backend</button>
//         </form>
//         {outputString && <p>String received from backend: {outputString}</p>}
            
//     </div>
//   );
// }

// export default Post;
