import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import {TweetsComponent} from './tweets'
import reportWebVitals from './reportWebVitals';



const reactRoot = document.getElementById('root')
const retechTweets = document.getElementById('retech-tweets')

if (reactRoot){
  ReactDOM.render(
    <React.StrictMode>
      <App />
    </React.StrictMode>,
    reactRoot
  );  
}

if (retechTweets){
  ReactDOM.render(
    <React.StrictMode>
      <TweetsComponent />
    </React.StrictMode>,
    retechTweets
  );  
}

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
