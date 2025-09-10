import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import NavBar from "./components/NavBar";
import Dashboard from "./components/Dashboard";
import Audio from "./pages/Audio";
import Animatous from "./pages/Animatous";
import Ecommerce from "./pages/Ecommerce";
import Crypto from "./pages/Crypto";
import Education from "./pages/Education";
import Tasks from "./pages/Tasks";
import Hermetica from "./pages/Hermetica";
import Stickbot from "./pages/Stickbot";

function App() {
  return (
    <Router>
      <NavBar />
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/audio" element={<Audio />} />
        <Route path="/animatous" element={<Animatous />} />
        <Route path="/ecommerce" element={<Ecommerce />} />
        <Route path="/crypto" element={<Crypto />} />
        <Route path="/education" element={<Education />} />
        <Route path="/tasks" element={<Tasks />} />
        <Route path="/hermetica" element={<Hermetica />} />
        <Route path="/stickbot" element={<Stickbot />} />
      </Routes>
    </Router>
  );
}

export default App;
