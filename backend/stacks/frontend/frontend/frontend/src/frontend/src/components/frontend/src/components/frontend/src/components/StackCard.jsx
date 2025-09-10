export default function StackCard({ title, description }) {
  return (
    <div style={{
      border: "1px solid #ccc",
      borderRadius: "8px",
      margin: "1rem",
      padding: "1rem"
    }}>
      <h2>{title}</h2>
      <p>{description}</p>
    </div>
  );
}
