import {BrowserRouter, Routes, Route} from "react-router-dom";
import React from "react";
import Coverage from "./component/covrage";
import NavbarX from "./component/navbar";
import Schedule from "./component/schedule";

function App() {
  return (
      <div>
          <NavbarX />
      <BrowserRouter>
          <Routes>
              <Route path="/" element={<Coverage />} />
              <Route path="generate-coverage" element={<Schedule />} />
          </Routes>
      </BrowserRouter>
      </div>
  );
}

export default App;
