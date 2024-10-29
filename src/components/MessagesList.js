import React from "react";

function MessagesList({ messages }) {
  return (
    <>
      {messages.map((msg, index) => (
        <div key={index} className={`message ${msg.role}-message`}>
          {msg.content}
        </div>
      ))}
    </>
  );
}

export default MessagesList;
