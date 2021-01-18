import React from 'react'


import { 
  retechCreateTweet,
  } from './lookup'


export function TweetCreate(props){
    const textAreaRef = React.createRef()
    const {didTweet} = props
    const handleBackendUpdate = (response, status) => {
      if (status === 201){
        didTweet(response)
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
        <form onSubmit={handleSubmit}>
          <textarea ref={textAreaRef} required = {true} className='form-control'>
  
          </textarea>
          <button type='submit' className='btn btn-primary my-3'>Tweet</button>
        </form>
      </div>
  }