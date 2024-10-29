import React, { useState } from "react";
import "./ChatWindow.scss";

function InputArea({ onSend }) {
  const [input, setInput] = useState("");

  const handleInputChange = (e) => {
    setInput(e.target.value);
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  const handleSend = () => {
    if (input.trim() !== "") {
      onSend(input);
      setInput("");
    }
  };

  return (
    <div className="input-area">
      <input
        value={input}
        onChange={handleInputChange}
        onKeyDown={handleKeyDown}
        placeholder="Type a message..."
      />
      <button className="send-button" onClick={handleSend}>
        Send
      </button>
    </div>
  );
}

export default InputArea;
