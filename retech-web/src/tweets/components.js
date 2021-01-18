import React, {useEffect, useState} from 'react'

import {TweetList} from './list'
import {TweetCreate} from './create'
import {Tweet} from './detail'
import {retechTweetDetail} from './lookup'

export function TweetsComponent(props){
  const [newTweets, setNewTweets] = useState([])
  const canTweet = props.canTweet === "false" ? false:true
  const handleNewTweet = (newTweet) => {
    let tempTweets = [...newTweets]
    tempTweets.unshift(newTweet)
    setNewTweets(tempTweets)
  }



  return <div className={props.className}>
      {canTweet === true && <TweetCreate didTweet={handleNewTweet} className='col-12 mb-3' />}
    <TweetList newTweets={newTweets} {...props}/>
  </div>
}

export function TweetDetailComponent(props){
  const {tweetID} = props
  const [didLookup, setDidLookup] = useState(false)
  const [tweet, setTweet] = useState(null)
  const handleBackendLookup = (response, status) =>{
    if (status === 200){
      setTweet(response)
    }else{
      alert("An error occured, Please try again")
    }
  }
  useEffect(() => {
    if (didLookup === false){
      retechTweetDetail(tweetID, handleBackendLookup)
      setDidLookup(true)
    }
  }, [tweetID, didLookup, setDidLookup])
  return tweet === null ? null : <Tweet tweet={tweet} className={props.className} />
}

  
  



