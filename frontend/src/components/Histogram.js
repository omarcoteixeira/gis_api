import React, { Component } from 'react';

class Histogram extends Component {

    constructor(props) {
        super(props);

        this.state = {
            image: [],
            isLoading: true,
        };
    }

    componentDidMount() {
        fetch(`http://localhost:5000/document/${this.props.mapId}/histogram`)
            .then(res => res.blob())
            .then(
                (result) => {
                    var blobUrl = URL.createObjectURL(result);

                    this.setState({
                        image: blobUrl,
                        isLoading: false,
                    });
                },
                (error) => {
                    console.error(error);
                }
            )
    }

    render() {
        return (
            <div className="Histogram">
                <div className="content">
                    <h2 className="subtitle is-size-5">Histograma de NDVI</h2>
                    <img src={this.state.image} />
                </div>
            </div>
    );
  }
}

export default Histogram;
