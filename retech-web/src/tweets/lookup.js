import {backendLookup} from '../db_lookup'

export function retechCreateTweet(newTweet, callback){
    backendLookup('POST','/create-tweet/', callback, {content:newTweet})
  }
  
export function retechTweetList(callback){
    backendLookup('GET','/tweets/', callback)
    }

export function retechTweetAction(tweetId, action, callback){
    const data = {id:tweetId, action:action}
    backendLookup('POST','/tweet/action/', callback,data)
}