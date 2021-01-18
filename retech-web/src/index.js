import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import {TweetsComponent, TweetDetailComponent} from './tweets'
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

const e = React.createElement
if (retechTweets){
  ReactDOM.render(
    e(TweetsComponent, retechTweets.dataset),
    retechTweets
  );  
}

const tweetDetailElement = document.querySelectorAll(".retech-tweet-detail")

tweetDetailElement.forEach( container => {
  ReactDOM.render(
    e(TweetDetailComponent, container.dataset),
    container
  );
})
// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
