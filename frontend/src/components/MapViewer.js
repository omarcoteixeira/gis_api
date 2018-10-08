import React, { Component } from 'react';
import { Map, Marker, Popup, TileLayer } from 'react-leaflet';

import Layer from "./Layer";
import Histogram from "./Histogram";
import SceneInfo from "./SceneInfo";
import SelectedPoint from "./SelectedPoint";

const position = [0, 0];
class MapViewer extends Component {

    constructor(props) {
        super(props);

        this.ndvi = false;
        this.defaultURL = this.createURL();
    }

    componentDidMount() { }

    createURL() {
        const mapType = this.ndvi ? 'ndvi' : 'default';

        this.mapId = 'bd74fcb4-3f4a-4769-bc8f-a9a5c6cc8893';
        this.defaultURL = `http://localhost:5000/document/${this.mapId}/${mapType}/{z}/{x}/{y}`;
        console.log(this.defaultURL);
    }

    onLayerChanged() {
        console.log('Layer Changed.')
    }

    render() {
        return (
            <div className="MapViewer">
                <div className="columns">
                    <div className="column is-full">
                        <div className="content map">
                          <Map center={position} zoom={-10}>
                            <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"/>
                          </Map>
                        </div>
                    </div>
                </div>
                <div className="columns">
                    <div className="column">
                        <Layer mapId={this.mapId} onChange={this.onLayerChanged}/>
                    </div>
                    <div className="column">
                        <Histogram mapId={this.mapId}/>
                    </div>
                    <div className="column">
                        <SceneInfo mapId={this.mapId}/>
                    </div>
                    <div className="column">
                        <SelectedPoint mapId={this.mapId}/>
                    </div>
                </div>
            </div>
    );
  }
}

export default MapViewer;
