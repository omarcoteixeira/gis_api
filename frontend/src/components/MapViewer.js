import React, { Component } from 'react';
import { Map, TileLayer, GeoJSON } from 'react-leaflet';

import Layer from "./Layer";
import Histogram from "./Histogram";
import SceneInfo from "./SceneInfo";
import SelectedPoint from "./SelectedPoint";

class MapViewer extends Component {

    constructor(props) {
        super(props);

        this.mapId = 'bd74fcb4-3f4a-4769-bc8f-a9a5c6cc8893';

        this.state = {
            layers: {
                ndvi: false,
                trueColor: true
            },
            center: [-10.6095247833, -45.7885489402],
            originalCoordinates: [],
            currentCoordinates: [],
            currentLat: 0,
            currentLng: 0,
            selectedPoint: null,
            isLoading: true,
            zoom: 12,
            minZoom: 1,
            maxZoom: 15
        };
    }

    componentDidMount() {
        fetch(`http://localhost:5000/document/${this.mapId}/coordinates`)
            .then(res => res.json())
            .then(
                (coordinates) => {
                    this.setState({
                        originalCoordinates: coordinates,
                        currentCoordinates: coordinates,
                        isLoading: false,
                    });
                },
                (error) => {
                    console.error(error);
                }
            )
    }

    onLayerChange(layer) {
        this.state.layers[layer] = !this.state.layers[layer];
    }

    onResetClick() {
        this.setState({
            selectedPoint: null
        });
    }

    onMouseMove(event) {
        this.setState({
            currentLat: event.latlng.lat,
            currentLng: event.latlng.lng,
        });
    }

    onMapClick(event) {
        this.setState({
            selectedPoint: event.latlng
        });
    }

    render() {
        return (
            <div>
                <div className="map-container">
                  <Map center={this.state.center}
                       zoom={this.state.zoom}
                       minZoom={this.state.minZoom}
                       maxZoom={this.state.maxZoom}
                       onMouseMove={this.onMouseMove.bind(this)}
                       onClick={this.onMapClick.bind(this)}>

                      <TileLayer
                        attribution=""
                        url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"/>
                      { this.state.layers.ndvi && (
                          <TileLayer
                            url="http://localhost:5000/document/bd74fcb4-3f4a-4769-bc8f-a9a5c6cc8893/ndvi/{z}/{x}/{y}"
                            tms={true}
                            noWrap={true}
                            opacity={0.7}
                            attribution=""/>
                      )}
                      { this.state.layers.trueColor && (
                          <TileLayer
                            url="http://localhost:5000/document/bd74fcb4-3f4a-4769-bc8f-a9a5c6cc8893/tms/{z}/{x}/{y}"
                            tms={true}
                            noWrap={true}
                            opacity={0.7}
                            attribution=""/>
                      )}
                      <GeoJSON data={this.state.currentCoordinates} />
                  </Map>
                </div>
                <div className="box map-controls">
                    <div className="columns">
                        <div className="column">
                            <Layer mapId={this.mapId} onLayerChange={this.onLayerChange.bind(this)}/>
                        </div>
                        <div className="column">
                            <Histogram mapId={this.mapId}/>
                        </div>
                        <div className="column">
                            <SceneInfo mapId={this.mapId}/>
                        </div>
                        <div className="column">
                            <SelectedPoint mapId={this.mapId}
                                           selectedPoint={this.state.selectedPoint}
                                           onResetClick={this.onResetClick.bind(this)}/>
                        </div>
                    </div>
                </div>
            </div>
    );
  }
}

export default MapViewer;
