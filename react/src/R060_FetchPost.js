import React from 'react';
import { useEffect, useState } from 'react';
// fetch POST요청 보내기
function R060_FetchPost() {
    const [contents, getContents] =useState('')
    
    const [change, getChange] = useState(1)
    useEffect(async() =>{
        const response = await fetch('http://date.jsontest.com/',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: {a:"react", b:200},
            })
        const json = await response.json()
        alert(json.date)
    },[])    
  return <div>
      <h1>fetch post</h1>
  </div>;
}

export default R060_FetchPost;
