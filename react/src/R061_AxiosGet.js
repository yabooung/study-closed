import react from "react";
import axios from "axios";
import { useState, useEffect } from "react";

function R061_AxiosGet() {
    useEffect(()=>{
        axios.get('http://date.jsontest.com/')
        .then(response=> {console.log(response.data.date)})
        .then(alert('axios get'))
    })
  return <div>axios get</div>;
}

export default R061_AxiosGet;
