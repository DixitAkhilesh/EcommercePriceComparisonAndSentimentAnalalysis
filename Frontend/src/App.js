import React from 'react';
import { useRoutes } from 'react-router-dom';
import Home from './components/Home';
import SearchElectronics from './components/SearchElectronics';
import SearchFashion from './components/SearchFashion';
import AmazonDetails from './components/AmazonDetails';
import FlipkartDetails from './components/FlipkartDetails';
import Electronics from './components/Electronics';

function App() {
  const routes = [
    { path: '/', element: <Home /> },
    { path: '/searchElectronics', element: <SearchElectronics /> },
    { path: '/searchFashion', element: <SearchFashion /> },
    { path: '/electronics', element: <Electronics /> },
    { path: '/Amazondetails', element: <AmazonDetails /> },
    { path: '/Flipkartdetails', element: <FlipkartDetails /> },
  ];

  const routing = useRoutes(routes);

  return (
    <div>
      {routing}
    </div>
  );
}

export default App;
