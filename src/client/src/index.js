import React from 'react';
import ReactDOM from 'react-dom';

//Store imports
import uiState from './stores/ui'

import './index.css';
import App from './App';

ReactDOM.render(<App 
    uiState={uiState}
    />
    ,document.getElementById('root'));