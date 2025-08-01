import { useState } from "react";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  const sendOne = () => {
    setCount(count + 1);
  };

  return (
    <>
      <div className="card">
        <button onClick={sendOne}>
          Press the button to send plus 1 to backend
          <br />
          current value {count}
        </button>
      </div>
    </>
  );
}

export default App;
