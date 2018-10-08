import React, { Component } from 'react';
import './App.css';
import 'bulma/css/bulma.css'

import MapViewer from './components/MapViewer'

class App extends Component {
    render() {
        return (
            <div className="App">
                <MapViewer/>
            </div>
        );
    }
}

export default App;
