import React, { Component } from 'react';

class SceneInfo extends Component {

    constructor(props) {
        super(props);

        this.state = {
            info: [],
            isLoading: true,
        };
    }

    componentDidMount() {
        fetch(`http://localhost:5000/document/${this.props.mapId}/meta`)
            .then(res => res.json())
            .then(
                (result) => {
                    const keys = Object.keys(result);
                    const info = keys.map((t) => `${t}: ${result[t]}` );

                    this.setState({
                        info: info,
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
            <div className="SceneInfo">
                <div className="content">
                    <h2 className="subtitle is-size-5">Informações da Cena</h2>
                    <div>
                        { this.state.info }
                    </div>
                </div>
            </div>
    );
  }
}

export default SceneInfo;
