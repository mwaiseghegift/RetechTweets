import React, {useEffect, useState} from 'react'

import {
  retechTweetList, 
  retechCreateTweet,
  retechTweetAction,
  } from './lookup'


export function TweetsComponent(props){

  const textAreaRef = React.createRef()
  const [newTweets, setNewTweets] = useState([])

  const handleBackendUpdate = (response, status) => {
    let tempTweets = [...newTweets]
    if (status === 201){
      tempTweets.unshift(response)
      setNewTweets(tempTweets)
    }else{
      alert('an error occured')
    }
  }

  const handleSubmit = (event) => {
    event.preventDefault()
    const newVal = textAreaRef.current.value
    retechCreateTweet(newVal, handleBackendUpdate)
    textAreaRef.current.value = ''
  }

  return <div className={props.className}>
      <div className='col-12 mb-3'>
        <form onSubmit={handleSubmit}>
        <textarea ref={textAreaRef} required = {true} className='form-control'>

        </textarea>
        <button type='submit' className='btn btn-primary my-3'>Tweet</button>
      </form>
    </div>
    <TweetList newTweets={newTweets}/>
  </div>
}

  
  export function TweetList(props){
    const [tweetsInit, setTweetsInit] = useState([])
    const [tweets, setTweets] = useState([])
    const [tweetsDidSet, setTweetsDidSet] = useState(false)
  
    useEffect(() => {
      const finalTweetList = [...props.newTweets].concat(tweetsInit)

      if (finalTweetList.length !== tweets.length){
        setTweets(finalTweetList)
      }
    }, [props.newTweets, tweets, tweetsInit])

    useEffect (() => {

      if (tweetsDidSet === false){
        const handleTweetListLookup = (response, status) => {
          if (status === 200){
            setTweetsInit(response)
            setTweetsDidSet(true)
          }else{
            alert("There was an error")
          }
        }
        retechTweetList(handleTweetListLookup)
      }

    },[tweetsInit, tweetsDidSet, setTweetsDidSet])
    return tweets.map((item, index)=>{
      return <Tweet tweet={item} className="my-5 py-5 border bg-white text-dark" key={`${index}-{item.id}`}/>
    })
  }

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

export function ParentTweet(props){
  const {tweet} = props

  return tweet.parent ? <div className='row'>
  <div className='col-11 mx-auto p-3 border rounded'>
  <p className='mb-0 text-muted small'>Retweet</p>
  <Tweet className='' tweet={tweet.parent} /></div>
  </div>: null
} 

export function Tweet(props) {
    const {tweet} = props
    const[actionTweet, setActionTweet] = useState(props.tweet ? props.tweet : null)
    const className = props.className ? props.className : 'col-10 max-auto col-md-6'

    const handlePerformAction = (newActionTweet) => {
      setActionTweet(newActionTweet)
    }

    return <div className={className}>
      <div>
        <p>{tweet.id} - {tweet.content}</p>
        <ParentTweet tweet={tweet}/>
      </div>
    
      {actionTweet &&<div className='btn btn-group'>
        <ActionBtn tweet={actionTweet} didPerformAction={handlePerformAction} action={{type: "like", display: "Likes"}} />
        <ActionBtn tweet={actionTweet} didPerformAction={handlePerformAction} action={{type: "unlike", display: "Unlike"}} />
        <ActionBtn tweet={actionTweet} didPerformAction={handlePerformAction} action={{type: "retweet", display: "Retweet"}} />
      </div>}
      </div> 

  }