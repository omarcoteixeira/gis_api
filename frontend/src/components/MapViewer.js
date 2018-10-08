import React, { Component } from 'react';
import { Map, Marker, Popup, TileLayer } from 'react-leaflet';

const position = [51.505, -0.09];
class MapViewer extends Component {

    constructor(props) {
        super(props);

        this.mapId = 'bd74fcb4-3f4a-4769-bc8f-a9a5c6cc8893';
        this.apiPath = 'http://localhost:5000/document/';

        this.defaultURL = this.apiPath.concat(this.mapId);
    }

    componentDidMount() {
        // fetch()
        //     .then(res => res.text())
        //     .then(
        //         (result) => {
        //             console.log(result);
        //         },
        //         (error) => {
        //             console.error(error);
        //         }
        //     )
    }

    render() {
        return (
            <div className="MapViewer">
                <div className="columns">
                    <div className="column is-full">
                        <div className="content map">
                          <Map center={position} zoom={13}>
                            <TileLayer
                              url={this.defaultURL}
                            />
                            <Marker position={position}>
                              <Popup>A pretty CSS3 popup.<br />Easily customizable.</Popup>
                            </Marker>
                          </Map>
                        </div>
                    </div>
                </div>
                <div className="columns">
                    <div className="column">
                        <div className="content">
                            <h2 className="subtitle is-size-5">Camadas</h2>
                        </div>
                    </div>
                    <div className="column">
                        <div className="content">
                            <h2 className="subtitle is-size-5">Histograma de NDVI</h2>
                        </div>
                    </div>
                    <div className="column">
                        <div className="content">
                            <h2 className="subtitle is-size-5">Informações da Cena</h2>
                        </div>
                    </div>
                    <div className="column">
                        <div className="content">
                            <h2 className="subtitle is-size-5">Ponto Selecionado</h2>
                        </div>
                    </div>
                </div>
            </div>
    );
  }
}

export default MapViewer;
