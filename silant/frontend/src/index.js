import App from "./components/App";
import { Provider } from "react-redux";
import { createRoot } from 'react-dom/client';
import React from "react";
import { ReactDOM } from "react";
import { store } from "./store";



createRoot(document.getElementById('root')).render(<Provider store={store}> <App /> </Provider>)