import React, { Component } from 'react';

class SelectedPoint extends Component {
    componentDidMount() {

    }

    render() {
        return (
            <div className="SelectedPoint">
                { this.props.selectedPoint && (
                    <div className="content">
                        <h2 className="subtitle is-size-5">Ponto Selecionado:</h2>
                        <div>
                          <p>Latitude: {this.props.selectedPoint && this.props.selectedPoint.lat}</p>
                          <p>Longitude: {this.props.selectedPoint && this.props.selectedPoint.lng}</p>
                        </div>
                        <div>
                          <button onClick={() => this.props.onResetClick()}>
                            Limpar
                          </button>
                        </div>
                    </div>
                )}
            </div>
    );
  }
}

export default SelectedPoint;
