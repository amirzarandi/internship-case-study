import React, { useState } from "react";
import "./App.scss";
import ChatWindow from "./components/ChatWindow";

function App() {

  return (
    <div className="App">
      <div className="heading">
        Instalily Case Study
      </div>
        <ChatWindow/>
    </div>
  );
}

export default App;
