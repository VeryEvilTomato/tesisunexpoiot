//Library imports
import React from 'react';
import ReactDOM from 'react-dom';

//Store imports
import uiStore from './stores/ui';

import './index.css';
import App from './App';

ReactDOM.render(<App uiStore={uiStore} />, document.getElementById('root'));