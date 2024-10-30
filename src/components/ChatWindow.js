import React, { useState, useEffect, useRef } from "react";
import { getAIMessage } from "../api/api";
import MessagesList from "./MessagesList";
import InputArea from "./InputArea";
import "./ChatWindow.scss";

function ChatWindow() {
  const defaultMessage = [{ role: "assistant", content: "Hi, how can I help you today?" }];
  const [messages, setMessages] = useState(defaultMessage);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSend = async (input) => {
    if (input.trim() !== "") {
      setMessages((prevMessages) => [...prevMessages, { role: "user", content: input }]);

      try {
        const newMessage = await getAIMessage(input, messages);
        setMessages((prevMessages) => [...prevMessages, { role: "assistant", content: newMessage }]);
      } catch (error) {
        console.error("Error fetching AI message:", error);
        setMessages((prevMessages) => [
          ...prevMessages,
          { role: "assistant", content: "Sorry, something went wrong." }
        ]);
      }
    }
  };

  return (
    <div className="container">
      <div className="messages-container">
        <MessagesList messages={messages} />
        <div ref={messagesEndRef} /> {/* Scroll anchor */}
      </div>
      <InputArea onSend={handleSend} />
    </div>
  );
}

export default ChatWindow;