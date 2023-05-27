import React from 'react';

function Footer() {
  return (
    <footer className="bg-dark text-white py-3" style={{ marginTop: 'auto' }}>
      <div className="container-fluid" style={{ display: 'flex', flexDirection: 'column', height:'30px'}}>
        <div className="row flex-grow-1">
          <div className="col-md-6">
            <p>&copy; 2023 CompareKar</p>
          </div>
          <div className="col-md-6 text-md-end">
            <p>Contact Us | Privacy Policy</p>
          </div>
        </div>
      </div>
    </footer>
  );
}

export default Footer;
