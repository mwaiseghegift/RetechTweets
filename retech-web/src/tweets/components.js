import React, {useEffect, useState} from 'react'

import {loadTweets, createTweet} from '../db_lookup'


export function TweetsComponent(props){

  const textAreaRef = React.createRef()
  const [newTweets, setNewTweets] = useState([])
  const handleSubmit = (event) => {
    event.preventDefault()
    const newVal = textAreaRef.current.value
    let tempTweets = [...newTweets]

    createTweet(newVal, (response, status, e) =>{
      if (status === 201){
        tempTweets.unshift(response)
      }else{
        alert('an error occured')
      }

    })


    setNewTweets(tempTweets)
    console.log(newVal)
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
        const myCallback = (response, status) => {
          if (status === 200){
            setTweetsInit(response)
            setTweetsDidSet(true)
          }else{
            alert("There was an error")
          }
        }
        loadTweets(myCallback)
      }

    },[tweetsInit, tweetsDidSet, setTweetsDidSet])
    return tweets.map((item, index)=>{
      return <Tweet tweet={item} className="my-5 py-5 border bg-white text-dark" key={`${index}-{item.id}`}/>
    })
  }

export function ActionBtn(props){
    const {tweet, action} = props

    const [likes, setLikes] = useState(tweet.likes ? tweet.likes:0)
    const [userLike, setUserLike] = useState(false)
 
    const className = props.className ? props.className :'btn btn-primary btn-sm'
  
    const actionDisplay = action.display ? action.display : "Action"
    const handleClick = (event) => {
      event.preventDefault()
      if (action.type === 'like'){
        if (userLike === true){
          setLikes(likes - 1)
          setUserLike(false)
        }else{
          setLikes(likes + 1)
          setUserLike(true)
        }
      }
    }
    const display = action.type === 'like' ? `${likes} ${actionDisplay}` : actionDisplay
    return <button className = {className} onClick={handleClick}>{display}</button>
  }
  
export function Tweet(props) {
  
    const {tweet} = props
    const className = props.className ? props.className : 'col-10 max-auto col-md-6'
  
    return <div className={className}>
      <p>{tweet.id} - {tweet.content}</p>
      <div className='btn btn-group'>
        <ActionBtn tweet={tweet} action={{type: "like", display: "Likes"}} />
        <ActionBtn tweet={tweet} action={{type: "unlike", display: "Unlike"}} />
        <ActionBtn tweet={tweet} action={{type: "retweet", display: "Retweet"}} />
      </div>
    </div>
  }