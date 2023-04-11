import React, { Component, Fragment } from "react";
import ReactDOM from "react-dom";
import Header from "./layout/Header";

export default function App() {
  return (
    <div>
        <Header/>
    </div>
  )
}

ReactDOM.render(<App />, document.getElementById("app"));
