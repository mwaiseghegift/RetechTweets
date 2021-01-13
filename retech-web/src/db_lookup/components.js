function getCookie(name){
  var cookieValue = null;
  if (document.cookie && document.cookie !== ''){
     var cookies = document.cookie.split(';');
     for (var i=0; i<cookies.length; i++){
        var cookie = cookies[i].trim();
        //does this cookie name begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + '=')){
           cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
           break;
        }
     }
  }
  return cookieValue;
}

function lookup(method, endpoint, callback, data){
  let jsonData;
  if (data){
    jsonData = JSON.stringify(data)
  }
  const xhr = new XMLHttpRequest()
  const url = `http://127.0.0.1:8000${endpoint}`
  const responseType = 'json'

  xhr.responseType = responseType
  const csrftoken = getCookie('csrftoken')
  xhr.open(method, url)
 
  xhr.setRequestHeader("Content-Type","application/json")
  if(csrftoken){
    // xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest")
    xhr.setRequestHeader("X-Requested-With","XMLHttpRequest")
    xhr.setRequestHeader("X-CSRFToken",csrftoken)
  }

  xhr.onload = function() {
     callback(xhr.response, xhr.status)
  }
  xhr.onerror = function (e){
    callback({"message":"The request prompted an error"})
  }
  
  xhr.send(jsonData)
}


export function createTweet(newTweet, callback){
  lookup('POST','/create-tweet/', callback, {content:newTweet})
}

export function loadTweets(callback){
  lookup('GET','/tweets/', callback)
  }