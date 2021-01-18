import React from 'react'

import {retechTweetAction,} from './lookup'

export function ActionBtn(props){
    const {tweet, action, didPerformAction} = props
    const likes = tweet.likes ? tweet.likes:0
    const className = props.className ? props.className :'btn btn-primary btn-sm'  
    const actionDisplay = action.display ? action.display : "Action"

    const handleBackendActionEvent = (response, status) =>{
      console.log(response, status)
      if((status === 200 || status === 201) && didPerformAction){
        didPerformAction(response, status)
      }
    }

    const handleClick = (event) => {
      event.preventDefault()
      retechTweetAction(tweet.id, action.type, handleBackendActionEvent)

    }
    const display = action.type === 'like' ? `${likes} ${actionDisplay}` : actionDisplay
    return <button className = {className} onClick={handleClick}>{display}</button>
  }