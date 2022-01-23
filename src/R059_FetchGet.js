import React, { useEffect } from 'react';
import { useState } from 'react/cjs/react.development';

function R059_FetchGet() {
    const [contents, getContents] =useState('')
    
    const [change, getChange] = useState(1)
    useEffect(async() =>{
        const response = await fetch('http://date.jsontest.com/')
        const json = await response.json()
        alert(json.date)
    },[change])
  return <div>
      <button onClick={()=>getChange(0?1:0)}> fetch get</button>
  </div>;
}

export default R059_FetchGet;
