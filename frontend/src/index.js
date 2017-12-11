import React from 'react';
import Axios from 'axios';
import ReactDOM from 'react-dom';
import './index.css';
import registerServiceWorker from './registerServiceWorker';
import Main from "./Main";


ReactDOM.render(
  <Main/>, document.getElementById('root'));
registerServiceWorker();
