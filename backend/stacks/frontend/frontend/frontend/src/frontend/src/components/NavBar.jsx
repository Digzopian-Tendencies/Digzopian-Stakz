import { Link } from "react-router-dom";

export default function NavBar() {
  return (
    <nav style={{ padding: "1rem", background: "#222", color: "white" }}>
      <Link to="/">Dashboard</Link> |{" "}
      <Link to="/audio">Audio</Link> |{" "}
      <Link to="/animatous">Animatous</Link> |{" "}
      <Link to="/ecommerce">E-Commerce</Link> |{" "}
      <Link to="/crypto">Crypto</Link> |{" "}
      <Link to="/education">Education</Link> |{" "}
      <Link to="/tasks">Tasks</Link> |{" "}
      <Link to="/hermetica">Hermetica</Link> |{" "}
      <Link to="/stickbot">StickBot</Link>
    </nav>
  );
}
