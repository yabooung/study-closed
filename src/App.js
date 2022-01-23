import react from 'react';

import './App.css';
import FunctionComponent from './R030_FunctionComponent'
import ReactHook from './R031_ReactHook';
import FetchGet from './R059_FetchGet'

function App() {
  return (
   <div>
     <h1>Start React 200! </h1>
     <FunctionComponent contents="[This is FunctionComponent ]"/>
     <ReactHook/>
     <FetchGet/>
   </div>
  );
}

export default App;
