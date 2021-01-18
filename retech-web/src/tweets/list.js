import React, {useEffect, useState} from 'react'
import {Tweet} from './detail'

import {
  retechTweetList, 
  } from './lookup'

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
        retechTweetList(props.username, handleTweetListLookup)
      }

    },[tweetsInit, tweetsDidSet, setTweetsDidSet, props.username])

    const handleDidRetweet = (newTweet) => {
      const updateTweetsInit = [...tweetsInit]
      updateTweetsInit.unshift(newTweet)
      setTweetsInit(updateTweetsInit)
      const updateFinalTweets = [...tweets]
      updateFinalTweets.unshift(tweets)
      setTweets(updateFinalTweets)
    }
     

    return tweets.map((item, index)=>{
      return <Tweet tweet={item} 
      didRetweet={handleDidRetweet} className="my-5 py-5 border bg-white text-dark" key={`${index}-{item.id}`}/>
    })
  }