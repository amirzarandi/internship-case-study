import React from "react";

const parseMessageContent = (content) => {
  // Convert bold text wrapped with ** into <strong> elements
  const boldRegex = /\*\*(.*?)\*\*/g;
  // Convert markdown-style links to anchor elements
  const linkRegex = /\[([^\]]+)\]\((https?:\/\/[^\s]+)\)/g;

  return content
    .replace(boldRegex, '<strong>$1</strong>')
    .replace(linkRegex, '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>');
};

function MessagesList({ messages }) {
  return (
    <>
      {messages.map((msg, index) => (
        <div key={index} className={`message ${msg.role}-message`}>
          <div
          dangerouslySetInnerHTML={{ __html: parseMessageContent(msg.content) }}
        />
        </div>
      ))}
    </>
  );
}

export default MessagesList;
